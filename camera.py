import urllib2
import subprocess
r=urllib2.urlopen("http://192.168.43.1:8080/shot.jpg")
o=open("ddd.jpg","wb")

subprocess.Popen("sudo python sms.py",shell=True).communicate()
subprocess.Popen("sudo python Mail.py",shell=True).communicate()

o.write(r.read())
o.close()
