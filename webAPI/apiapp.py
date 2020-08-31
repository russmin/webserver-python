#!/usr/bin/python

import os
import json, io
import sqlite3
import markdown

from flask import Flask, jsonify, g
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
# Create the application instance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.dirname(app.root_path) + '/devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#create the API
api = Api(app)


def get_db():
    db = getattr(g,'_database' , None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    user_id = db.Column(db.String(50))
class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deviceName = db.Column(db.String(50))
    deveui =db.Column(db.String(23))
    devProfile = db.Column(db.String(5))
    networkProfile = db.Column(db.String(7))


# Create a URL route in our application for "/"
@app.route('/')
def index():
    ##Show the Readme doc##
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

class UserList(Resource):
    def get(self):
        UserList = Users.query.all()
        output = []

        for users in UserList:
            user_data = {}
            user_data['name'] = users.name
            user_data['password'] = users.password
            user_data['user_id'] = users.user_id
            output.append(user_data)

        return jsonify({'users': output})

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', required=True)
        parser.add_argument('password', required=True)
        parser.add_argument('user_id', required=True)

        args = parser.parse_args()
        new_user = Users(name= args['name'], password = args['password'], user_id = args['user_id'])
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User Created', 'data': args}, 201
class User(Resource):
    def get(self, identifier):
        user = Users.query.filter_by(user_id = identifier).first()

        if not user:
            return jsonify({'No user found'})
        user_data = {}
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['user_id'] = user.user_id

        return jsonify({'user': user_data})
    def delete():
        return ''
class DeviceList(Resource):
    def get():
        return ''
    def post():
        return ''
class Device(Resource):
    def get(self, identifier):
        return ''
    def delete():
        return ''

##api.add_resource(DeviceList, '/devices')
##api.add_resource(Device, '/device/<string:identifier>')
api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<string:identifier>')
if __name__ =='__main__':
    app.run(debug=True)
