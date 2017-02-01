from flask import Flask
import sys
import Adafruit_DHT
import json
from Components.temperature.tempHumidity import TemperatureSensor
app = Flask(__name__)

@app.route("/")
def root():
#	templateFile = open("temp.json",'r')
#	test = templateFile.read()
    return "Bentern"
	
@app.route("/sensor/temperature/degree")
def tempDegree():
    sensor = TemperatureSensor(Adafruit_DHT.DHT11, "26");
    temperaturen = sensor.getTemperature("heihei.out");
    return json.dumps(temperaturen, default=lambda o: o.__dict__)

@app.route("/sensor/temperature/humidity")
def tempHumidity():
    templateFile = open("temperatureSensor.json",'r')
    temperature = templateFile.read()
    return temperature

if __name__ == "__main__":
    app.run()
