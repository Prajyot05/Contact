from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__) # Initialises the Flask Application
CORS(app) # Disable the CORS error for us so that we are able to send Cross Origin Requests to our app

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) # Creates a database instance that gives us access to the database specified in line 8