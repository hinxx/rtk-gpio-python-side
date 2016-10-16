#RTK.GPIO implementation of SMBUS
import rtkserial

serial = rtkserial.s

def _write(str):
    serial.write(str)

def write_i2c_block_data(i2caddress,command,data):
    #Get the address and convert it to 8 bit for mbed
    i2caddress = hex(i2caddress<<1)
    #and now convert that to a letter
    i2caddrchar = chr(int(i2caddress,0))
    #Now write address to serial port
    _write("IW") #I2C write
    _write(i2caddrchar)
