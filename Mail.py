import RPi.GPIO as GPIO
from subprocess import call
import time
import os
import glob
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import subprocess
import sys

gmail_user = "@gmail.com"
gmail_pwd = ""
FROM = '@gmail.com'
TO = ['@gmail.com'] #must be a list

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(25, GPIO.OUT)

#GPIO.output(25, False)
               
time.sleep(1)
msg = MIMEMultipart()
time.sleep(1)
msg['Subject'] ="testing msg send from python"
time.sleep(1)
fp = open("ddd.jpg", 'rb')
time.sleep(1)
img = MIMEImage(fp.read())
time.sleep(1)
fp.close()
time.sleep(1)
msg.attach(img)
time.sleep(1)
try:
	server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
	print "smtp.gmail"
        server.ehlo()
	print "ehlo"
        server.starttls()
	print "starttls"
        server.login(gmail_user, gmail_pwd)
	print "reading mail & password"
        server.sendmail(FROM, TO, msg.as_string())
	print "from"
        server.close()
        print 'successfully sent the mail'
 #       GPIO.output(25, True)
        time.sleep(2)
  #      GPIO.output(25, False)

except:
	print "failed to send mail"
#	GPIO.output(25, False)

#GPIO.cleanup()
sys.exit(1)

