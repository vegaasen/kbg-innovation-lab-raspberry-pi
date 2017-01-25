from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
#	templateFile = open("temp.json",'r')
#	test = templateFile.read()
	return "Bentern"
	
@app.route("/sensor/temperature/degree")
def tempDegree():
	templateFile = open("web.html",'r')
	temperature = templateFile.read()
	return temperature

@app.route("/sensor/temperature/humidity")
def tempHumidity():
	templateFile = open("temperatureSensor.json",'r')
	temperature = templateFile.read()
	return temperature

if __name__ == "__main__":
    app.run()
