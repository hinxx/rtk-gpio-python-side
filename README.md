RTk.GPIO Python Library
=====

[![Build Status](http://rtkjenkins.servehalflife.com:8120/jenkins/buildStatus/icon?job=RTKGPIOPY)](http://rtkjenkins.servehalflife.com:8120/jenkins/job/RTKGPIOPY/)

Originally based on AnyIO by David Whale (@whaleygeek). The idea was then improved and put together with new hardware designed by Ryanteck LTD.

The library replicates most of the same functions as RPi.GPIO library and then these functions instead send commands to the RTk.GPIO board to emulate GPIO.

This package is the python module that runs on a Windows, Mac or Linux machine (or technically anything that can run python & pyserial). Firmware which is programmed onto the microcontroller can be found at our other repository.

The two communicate over a serial API which we've written and will be documented soon.


This package consists of two parts - a Python module that runs on a PC,
Mac or Linux machine (well, anything that can run Python and pyserial),
and some firmware that is programmed to a microcontroller.

 The two are linked together by a serial port controlled by the pyserial
library. Calls to the anyio.GPIO methods on the host computer will
cause reads or writes to the GPIO pins on the microcontroller platform.


In this way, it is possible to write a hardware control program on any
platform, that can easily be ported between different platforms
(including the Raspberry Pi). Just change the "import RPi.GPIO as GPIO"
to "import anyio.GPIO as GPIO" and change your pin numbers, and you'll
be working in no time!


The serial link between the two parts runs at varying speeds depending o the microcontroller, and each
command is only a few characters, so the system performs reasonably well
unless you are repeatedly polling or changing lots of GPIO's at the same
time.

The arduino pro micro runs at 115200 Baud and the <Insert new board here> at a faster baud rate.


Board Options
----
Currently the <Insert new board here> is being funded on kickstarter over at

You can also buy an arduino pro mico pre-programmed ready to go from:
http://skpang.co.uk/catalog/pro-micro-33v8mhz-with-headers-and-anyio-firmware-p-1327.html

All you need to do is plug it in, download this module by choosing
the "Download as Zip" button, unzip the file and run the test programs,
and you'll be working in no time!

You can also program your own pro micro and flash the firmware located at anyio/arduino/firmware/gpio/gpio.ino to get going.





USE OF PYSERIAL
----

This module uses pyserial to communicate with the Arduino Pro Micro.

anyio modifies the Python PACKAGEPATH for you when it runs,
to make sure that it uses this embedded pyserial rather than one
that might or might not be installed on your system. This means
that if you don't have pyserial installed on your system, you should
still be able to just run this out of the box and it should work.

If you already have pyserial installed and want to use your installed
version for any reason, you can change the anyio/arduino/GPIO.py
USE_EMBEDDED_PYSERIAL = False


FUTURE WORK
----

This package contains a console based (text mode) simulator that can be
used to test your programs on before you connect to real hardware, and
this supports both inputs and outputs. This console package
works, but is not completely documented yet. You can try it with this:
import anyio.console.GPIO as GPIO


The GPIO interface itself could be anything, not just an Arduino.
There is a very simple protocol between the python module and the target
GPIO hardware, that is written in a way to allow future extension to
support other hardware peripherals such as I2C, SPI, UART, PWM, Analog,
OneWire and other protocols and features aimed at near real time control
and sensing.


There are placeholders in the design for a tkinter GUI simulator that I
am planning to write soon, and also a network aware version, that
allows GPIO controls to be sent remotely over a network connection to
a GPIO server running on any arbitrary host computer (e.g. a Raspberry Pi).


NOTES ABOUT COPYRIGHTED MATERIAL
----

The source code in the anyio package is (c) 2014 David Whale.

There is an embedded version of pyserial inside the anyio package, and
this is provided in it's entirely complete form, with it's original
licence, which allows for it to be embedded inside other packages with
out any special install.

There is an embedded version of the ProMicro.inf file, which came from
the SparkFun github repository. It is included here for convenience,
but the latest copy can always be retrieved from here:

https://github.com/sparkfun/SF32u4_boards/blob/master/driver/ProMicro.inf


David Whale

@whaleygeek

June 2014
