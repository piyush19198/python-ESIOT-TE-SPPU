import time, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)

GPIO.output(3, True)

time.sleep(1)