
# Flask Restful API
**Flask** is a micro-framework for Python. It allows you to build websites and web apps quite rapidly and easily, it's really good and light

## Problem Statement
Given data for country and capital. To insert these data in sqlite db , so that  cost of API response time become minimum . My approach -

 1. create a new text file "country_list.txt" and paste all the data of country and capital. ***data given are in comma seperated  Country, Capital and Capital in some case***
 2. in app.py read this txt file using csv.reader using delimiter  `,`
 3. convert  it into panda dataframe with Columns [Country, Capital, temp]
 4. merging two column capital and temp where temp has value with `()
 5. removing column temp
 6. removing all empty row and country without capital
 7. inserting column id with autoincremtn
 8. converting dataframe into sql insert query
   ***code***
    
	    import pandas as pd
	    import numpy as np
		import csv
		
	    with open('country_list.txt', 'r', encoding="utf-8") as csvfile:
		    csv_reader = csv.reader(csvfile, delimiter=",")
		    df = pd.DataFrame(csv_reader, columns=['Country', 'Capital', 'temp'])
		    df['Capital'] = np.where(df['temp'].isnull(), df['Capital'], f['Capital']+'('+df['temp']+')')
		    df = df.drop(columns=['temp'])
		    df.dropna(inplace=True)
		    df.insert(0, 'id', range(0, 0+len(df)))
		    df.to_sql('country', con=db.engine, index=False, if_exists='replace')
		csvfile.close()

`	**Conclusion**
In future if country and capital data get change we just need to copy & paste the data into country_list.txt file. Data will automatically inserted into sqlite db.

##  Rest API
|HTTP Method  | CRUD Operation  | Description |
|--|--|--|
| POST | Search| Search Country Capital `/capital`|
| GET  | READ  |Retrieve all Country Capital `/capital`|
| GET| READ| Retrieve single Country Capital `/capital/<country>`|


## To Execute 

 - **To Test**
  `python test.py`
  
 - **To run** 
 `python app.py`
 - **To run in Production (UNIX based)**
  `gunicorn app:app`

## Unit Testing
Flask provides a way to test your application by exposing the Werkzeug test and handling the context locals for us.
### *Test cases*
|  S.NO| Test Case|
|--|--|
| 1|Testing the index page response  |
| 2| Testing country capital response |
| 3| Testing country capital from post method and redirect check|
| 4| Testing incorrect counry name |


## Dependency
|dependency|version|
|--|--|
|autopep8|1.4.4|
|Click|7.0|
|Flask|1.1.1|
|flask-marshmallow|0.10.1|
|Flask-SQLAlchemy|2.4.0|
|gunicorn|19.9.0|
|itsdangerous|1.1.0|
|Jinja2|2.10.1|
|MarkupSafe|1.1.1|
|marshmallow|3.0.5|
|marshmallow-sqlalchemy|0.19.0|
|numpy|1.17.2|
|pandas|0.25.1|
|pycodestyle|2.5.0|
|python-dateutil|2.8.0|
|pytz|2019.2|
|six|1.12.0|
|SQLAlchemy|1.3.8|
|Werkzeug|0.15.6|

## command

1. pip3 install virtualenv
2. virtualenv env => creating isolated python environment
3. source env/Scripts/activate => activating virtualenv
4. pip3 install flask
5. pip3 install flask-sqlalchemy
6. pip3 install autopep8
7. pip3 install pandas
8. python app.py => running application
9. pip3 install autopep8
10. pip3 install flask_marshmallow
11. pip3 install marshmallow-sqlalchemy
12. python test.py => testing application
13.  pip3 install gunicorn
14. pip3 freeze > requirements.txt => exporting dependency used to txt file
15. heroku login
16. touch Procfile
17. heroku create country-capital-api
18. git push heroku prod:master
