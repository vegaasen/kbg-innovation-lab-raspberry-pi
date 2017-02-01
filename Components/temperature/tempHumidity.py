from time import sleep
from RPi import GPIO
import os
import Adafruit_DHT
import json

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

def write(what,where):
	file=open(where, "w+");
	file.write(what);
	file.close();
	print (what + " written to " + where);

class Temperature:

	def __init__(this, humidity, temperature):
		this.humidity = humidity;
		this.temperature = temperature;

	def __str__(this):
		return "Humidity {%s}, Temperature {%s}" % (this.humidity, this.temperature);

class TemperatureSensor:

	def __init__(this, sensorType, pinLocation):
		this.sensorType = sensorType;
		this.pinLocation = pinLocation;
		print ("Defined Temperature with sensorType: {%s}, pinLocation {%s}" % (sensorType, pinLocation));

	def __str__(this):
		return "hei object";

	def getTemperature(this, logLocation):
		print (this);
		humidity,temperature = Adafruit_DHT.read_retry(this.sensorType,this.pinLocation);
		candidate = Temperature(0, 0);
		if humidity is not None:
			candidate.humidity = humidity;
		if temperature is not None:
			candidate.temperature = temperature;
		print ("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature,humidity))
		return candidate;

sensor = TemperatureSensor(Adafruit_DHT.DHT11, "26");
temperaturen = sensor.getTemperature("heihei.out");
write(json.dumps(temperaturen, default=lambda o: o.__dict__), "../temperatureSensor.json");
