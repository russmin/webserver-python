# About
This application uses flask and flask extentions to create a simple websever and API in python. For more information about these libraries used in the app see the docs below


- *Flask* is lightwieght web appliction framework for python.
[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
- *Flask-Restful* is an extension for Flask that adds support for quickly building REST APIs.
[Flask-restful Documentation](https://flask-restful.readthedocs.io/en/latest/index.html)
- *Flask-sqlalchemy* is a flask extension that adds support for sqlalchemy(database toolkit) for flask
[Flask-sqlalchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

Flask has many more extensions to extend your web applications. [Popular flask extensions](https://www.fullstackpython.com/flask-extensions-plug-ins-related-libraries.html)

# How to Run Application On conduit
install python3 to the conduit
```
  $ sudo opkg install python3
  $ sudo opkg install python3-modules
```
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
$ python3
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
$ python3 apiapp.py
```

# API Documentation

## List all users
### Definition 'GET /users'

**Response**

```json
 [ { "username": "Adam", "password": "sharkl139737"} ]
```
on success

## Add New User
### Definition 'POST /users'

**Arguments**

"username": string' user name
"password": string' password for user

on success
```
[ { "username": "Adam", "password": "sharkl139737", } ]
```
## Delete a User
### Definition 'DELETE /users'

**Response**

`'message': 'No user found'` if no user found
`{'message': 'The user has been deleted'}` on sucess

## List all LoraMessages
### Definition 'GET /LoraMessage'

**Response**

```json
[ {
    "deviceName": "TempSensor",
    "deveui": "00-80-00-00-04-01-80-4d",
    "appeeui": "01-01-01-01-01-01-01",
    "data": "SF12BW125",
    "size" : 12,
    "timestamp" : "2020-09-02T09:02:02.648602Z",
    "sqn" : 22
    }
  ]
```
## Adding a new LoraMessage
### Definition 'POST /LoraMessage'

**Arguments**

"deviceName": string' friendly name for device
"deveui": string' unique device EUI
"appeui": string' app eui
"data": string' network class profile
"size": integer
"timestamp": string'
"sqn": integer


`"message": Lora Message Added", 201` on success
```json
{
  "deviceName": "TempSensor",
  "deveui": "00-80-00-00-04-01-80-4d",
  "appeeui": "01-01-01-01-01-01-01",
  "data": "SF12BW125",
  "size" : 12,
  "timestamp" : "2020-09-02T09:02:02.648602Z",
  "sqn" : 22
}
```

## Lookup LoraMessage details for a specific device
### Definition 'GET /LoraMessage/deveui/'

**Response**
`Lora Message not found` if the LoraMessage does not exists

on success
```json
{   
  "LoraMessageName": "TempSensor",
  "deveui": "00-80-00-00-04-01-80-4d",
  "appeeui": "01-01-01-01-01-01-01",
  "data": "SF12BW125",
  "size" : 12,
  "timestamp" : "2020-09-02T09:02:02.648602Z",
  "sqn" : 22
 }
```
