from flask import Flask
import pandas as pd


app = Flask(__name__)


@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "<h1>Welcome to my 'Home' page!</h1>"


@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)