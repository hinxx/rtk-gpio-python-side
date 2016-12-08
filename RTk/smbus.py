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

        #Get the address and convert it to 8 bit for mbed and then convert to the char to send over.
        i2caddrchar = chr(int(hex(i2caddress<<1),0))
        #and now convert that to a letter
        self._write("IW") #I2C write
        self._write(i2caddrchar) # Write the 8 Bit I2C address
        self._write(chr(int(len(data))))
        self._write(chr(int(hex(command),0))) # Write the command char
        for idx, dataVal in enumerate(data): #Write each item of data
            self._write(chr(int(hex(dataVal),0))) #Data
            if(idx != len(data)):
            	sleep(i)

    def read_word_data(self,i2caddress,command) :
        i2caddress = hex(i2caddress<<1)
        #and now convert that to a letter
        i2caddrchar = chr(int(i2caddress,0))
        pass
