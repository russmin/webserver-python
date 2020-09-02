# How to Run Application

install all required libraries libraries using pip
for Example:
```
  pip install flask
  pip install flask-restful
  pip install flask_sqlalchemy
  pip install werkzeug.security
```


# API Documentation

## List all users

*Definition 'GET /users'*

**Response**

`200 OK` on success
```
json [ { "username": "Adam", "password": "sharkl139737", } ]
```
*Definition 'POST /devices'*

**Arguments**

"username": string' user name
"password": string' password for user
If a device with given identifier already exists, the existing device will be overwritten Response
```
[ { "username": "Adam", "password": "sharkl139737", } ]
```
List all devices
Definition 'GET /devices'

**Response**

'200 OK' on success
```json [ { "deviceName": "TempSensor", "deveui": "00-80-00-00-04-01-80-4d", "devProfile": "US915", "networkProfile": "CLASS-A" } ]
```
## Adding a new Device

*Definition "POST /devices'*

**Arguments**

"deviceName": string' friendly name for device
"deveui": string' unique device EUI
"devProfile": string' the Lora device profile
"networkProfile": string' network class profile
If a device with given identifier already exists, the existing device will be overwritten Response

`"201 Device Added"` on success
```
{ "deviceName": "TempSensor", "deveui": "00-80-00-00-04-01-80-4d", "devProfile": "US915", "networkProfile": "CLASS-A" }
```

## Lookup device details 'GET /device/'

**Response**
`Device not found` if the device does not exists

```
{ "deviceName": "TempSensor", "deveui": "00-80-00-00-04-01-80-4d", "devProfile": "US915", "networkProfile": "CLASS-A" } '''
```
## Delete a device 'DELETE /devices/'

*Response*
`Device Not found` if the device does not exist
`204 No Content` on success
