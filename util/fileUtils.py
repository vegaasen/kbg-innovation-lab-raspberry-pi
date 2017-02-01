# @since 01.02.2017
# @usage write(json.dumps(temperaturen, default=lambda o: o.__dict__), "../temperatureSensor.json");

import os;

class FileUtils:

    def __init__(this):

    def write(what, where):
    	file=open(where, "w+");
    	file.write(what);
    	file.close();
    	print (what + " written to " + where);

    write = staticmethod(write);
