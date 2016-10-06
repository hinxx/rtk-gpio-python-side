# anyio/arduino/GPIO.py  21/04/2014  D.J.Whale
#
# An ardunio (serial) based GPIO link

# CONFIGURATION ========================================================

DEBUG = False
# There was the option to use the serial library pre-installed. This has changed so that we know the python lib in use is the one distributed with the rtk library.
#If you wish to use the built in one instead change the import rtkserial to import serial which is below (Approx line 38)

MIN_PIN = 0
MAX_PIN = 27

IN      = 0
OUT     = 1
BCM     = 0
BOARD   = 1
HIGH    = 1
LOW     = 0

PUD_OFF = 20
PUD_DOWN = 21
PUD_UP = 22
VERSION = "RTk.GPIO 0.1A"
RPI_REVISION = 3


# OS INTERFACE =========================================================

from .. import protocol
from .. import adaptors
import anyio.rtk.portscan as portscan

from os import sys, path
thisdir = path.dirname(path.abspath(__file__))
sys.path.append(thisdir)

import rtkserial as serial


# STATIC REDIRECTORS ===================================================

# Find out if there is a pre-cached port name.
# If not, try and find a port by using the portscanner

name = portscan.getName()
if name != None:
  if DEBUG:
    print("Using port:" + name)
  PORT = name
else:
  name = portscan.find()
  if name == None:
    raise ValueError("No port selected, giving in")
  PORT = name
  print("Your anyio board has been detected")
  print("Now running your program...")

BAUD = 230400


s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

s.close()
s.port = PORT
s.open()


instance = protocol.GPIOClient(adaptors.SerialAdaptor(s), DEBUG)

def setwarnings(option):
  instance.setwarnings(option)

def setmode(mode):
  instance.setmode(mode)

def setup(channel, mode,pull_up_down=None):
  instance.setup(channel, mode,pull_up_down)

def input(channel):
  return instance.input(channel)

def output(channel, value):
  instance.output(channel, value)

def analogIn(channel):
  return instance.cake(channel)

def cleanup():
  instance.cleanup()


# END
