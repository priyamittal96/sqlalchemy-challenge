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
        "/api/v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Retrieve the last 12 months of precipitation data
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Perform a query to retrieve the data and precipitation scores
    date_prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    
    precipitation = {date: prcp for date, prcp in date_prcp}
    print(precipitation)
    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    # List the stations
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    
    return jsonify(stations)


# @app.route("/api/v1.0/tobs")
# def tobs():

# @app.route("/api/v1.0/<start>")
# def start():

# @app.route("/api/v1.0/<start>/<end>")
# def start_end():



if __name__ == "__main__":
    app.run(debug=True)