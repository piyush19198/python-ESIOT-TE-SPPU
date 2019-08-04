import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
#GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
	i=GPIO.input(11)

        if i==1:                 #When output from motion sensor is LOW
 	      print "Detected", i
#             GPIO.output(3, 0)  #Turn OFF LED
              time.sleep(0.5)
        elif(i==0):
              print "Clear",i
#             GPIO.output(3, 1)  #Turn ON LED
              time.sleep(0.5)

