# importing library
import csv
import pandas as pd
import numpy as np

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configuring flask with sqlite db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
db = SQLAlchemy(app)

# table or model for sqlite db
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Country = db.Column(db.String(100), nullable=False)
    Capital = db.Column(db.String(100), nullable=False)

# entry point to run the application
if __name__ == '__main__':
    app.run()
