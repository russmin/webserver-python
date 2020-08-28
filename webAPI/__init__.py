#!/usr/bin/python
import markdown
import os

from flask import Flask, jsonify

# Create the application instance
app = Flask(__name__)

# Create a URL route in our application for "/"
@app.route('/')
def index():

    with open(os.path.dirname(app.instance_path) + '/README.md', 'r') as markdown_file:
        #Read the content of the FILE
        content = markdown_file.read()

        #Convert to HTML
        return markdown.markdown(content)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
