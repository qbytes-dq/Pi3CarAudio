#Read the temperature from an LM335 from analogue input 1 
#in A/D in the PCF8591P @ address 74
from smbus import SMBus

# comment out the one that does not apply to your board
bus = SMBus(0) # for revision 1 boards
#bus = SMBus(1) # for revision 2 boards
address = 74
Vref = 4.35
convert = Vref / 256

print "Read the temperature"
print "Ctrl C to stop" 
bus.write_byte(address, 1) # set control register to read channel 1

while(0 == 0): # do forever
   reading = bus.read_byte(address) # read A/D 1
   voltage = convert * reading
   # Temperature is 0.010 V per degree C
   temp = (voltage - 2.7315) *100 # should read 2.7315V at 0 C
   temp = temp + 1.0 # calibration adjustment
  # print"A/D reading",reading,"meaning",round(voltage,2),"V", " Temperature",round(temp,0)," degrees C"
   print" Temperature",int(temp)," degrees C"

