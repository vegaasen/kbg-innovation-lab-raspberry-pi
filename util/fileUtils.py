import os;

class FileUtils:

    def __init__(this):

    def write(what, where):
    	file=open(where, "w+");
    	file.write(what);
    	file.close();
    	print (what + " written to " + where);
