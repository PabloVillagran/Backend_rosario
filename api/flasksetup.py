from flask import Flask, request, jsonify
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api
from flask_cors import CORS
import conexion as c_params

app = Flask(__name__)
api = Api(app)
con_string = "mariadb+mysqlconnector://"+c_params.con_string
app.config['SQLALCHEMY_DATABASE_URI'] = con_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

CORS(app)

db = SQLAlchemy(app)
mellow = Marshmallow(app)

