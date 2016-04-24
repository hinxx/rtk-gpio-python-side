# testLED.py - 06/06/2014 D.J.Whale
# Modified by Ryan Walmsley
# Test flashing an LED

import time
t = 0.2


# RTk.GPIO
import anyio.GPIO as GPIO

RED = 22
YEL = 23
GRN = 24
BUZZ = 5
BTN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YEL, GPIO.OUT)
GPIO.setup(GRN, GPIO.OUT)


try:
  while True:
	GPIO.output(RED, True)
	time.sleep(t)
	GPIO.output(YEL, True)
	time.sleep(t)
	GPIO.output(GRN, True)
	time.sleep(2)
	GPIO.output(RED, False)
	time.sleep(t)
	GPIO.output(YEL, False)
	time.sleep(t)
	GPIO.output(GRN, False)
	time.sleep(2)   
finally:
  GPIO.cleanup()
  
# END
