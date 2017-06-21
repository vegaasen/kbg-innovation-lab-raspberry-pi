
import RPi.GPIO as GPIO
from time import sleep
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.cleanup()

GPIO.setup(26,GPIO.IN)
GPIO.setup(2,GPIO.OUT)



while True:
	knapp = GPIO.input(26)
	GPIO.output(2,GPIO.HIGH)
	if knapp == False:
		print "knapp YEAH!!"
		#sleep(0.5)
		#os.system('clear')
		while knapp == False:
			knapp = GPIO.input(26)
