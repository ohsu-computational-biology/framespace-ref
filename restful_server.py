import os
from flask import Flask
from flask_restful import Resource, Api
import os

from pymongo import MongoClient

from api.units import Units

# app = Flask(__name__)
# name passed to flask app will bind to db
app = Flask('framespace')
api = Api(app)

# if not docker, then run locally
try:
  mongo = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
except:
  mongo = MongoClient()

db = mongo['framespace']

api.add_resource(Units, '/units', '/units/search', resource_class_kwargs={'db': db})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
