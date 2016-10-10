#TrafficHAT KS Demo
from time import sleep
t = 0.2
import anyio.GPIO as GPIO

RED = 22
YEL = 23
GRN = 24
BUZZ = 5
BUTT = 25

GPIO.setmode(GPIO.BCM)
sleep(t)
GPIO.setup(RED, GPIO.OUT)
sleep(t)
GPIO.setup(YEL, GPIO.OUT)
sleep(t)
GPIO.setup(GRN, GPIO.OUT)
sleep(t)
GPIO.setup(BUZZ,GPIO.OUT)
sleep(t)
GPIO.setup(BUTT,GPIO.IN)
sleep(t)

try:
	while True:
		GPIO.output(RED, True)
		sleep(t)
		GPIO.output(YEL, True)
		sleep(t)
		GPIO.output(GRN, True)
		sleep(2)
		GPIO.output(RED, False)
		sleep(t)
		GPIO.output(YEL, False)
		sleep(t)
		GPIO.output(GRN, False)
		sleep(2)

	
finally:
	GPIO.cleanup()
