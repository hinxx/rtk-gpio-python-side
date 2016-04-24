#Program that tests each pin of the RTk.GPIO port
#Import the RTk.GPIO Board
import anyio.GPIO as RTKGPIO
#And now the RPi header
import RPi.GPIO as RPIGPIO
import sys
from time import sleep

#Set the modes
RPIGPIO.setmode(RPIGPIO.BCM)
RTKGPIO.setmode(RTKGPIO.BCM)

#Define GPIO pins
gpios = [4,23,24,25]
errorPins = []

print("Setting up GPIO Outs on the RTK Board")
#Setup the RPi
for gpio in gpios:
	print(gpio)
	RTKGPIO.setup(gpio, RTKGPIO.OUT)

print("Setting up GPIO Ins on the RPi Board")
for gpio in gpios:
	print(gpio)
	RPIGPIO.setup(gpio, RPIGPIO.IN)

print("Now Testing")
for gpio in gpios:
	print("Testing GPIO%s",str(gpio))
	print("Turning off")
	RTKGPIO.output(gpio,0)
	sleep(0.1)
	print("Reading input")
	input1 = RPIGPIO.input(gpio)

	print("Turning on")
	RTKGPIO.output(gpio,True)
	sleep(0.1)
	print("Reading input")
	input2 = RPIGPIO.input(gpio)	
	if(input1 == 0 and input2 ==1):
		print("GPIO Pin Passed")
	else:
		errorPins.append(gpio)
		print("GPIO Pin Failed")
		print(input1)
		print(input2)
	sleep(0.1) #Sleep buffers required
	
if(len(errorPins) > 0):
	print("Errors Detected")
	print(errorPins)
	sys.exit("Not all GPIO Pins passed")
else:
	print("Passed!")

print("Tests done")
