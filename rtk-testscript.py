#RTk.GPIO Test script
DEBUG = True
rtkGPIOPort = ""
import serial.tools.list_ports
serialPorts = serial.tools.list_ports.comports()

for port in serialPorts:
    if( "1a86:7523" in port[2].lower() or "1a86:7523" in port[2].lower()):
        if(DEBUG):
            print ("RTk.GPIO Found on port: "+port[0])
        rtkGPIOPort = port[0]
        break
if(rtkGPIOPort == ""):
	print ("\nError: RTk.GPIO not detected.\nFor more support please visit our website at http://Ryanteck.com/rtk-000-00C\nPress enter to close.")
	input()
	exit()

#print ("Debug cable fully detected fine.\n Press enter to launch the terminal.")


BAUD = 230400


s = serial.Serial(rtkGPIOPort)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
#s.write_timeout =
s.timeout = 1

s.close()
s.port = rtkGPIOPort
s.open()
s.write("VV".encode('ascii'))
print(str(s.read(size=20)))
