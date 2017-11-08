# This requires the following to exists:
# MySQLdb python package.
# Raspberry: sudo apt-get install python-mysqldb
# OSX:
import MySQLdb;
import base64;

class Database:

    def __init__(this, username, password, hostname, database):
        this.username = username;
        this.password = password;
        this.hostname = hostname;
        this.database = database;
        print("username %s, hostname %s" % (username, hostname));

    def connect(this):
        if this.db is None:
            this.db = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="vegard11", db="iot");
        if this.cursor is None:
            this.cursor = db.cursor();

    def query(this, what):
        connect();
        this.cursor.execute(what);
        return cur.fetchall();

    def disconnect(this):
        this.db.close;

database = Database("root", "vegard11", "localhost", "iot");
# print all the first cell of all the rows
for row in database.query("SELECT * FROM iot_home_temperature"):
    print row;

database.disconnect();
