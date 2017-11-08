import Adafruit_DHT;
import urllib2;
import sys;
from Components.temperature.DHT11 import TemperatureSensor;
from latestYrForecast import LatestYrForecast;

device = "undefined";
hostname = device;

if len(sys.argv) == 2:
    device = sys.argv[1];

sensor = TemperatureSensor(Adafruit_DHT.DHT11, "26");

if sensor is None:
    print "Sensor is undefined. Skipping :-)";
else:
    try:
        hostname = urllib2.urlopen("http://ifconfig.me/ip").read();
    except (urllib2.HTTPError, urllib2.URLError) as e:
        print "Unable to fetch IP. Set to undefined."

    forecast = LatestYrForecast("https://www.yr.no/place/Norway/Buskerud/Kongsberg/Kongsberg/varsel.xml");
    url = "https://www.vegaasen.com/iot/thermostat.php?temperature=" + str(sensor.getTemperature()) + "&humidity=" + str(sensor.getHumidity()) + "&outsideTemperature=" + str(forecast.getTemperature());
    url = url + "&location=" + device + "&author=vegaasen" + "&device=" + hostname;
    try:
        req = urllib2.Request(url, "Aasen' RaspberryPI");
        handle = urllib2.urlopen(req);
        print handle;
    except urllib2.HTTPError as e:
        if e.code == 404:
            print "not found :-)"
        else:
            print e;
    except urllib2.URLError as e:
        print e;
        print "LOL";
    else:
        print "WTF? :-)";
