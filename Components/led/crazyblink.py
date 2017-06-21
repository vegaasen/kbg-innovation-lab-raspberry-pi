
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

stopp = 0

while stopp != 1:
	stopp = 1
	GPIO.output(26,GPIO.LOW)
	GPIO.output(19,GPIO.HIGH)
	sleep(2)
	GPIO.output(19,GPIO.LOW)
	GPIO.output(26,GPIO.HIGH)
	sleep(2)
	GPIO.output(26,GPIO.LOW)
	GPIO.output(13,GPIO.HIGH)
	sleep(2)
	#Crazy
	t = 100
	while 1 < t:

		t = t - 1
		GPIO.output(26,GPIO.HIGH)
		sleep(0.05)
		GPIO.output(26,GPIO.LOW)
		sleep(0.05)
		GPIO.output(13,GPIO.HIGH)
		sleep(0.05)
		GPIO.output(13,GPIO.LOW)
		sleep(0.05)
		GPIO.output(19,GPIO.HIGH)
		sleep(0.05)
		GPIO.output(19,GPIO.LOW)
		sleep(0.05)

	#skru av alle
	GPIO.output(13,GPIO.LOW)
	GPIO.output(26,GPIO.LOW)
	GPIO.output(19,GPIO.LOW)
GPIO.cleanup()
