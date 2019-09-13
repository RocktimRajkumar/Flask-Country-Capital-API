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


# entry point to run the application
if __name__ == '__main__':
    app.run()
