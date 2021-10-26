import decimal
from flask import Flask, request, jsonify, json
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api
from flask_cors import CORS
import conexion as c_params


class MyJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)



app = Flask(__name__)
api = Api(app)
con_string = "mariadb+mysqlconnector://"+c_params.con_string
app.config['SQLALCHEMY_DATABASE_URI'] = con_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
app.json_encoder = MyJSONEncoder

CORS(app)

db = SQLAlchemy(app)
mellow = Marshmallow(app)

