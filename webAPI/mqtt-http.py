import time
import io, json 					#needed for exporting payloads to json file
import paho.mqtt.client as mqtt

import argparse
import logging
import base64
import binascii
import httplib # be careful for python3!


class mqttStoreForward:

	#class variables
	isConnected = False
	isOnMessage = False
				#checks ethernet connection
	lora_client = mqtt.Client()
	packet = None 							#will carry msg payload...empty to begin
	isJsonEmpty = True 						#keep track of whether file is empty
	jsonFilePath = 'packetStorage.json' #INPUT DESIRED JSON FILE NAME HERE OR LEAVE DEFAULT
	payloadData = None
	devEUI = None

	def __init__ (self):
		#touch jston file if it does not exist
		file = open(self.jsonFilePath, 'a')
		file.close()

	#connect lora client to localhost
	def setLoraClient(self):
		self.lora_client.connect("127.0.0.1")

#callback function initiated on on_connect property for lora client
	def loraOnConnect(self, client, userdata, flags, rc):
		print("Lora Client Connection: " + str(rc)) 	#Returns a 0
		self.lora_client.subscribe("lora/+/up", qos=0)
		self.isConnected = True

	#callback function initiated on on_disconnect property for both clients
	def onDisconnect(self, client, userdata, rc):
		self.isConnected = False
		print("The connection has failed.")


	def rbPayloadFormatters(self, msg):
		msgObj = json.loads(msg)
		newMsg = {}
		msgHex = base64.b64decode(msgObj["data"])
		newMsg["DeviceName"] = "TempSensor"
		newMsg["deveui"] = msgObj["deveui"]
		newMsg["appeui"] = msgObj["appeui"]
		newMsg["data"] = binascii.hexlify(msgHex)
		newMsg["size"] = msgObj["size"]
		newMsg["timestamp"] = msgObj["tmst"]
		newMsg["seq"] = msgObj["seqn"]
		return json.dumps(newMsg)


	#call back function initiated on on_message



	def onMessage(self, mqtt_client, userdata, msg):
		self.packet = self.rbPayloadFormatters(msg.payload)
		pkt = json.loads(self.packet)

		print(self.packet)
		#### HTTP REQUEST GOES HERE ####
		Connection = httplib.HTTPSConnection("localhost:5000/")
		Headers = {"Content-Type": "application/json", "Accept":"application/json"}
		Connection.request("POST", "/devices", self.packet, rbHeaders)
		Response = rbConnection.getresponse()
		ResponseMsg = rbResponse.read()
		### do something with response message ###
		print(ResponseMsg)




   	#set callback properties of both clients to their respective functions(from above)
	def setVals(self):
		self.lora_client.on_connect = self.loraOnConnect
		self.lora_client.on_message = self.onMessage
		self.lora_client.on_disconnect = self.onDisconnect


			#takes packet parameter and appends it to a file
	def writeToJson(self, data):
		with open(self.jsonFilePath, 'a') as myFile:
			myFile.write(data + "\r\n")

 	#Controls what is done with the packet depending on a working/not working connection
	def checkConnect(self, packet):
		if(self.isConnected == True):
			#check whether the file is empty/has stored packets every time the
			#connection is found to be good
			self.checkJsonFile()
			##################################################################################
			#ADD YOUR CODE HERE. WHEN THE CONNECTION IS WOKRING, DECIDE WHAT TO DO WITH PACKET
			##################################################################################
			print("PRINTING PACKET/CONNECTION OK")
			print("PRINTED: " + packet)

		else:
			#When the connection is bad, we write the packet to the json file for storage.
			print("ADDING TO JSON FILE. CONNECTION DOWN") #Ethernet down
			'''FOR TESTING, make sure that this packet matches one printed when it reconnects
			 and forwards packets from json storage: '''
			print("STORED: " + packet)
			self.writeToJson(packet) #store
	#Creates infinite loop needed for paho mqtt loop_forever()
	def runLoop(self):
		while(True):
			time.sleep(1)

	#Creates event loop and new thread that initializes the paho mqtt loops for both clients
	def startLoop(self):
		#UI thread = terminal interaction
		self.lora_client.loop_start()
	def pingCon(self):
		if(self.isOnMessage == True):
			self.pingConsole()
