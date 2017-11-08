# Usage:
# Note: The URLs used in this thingie is fetched from yr.no and used in the following manner:
# https://www.yr.no/place/Norway/<some>/<place>/<jeah>/varsel.xml
# More details can be found on the YR.no home pages
#
# forecast = LatestYrForecast("https://www.yr.no/place/Norway/Buskerud/Kongsberg/Kongsberg/varsel.xml");
# temperature = forecast.getTemperature();

import urllib2;
from xml.etree import ElementTree;

class LatestYrForecast:

	def __init__(self, yrUrlVarsel):
		self.yrUrlVarsel = yrUrlVarsel;
		print ("Defined LatestYrForecast with url: {%s}" % (yrUrlVarsel));

	def getForecast(self):
		document = ElementTree.parse(urllib2.urlopen(urllib2.Request(self.yrUrlVarsel, headers={"Accept" : "application/xml"})));
		rootElem = document.getroot();
		imminentForecast = rootElem.findall("forecast")[0].findall('tabular')[0].findall('time')[0];
		if imminentForecast is None:
			print "Unable to fetch the weatherdata for location :'(";
			return None;
		else:
			return imminentForecast;

	def getTemperature(self):
		forecast = self.getForecast();
		if forecast is None:
			return None;
		else:
			return forecast.find('temperature').get('value');
