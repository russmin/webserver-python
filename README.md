# About
This application uses flask and flask extentions to create a simple websever and API in python. For more information about these libraries used in the app see the docs below


- *Flask* is lightwieght web appliction framework for python. 
[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
- *Flask-Restful* is an extension for Flask that adds support for quickly building REST APIs.
[Flask-restful Documentation](https://flask-restful.readthedocs.io/en/latest/index.html)
- *Flask-sqlalchemy* is a flask extension that adds support for sqlalchemy(database toolkit) for flask
[Flask-sqlalchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

Flask has many more extensions to extend your web applications. [Popular flask extensions](https://www.fullstackpython.com/flask-extensions-plug-ins-related-libraries.html)

# How to Run Application

install all required libraries libraries using pip
for Example:
```
  $ pip install flask
  $ pip install flask-restful
  $ pip install flask_sqlalchemy
  $ pip install werkzeug
```
before running the 'apiapp.py' script create the database using the following steps:

- open python
```
$ python
```
- in python run the following lines. this will import the db from the app and create the db tables from the models
```
$ from apiapp import db
$ db.create_all()
```
- exit python
```
exit()
```
next run the apiapp
```
$ python apiapp.py
```

# API Documentation

## List all users
### Definition 'GET /users'

**Response**
 
```
json [ { "username": "Adam", "password": "sharkl139737", } ]
```
on success

## Add New User
### Definition 'POST /users'

**Arguments**

"username": string' user name
"password": string' password for user
If a device with given identifier already exists, the existing device will be overwritten Response
```
[ { "username": "Adam", "password": "sharkl139737", } ]
```
## Delete a User
### Definition 'DELETE /users'

**Response**

`'message': 'No user found'` if no user found
`{'message': 'The user has been deleted'}` on sucess

## List all devices 
### Definition 'GET /devices'

**Response**

```json [ { "deviceName": "TempSensor", "deveui": "00-80-00-00-04-01-80-4d", "devProfile": "US915", "networkProfile": "CLASS-A" } ]
```
## Adding a new Device 
### Definition 'POST /devices'

**Arguments**

"deviceName": string' friendly name for device
"deveui": string' unique device EUI
"devProfile": string' the Lora device profile
"networkProfile": string' network class profile
If a device with given identifier already exists, the existing device will be overwritten Response

`"message": Device Added", 201` on success
```
{ "deviceName": "TempSensor", "deveui": "00-80-00-00-04-01-80-4d", "devProfile": "US915", "networkProfile": "CLASS-A" }
```

## Lookup device details 
### Definition 'GET /devices/<deveui>'

**Response**
`Device not found` if the device does not exists
on success
```
{ "deviceName": "TempSensor", "deveui": "00-80-00-00-04-01-80-4d", "devProfile": "US915", "networkProfile": "CLASS-A" } '''
```

## Delete a device 
### Definition 'DELETE /devices/<deveui>'

**Response**
`Device Not found` if the device does not exist
`204 No Content` on success
