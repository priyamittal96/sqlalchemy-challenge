from flask import Flask, jsonify
import pandas as pd
import datetime as dt
import json
import numpy as np

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

@app.route("/")
def home():
    return (
        "<h1>Welcome to the Hawaii Climate API home page!</h1><br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Retrieve the last 12 months of precipitation data
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Perform a query to retrieve the data and precipitation scores
    date_prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    
    session.close()
    
    precipitation = {date: prcp for date, prcp in date_prcp}
    print(precipitation)
    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    # List the stations
    results = session.query(Station.station).all()
    
    session.close()
    stations = list(np.ravel(results))
    
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Query the dates and temperature observations of the most active station for the last year of data
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281')\
                .filter(Measurement.date >= prev_year).all()
        
    session.close()    
    temps = {date: tobs for date, tobs in results}

    # Return a JSON list of temperature observations (TOBS) for the previous year.
    date_temp = list(np.ravel(temps))
    return jsonify(temps)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_end(start = None, end = None):
    sel = [func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)]
    
    if not end: 
        results = session.query(*sel).filter(Measurement.date >= start).all()
        
        session.close()
        temps = list(np.ravel(results))
        return jsonify(temps)
    
    results = session.query(*sel).filter(Measurement.date >= start)\
            .filter(Measurement.date <= end).all()
    
    session.close()
    temps = list(np.ravel(results))
    return jsonify(temps)



if __name__ == "__main__":
    app.run(debug=True)