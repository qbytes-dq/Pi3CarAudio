# LED_trace1 - Buf -- restistor -- A1 -- LED -- Gnd
# Print the voltage across an LED an voltage applied to LED and resistor
from smbus import SMBus
from time import sleep

# comment out the one that does not apply to your board
bus = SMBus(0) # for revision 1 boards
#bus = SMBus(1) # for revision 2 boards
address = 74
control = 1<<6 | 1 # enable analogue output and set to read A1
Vref = 4.44
convert = Vref / 256

print("Output a ramp on the D/A")
print("Ctrl C to stop")
while(True): # do forever
 for v in range(28,256): # start close to 0.7V
     bus.write_byte_data(address, control, v) # trigger last value to D/A 
     bus.write_byte_data(address, control, v) # trigger this value to D/A
     reading = bus.read_byte(address) # read to kick off conversion
     reading = bus.read_byte(address) # read value
     Vbuf = (convert * v) - 0.7 # compensate for 0.7V lost in the bufferd output
     if Vbuf < 0:
         Vbuf = 0
     Vin = convert * reading
     if Vin > Vbuf:
         Vbuf = Vin
     Vout = convert * v # raw output voltage
     print "Out",round(Vout,2),"V Buffered",round(Vbuf,2) , "V --> Measured input 1 ", round(Vin,2),"V"
     sleep(0.01)
