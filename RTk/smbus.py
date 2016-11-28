#RTK.GPIO implementation of SMBUS
import rtkserial
import pprint
from time import sleep
serial = rtkserial.s
print("imported rtkbus")
i = 0.0017
class SMBus:

    def __init__(self,bus):
        self.bus = bus
    def _write(self,str):
        #print((str))
        serial.write(str)

    def write_i2c_block_data(self,i2caddress,command,data):

        #pprint.pprint(str(i2caddress)+","+str(command)+","+str(data))
        #Get the address and convert it to 8 bit for mbed
        i2caddress = hex(i2caddress<<1)
        #and now convert that to a letter
        i2caddrchar = chr(int(i2caddress,0))
        self._write("IW") #I2C write
        #sleep(i)
        self._write(i2caddrchar) # Write the 8 Bit I2C Address
        #sleep(i)
        self._write(chr(int(len(data))))

        #sleep(i)
        self._write(chr(int(hex(command),0))) # Write the command char
        #sleep(i)
        #Now write address to serial port
        for idx, dataVal in enumerate(data): #Write each item of data
            #print(chr(int(hex(dataVal),0)))
            self._write(chr(int(hex(dataVal),0))) #Data
			if(idx != len(data)):
            	sleep(i)
        #print("wrote block")
        #raw_input()
