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


with open('country_list.txt', 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    df1 = pd.DataFrame(csv_reader, columns=['Country', 'Capital', 'temp'])
    df1['Capital'] = np.where(df1['temp'].isnull(
    ), df1['Capital'], df1['Capital']+'('+df1['temp']+')')
    df1 = df1.drop(columns=['temp'])
    df1.to_sql('country', con=db.engine, index=False, if_exists='replace')
csvfile.close()

# entry point to run the application
if __name__ == '__main__':
    app.run()
