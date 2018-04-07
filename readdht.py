import RPi.GPIO as GPIO 
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11 
pin = 4 

while True : 
	hum ,temp = Adafruit_DHT.read_retry(sensor,pin)
	if hum is not None and temp  is not None :
		print 'Temp ={0:0.1f}*C Humi = {1:0.1f}%'.format(temp,hum)
		time.sleep(2)
	else :
		print 'Failed to get read'
