from flask import Flask
import Adafruit_DHT #Can this be removed?
import json

#List of Components
from Components.temperature.temperature import TemperatureSensor
from Components.led.blink import Blink


app = Flask(__name__)

@app.route("/")
def root():
    welcomePageFile = open("web.html",'r')
    welcomePage = welcomePageFile.read()
    return welcomePage

@app.route("/sensor/led/blink/<float:delay>")
def ledBlink(delay):
    sensor = Blink(26);
    blinky = sensor.blink(delay);
    return "blinking in %s" % delay
	
@app.route("/sensor/temperature/degree")
def degree():
    sensor = TemperatureSensor(Adafruit_DHT.DHT11, "26");
    temperaturen = sensor.getTemperature();
    return json.dumps(temperaturen, default=lambda o: o.__dict__)

@app.route("/sensor/temperature/humidity")
def humidity():
    sensor = TemperatureSensor(Adafruit_DHT.DHT11, "26");
    temperaturen = sensor.getHumidity();
    return json.dumps(temperaturen, default=lambda o: o.__dict__)

if __name__ == "__main__":
    app.run()
