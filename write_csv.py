import os
import time 
from time import sleep
from datetime import datetime

file = open("/home/pi/data_log.csv", "a")
i=0
if os.stat("/home/pi/data_log.csv").st_size == 0:
	file.write("Time,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n")

while (i<50):
	i=i+1
	now = datetime.now()
	file.write(str(now)+','+str(i)+','+str(-i)+','+str(i-10)+','+str(i+5)+','+str(i*i)+'\n')
	file.flush()
	print i
	time.sleep(0.25)
file.close() 
print "Close"
