
from time import sleep
from RPi import GPIO
import os

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)


#GPIO.setup(26, GPIO.IN)

GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)

while True:
	GPIO.add_event_detect(26, GPIO.RISING)
	if GPIO.event_detected(26):
		print('temp rising')
	#sleep(0.5)
	#os.system('clear') 

GPIO.cleanup()
