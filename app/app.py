from sqlite3 import threadsafety
from flask import Flask
from flaskext.mysql import MySQL
import json
import decimal
from flask.json import JSONEncoder
from flask_cors import CORS,cross_origin

class JsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
CORS(app, resources={r'/api/*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin: *'

## change to name of your database; add path if necessary
mysql = MySQL()
#pp.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'airports'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

# this variable, db, will be used for all SQLAlchemy commands
conn = mysql.connect()
cursor =conn.cursor()


#!/usr/bin/env python
# encoding: utf-8


@app.route('/')
def index():
   cursor1=conn.cursor()
   cursor1.execute("SELECT * FROM airports WHERE iata_code ='LEJ'")
   row_headers=[x[0] for x in cursor1.description] #this will extract row headers
   rv = cursor1.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))
   cursor1.close()
   return json.dumps(json_data)



@app.route('/api/airport/<city>', methods=['GET'])
@cross_origin()
def airport(city):
   cursor2=conn.cursor()
   cursor2.execute("SELECT iata_code FROM airports WHERE municipality LIKE '%"+city+"%'")
   row_headers=[x[0] for x in cursor2.description] #this will extract row headers
   rv = cursor2.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))
   cursor2.close()
   return json.dumps(json_data)


@app.route('/api/city/<iata>',methods=['GET'])
@cross_origin()
def city(iata):
   cursor3=conn.cursor()
   cursor3.execute("SELECT municipality FROM airports WHERE iata_code LIKE '"+iata+"'")
   row_headers=[x[0] for x in cursor3.description] #this will extract row headers
   rv = cursor3.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))
   cursor3.close()
   return json.dumps(json_data)

if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")

cursor.close()



