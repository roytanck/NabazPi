#!/usr/bin/env python3

# NabazPi3.py
# Connect the Raspberry Pi to an MQTT broker, and use eSpeak to have it read messages out loud.
# Requires the 'paho-mqtt' client library (https://github.com/eclipse/paho.mqtt.python).
# Requires eSpeak (http://espeak.sourceforge.net/).
# License: GPL v3 (https://www.gnu.org/licenses/gpl-3.0.en.html).

import os
import subprocess
import paho.mqtt.client as mqtt
# import RPi.GPIO as GPIO
import time
import argparse

# get the command line options
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--broker", help="Broker address", required=True )
parser.add_argument("-u", "--username", help="Broker username", required=True )
parser.add_argument("-p", "--password", help="Broker password", required=True )
parser.add_argument("-s", "--subject", help="Subject to subscribe to", required=True )
args = parser.parse_args()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe(args.subject)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	# decode the byte array that holds our message, and remove double quotes
	message = msg.payload.decode().replace('"','')
	# check if the string is safe to say
	if(check_message(message)):
		# call the function that does the talking
		say_string(message)
	else:
		say_string("I don't think it's safe to say that.")

# Check messages for characters that allow command chaining
def check_message(message):
	if('&' in message or '|' in message):
		return False
	return True

# Helper function to speak strings
def say_string(message):
	# assemble the command
	command = 'espeak -a200 -p40 -ven -k20 "' + str(message) + '" 2>/dev/null'
	# execute command and print the return value
	retvalue = subprocess.call(command, shell=True)
	print('Output: "'+message+'" (return value: '+str(retvalue)+')')

# initialize the client
client = mqtt.Client()
client.username_pw_set(args.username,args.password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(args.broker, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()
