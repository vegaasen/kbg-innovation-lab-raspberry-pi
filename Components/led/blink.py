# @since 01.02.2017
# @usage new Blink(26).blink(1);

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False);

class Blink:

	def __init__(this, pinLocation):
		this.pinLocation = pinLocation;
		print ("Defined Blink with pinLocation {%s}" % (pinLocation));

	def __str__(this):
		return "Blink pinLocation {%s}" % (pinLocation);

	def blink(this, delay=0):
		print ("Blinking with {%s} as the defined delay" % (delay));
		GPIO.setup(this.pinLocation,GPIO.OUT)
		GPIO.output(this.pinLocation, GPIO.HIGH);
		time.sleep(delay);
		GPIO.output(this.pinLocation, GPIO.LOW);
		GPIO.cleanup();
		print ("Blinking finished :-)");

