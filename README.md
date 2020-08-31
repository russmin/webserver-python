Usage

All responses will have this form '''json { "data": "content of the response" "message": Description of what happened? }

Response definition for expected value in 'data field'

List all users
Definition 'GET /users'

Response

'200 OK' on success
'''json [ { "name": "Adam", "password": "sharkl139737", } ]

"POST /devices'

Arguments

"Name": string' user name
"password": string' password for user
If a device with given identifier already exists, the existing device will be overwritten Response

"201 user added" on success ''' [ { "name": "Adam", "password": "sharkl139737", } ]

List all devices
Definition 'GET /devices'

Response

'200 OK' on success
'''json [ { "deviceName": "TempSensor", "deveui": "00-80-00-00-04-01-80-4d", "devProfile": "US915", "networkProfile": "CLASS-A" } ]

##Adding a new Device## Definition

"POST /devices'

Arguments

"deviceName": string' friendly name for device
"deveui": string' unique device EUI
"devProfile": string' the Lora device profile
"networkProfile": string' network class profile
If a device with given identifier already exists, the existing device will be overwritten Response

"201 Device Added" on success ''' { "deviceName": "TempSensor", "deveui": "00-80-00-00-04-01-80-4d", "devProfile": "US915", "networkProfile": "CLASS-A" }

##Lookup device details## 'GET /device/'

Response -'404 Not Found' if the device does not exists

'200 OK' on success
''' { "deviceName": "TempSensor", "deveui": "00-80-00-00-04-01-80-4d", "devProfile": "US915", "networkProfile": "CLASS-A" } '''

Delete a device
DELETE /devices/

Response --'404 Not found' if the device does not exist --'204 No Content' on success

##List all Uplinks##

Definition 'GET /uplinks/'

Response

'200 OK' on success
'''json [ { "deveui": "00-80-00-00-04-01-80-4d", "gatewayeui": "00-80-00-00-00-01-5d-e4" "time": "", "payload": "CLASS-A" "size":

} ]
