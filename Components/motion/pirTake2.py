#https://www.raspberrypi.org/learning/physical-computing-with-python/pir/
#https://www.raspberrypi.org/learning/parent-detector/worksheet/
#bytt om på strøm og jord

from gpiozero import MotionSensor
from datetime import datetime
import MySQLdb

#SQL setup
#Server Connection to MySQL:
conn = MySQLdb.connect(host= "bsoftware.no",
                  user="bsofthim_watcher",
                  passwd="watcher2020",
                  db="bsofthim_theWatcher")

pir = MotionSensor(4)
while True:
    pir.wait_for_motion()
    print("I saw you!!")
    x = conn.cursor()
    try:
        x.execute("""INSERT INTO blueroom VALUES (%s,%s)""",(1,datetime.now()))
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    pir.wait_for_no_motion()
    


