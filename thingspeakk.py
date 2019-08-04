#!/usr/bin/python
import datetime
from datetime import datetime
import RPi.GPIO as GPIO
import time
import decimal
import httplib, urllib
import time
import subprocess
import sys
import Adafruit_DHT

sleep = 2 # how many seconds to sleep between posts to the channel
key = 'GNRSGS61ZETE14L3'  # Thingspeak channel to update
timer=time.time()

while True:
	humidity, temperature = Adafruit_DHT.read_retry(11,2)
	print temperature, humidity
	params = urllib.urlencode({'field1':temperature,'field2':humidity,'key':key})
	headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                print response.status, response.reason
                data = response.read()
                conn.close()
        except:
                print "connection failed"





