# sqlalchemy-challenge
This particular climate analysis is for Hawaii to help plan for the trip based on the weather.

## Technologies
Initial data retrieval and analysis occurred in the jupyter notebook to help visualize and understand the climate analysis based on various criteria. Later using flask, generated an API database that would allow for easy access to all data and filter based on various dates. 

## climate_starter.ipynb
The notebook walks through various sqlalchemy and pandas queries to generate a series of data points detailing counts, plotting precipitation, temperature and looking into summary statistics. 

## app.py
Similar to the jupyter notebook, using sqlalchemy and jsonify, the flask was used to query various parts of the climate analysis into an API. With varius routes highlighting various analyses. 

In order to run this API, please have all files downloaded and run the app.py. Make sure to have the necessary packages installed to be able to run the queries.
