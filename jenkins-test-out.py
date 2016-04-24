#Program that tests each pin of the RTk.GPIO port
#Import the RTk.GPIO Board
import anyio.GPIO as RTKGPIO
#And now the RPi header
import RPi.GPIO as RPIGPIO

#Set the modes
RPIGPIO.setmode(RPIGPIO.BCM)
RTKGPIO.setmode(RTKGPIO.BCM)

#Define GPIO pins
gpios = [2]


print("Setting up GPIO Outs on the RTK Board")
#Setup the RPi
for gpio in gpios:
	print(gpio)
	RTKGPIO.setup(gpio, RTKGPIO.OUT)

print("Setting up GPIO Ins on the RPi Board")
for gpio in gpios:
	print(gpio)
	RPIGPIO.setup(gpio, RPIGPIO.IN)

print("Tests done")
