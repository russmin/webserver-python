#!/usr/bin/python
#######
##Example webserver and webAPI set-up example##
##Written by Russel Ndip##

#import relavent libraries
import os
import json, io
import sqlite3 ##create database for story data created from requests


## imports flask and relavent flask extentions and methods
from flask import Flask, jsonify, g
from flask_restful import Resource, Api, reqparse ## flask extension for building
from flask_sqlalchemy import SQLAlchemy ## flask extension for connecting to a database
from werkzeug.security import generate_password_hash, check_password_hash

# Create the application instance
app = Flask(__name__)
db = SQLAlchemy(app) #create database instance and bind to app
api = Api(app) #create the API instance and bind to app


# Configure sqlite database in the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.dirname(app.root_path) + '/devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JSON_SORT_KEYS"] = False

#connect and return database
def get_db():
    db = getattr(g,'_database' , None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
#closes connection when aplication exits
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#define the table models in database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deviceName = db.Column(db.String(50))
    deveui =db.Column(db.String(23))
    devProfile = db.Column(db.String(5))
    networkProfile = db.Column(db.String(7))


# Create a URL route in our application for "/"
@app.route('/')
def index():
    return "welcome to the app"

#### next set of classes use flask restful to define endpoints and request methods
class UserList(Resource):
    ##get all users##
    def get(self):
        UserList = Users.query.all()
        output = []

        for users in UserList:
            user_data = {}
            user_data['username'] = users.username
            user_data['password'] = users.password

            output.append(user_data)

        return jsonify({'users': output})

    ## create new user##
    def post(self):
        #initialize request parser, set parameter arguments
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        #save arguments into object
        args = parser.parse_args()
        password = args['password']
        username = args['username']
        #hash the password
        hash_password = generate_password_hash(password, method='sha256')

        new_user = Users(username=username, password = hash_password)
        db.session.add(new_user)
        db.session.commit()

        return ({'message': 'User Created', 'data': args}, 201)
class User(Resource):
    def get(self, identifier):
        # get user if exists
        user = Users.query.filter_by(username = identifier).first()
        #handle if user doesn't exist
        if not user:
            return jsonify({'message':'No user found'})
        user_data = {}
        user_data['username'] = user.username
        user_data['password'] = user.password

        return jsonify({'user': user_data})

    def delete(self, identifier):
        user = Users.query.filter_by(username = identifier).first()
        if not user:
                return jsonify({'message': 'No user found'})
        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'The user has been deleted'})

class DeviceList(Resource):
    def get(self):
        DeviceList  = Devices.query.all()
        output = []
        for devices in DeviceList:
            device_data = {}
            device_data["deviceName"] = devices.deviceName
            device_data["deveui"] = devices.deveui
            device_data["devProfile"] = devices.devProfile
            device_data["networkProfile"] = devices.networkProfile

            output.append(device_data)

        return jsonify({'devices': output})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('deviceName', required=True)
        parser.add_argument('deveui', required=True)
        parser.add_argument('devProfile', required=False)
        parser.add_argument('networkProfile', required=False)

        args = parser.parse_args()
        deviceName= args['deviceName']
        deveui = args['deveui']
        devProfile = args['devProfile']
        networkProfile = args['networkProfile']

        new_device = Devices(deviceName=deviceName, deveui=deveui, devProfile= devProfile, networkProfile= networkProfile)
        db.session.add(new_device)
        db.session.commit()
        return ({'message': 'Device Added', 'data': args}, 201)


class Device(Resource):
    def get(self, identifier):
        device = Devices.query.filter_by(deveui= identifier).first()

        if not device:
            return jsonify({'message': 'Device not found'})
        device_data = {}
        device_data['deviceName'] = device.deviceName
        device_data['deveui'] = device.deveui
        device_data['devProfile'] = device.devProfile
        device_data['networkProfile'] = device.networkProfile

        return jsonify({'device': device_data})

# add api routes and endpoints

api.add_resource(DeviceList, '/devices')
api.add_resource(Device, '/devices/<string:identifier>')
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<string:identifier>')
if __name__ =='__main__':
    app.run(debug=True)
