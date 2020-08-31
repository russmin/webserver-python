#!/usr/bin/python
import markdown
import os

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

# Create the application instance
app = Flask(__name__)

#create the API
api = Api(app)

# Create a URL route in our application for "/"
@app.route('/')
def index():
    ##Show the Readme doc##
    with open(os.path.dirname(app.instance_path) + '/README.md', 'r') as markdown_file:
        #Read the content of the FILE
        content = markdown_file.read()

        #Convert to HTML
        return markdown.markdown(content)

class DeviceList(Resource)
    def get(self):

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
