#!/usr/bin/python
#######
##Example webserver and webAPI set-up example##
##Written by Russel Ndip##
#import relavent libraries
import os
import json, io
import sqlite3 ##create database for story data created from requests
import markdown

## imports flask and relavent flask extentions and methods
from flask import Flask, jsonify, g
from flask_restful import Resource, Api, reqparse ## flask extension for building
from flask_sqlalchemy import SQLAlchemy ## flask extension for connecting to a database
from flask_httppauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# Create the application instance
app = Flask(__name__)
db = SQLAlchemy(app) #create database instance and bind to app
api = Api(app) #create the API instance and bind to app
auth = HTTPBasicAuth(app)

# Configure sqlite database in the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.dirname(app.root_path) + '/devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

#define the tables in database
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

@auth.verify_password
def verify_password(username, password)
    user = Users.query.filter_by(name=username).first()

    if user and \ check_password_hash(user.password, password):

# Create a URL route in our application for "/"
@app.route('/')
@auth.login_required
def index():
    return "welcome"

#### next set of classes use flask restful to define endpoints and request methods
class UserList(Resource):
    def get(self):
        UserList = Users.query.all()
        output = []

        for users in UserList:
            user_data = {}
            user_data['username'] = users.username
            user_data['password'] = users.password
            user_data['user_id'] = users.user_id
            output.append(user_data)

        return jsonify({'users': output})

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)


        args = parser.parse_args()
        hash_password = generate_password_hash(args['password'])

        new_user = Users(name= args['name'], password = hash_password, user_id = args['user_id'])
        db.session.add(new_user)
        db.session.commit()

        return ({'message': 'User Created', 'data': args}, 201)
class User(Resource):
    def get(self, identifier):
        user = Users.query.filter_by(username = identifier).first()


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
        return ''
    def post(self):
        return ''
class Device(Resource):
    def get(self, identifier):
        return ''
    def delete(self, identifier):
        return ''

api.add_resource(DeviceList, '/device')
api.add_resource(Device, '/device/<string:identifier>')
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<string:identifier>')
if __name__ =='__main__':
    app.run(debug=True)
