#Usage:
# sensor = TemperatureSensor(Adafruit_DHT.DHT11, "26");
# temperature = sensor.getTemperature();

from time import sleep
from RPi import GPIO
import os
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

NOT_FOUND = -1;

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

	def getTemperatureHumidity(this):
		print (this);
		humidity,temperature = Adafruit_DHT.read_retry(this.sensorType,this.pinLocation);
		candidate = Temperature(0, 0);
		if humidity is not None:
			candidate.humidity = humidity;
		if temperature is not None:
			candidate.temperature = temperature;
		print ("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature,humidity))
		return candidate;

	def getHumidity(this):
		candidate = getTemperatureHumidity();
		if candidate.humidity == 0:
			return NOT_FOUND;
		else:
			return candidate.humidity;

	def getTemperature(this):
		candidate = getTemperatureHumidity();
		if candidate.temperature == 0:
			return NOT_FOUND;
		else:
			return candidate.temperature;
