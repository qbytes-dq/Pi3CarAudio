#Read a value from analogue input 0 
#in A/D in the PCF8591P @ address 74
from smbus import SMBus

# comment out the one that does not apply to your board
bus = SMBus(0) # for revision 1 boards
#bus = SMBus(1) # for revision 2 boards
address = 74
Vref = 4.3
convert = Vref / 256

print("Read the A/D channel 0")
print("print reading when it changes")
print("Ctrl C to stop")
bus.write_byte(address, 0) # set control register to read channel 0
last_reading =-1

while(0 == 0): # do forever
   reading = bus.read_byte(address) # read A/D 0
   if(abs(last_reading - reading) > 1): # only print on a change
      print"A/D reading",reading,"meaning",round(convert * reading,2),"V"
      last_reading = reading
