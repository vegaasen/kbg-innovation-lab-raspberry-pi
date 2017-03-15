import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(4, GPIO.OUT)         #LED output pin
GPIO.output(4,GPIO.HIGH)
while True:
       i=GPIO.input(26)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             #GPIO.output(3, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(4,GPIO.LOW)
             #GPIO.output(3, 1)  #Turn ON LED
             time.sleep(0.1)
