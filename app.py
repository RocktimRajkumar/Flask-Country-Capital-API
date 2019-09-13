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


# Reading country list with capital from country_list.txt file and adding it to the sqlite database
with open('country_list.txt', 'r', encoding="utf-8") as csvfile:
    # converting string to comma seperated values
    csv_reader = csv.reader(csvfile, delimiter=",")
    # converting comma seperated value to dataframe i.e to tabular form with columns Country, Capital and temp
    df = pd.DataFrame(csv_reader, columns=['Country', 'Capital', 'temp'])
    # Concatenating column temp with Capital only when temp has value
    df['Capital'] = np.where(df['temp'].isnull(
    ), df['Capital'], df['Capital']+'('+df['temp']+')')
    # Dropping column temp
    df = df.drop(columns=['temp'])
    # insert bulk data frame value to database
    df.to_sql('country', con=db.engine, index=False, if_exists='replace')
csvfile.close()

# entry point to run the application
if __name__ == '__main__':
    app.run()
