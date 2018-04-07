import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) #defind pin 12 input pull up 
status = 0 
while True : 
	if(status == 0 ) : 
		GPIO.output(11,GPIO.HIGH)
		print("Input high")
	else: 
		GPIO.output(11,GPIO.LOW)
		print("input low")
	time.sleep(0.5)
	if(GPIO.input(12)==0):
		time.sleep(0.1)
		while(GPIO.input(12)==0):
			time.sleep(0.1)
		status = ~status 
