# NabazPi
Reviving the Nabaztag Wifi Rabbit using the Raspberry Pi and MQTT.

This repository contains code written for my "NabazPi" project. More info [on my blog](https://www.roytanck.com/tag/nabazpi/).

## Installation
This assumes you have an MQTT broker you can use, and devices that can send messages to it.

* Make sure the Raspberry Pi is running a recent version of Raspbian.
* Make sure Python 3 is installed.
* Install the pip package manager. [more info](https://www.raspberrypi.org/documentation/linux/software/python.md)
* install the paho-mqtt client library. [more info](https://github.com/eclipse/paho.mqtt.python)
* Install eSpeak. [more info](http://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis))
* Copy the 'nabazpi3.py' script to your home directory.

## Usage
On the command line, call the script, providing the broker details.

`./nabazpi3.py -b "iot.example.com" -u "username" -p "password" -s "subject/#"`

This will connect the Pi to the MQTT broker. If no error occurs, you should see:

`Connected with result code 0`

The Pi is now listening for new messages posted to the subject you provided. Next, connect speakers or headphones to the Raspberry Pi, and send a test message to broker. The rabbit should now speak the message, and print a confirmation to stdout:

`Output: "I'm fluent in over six million forms of communication." (return value: 0)`

Have fun!
