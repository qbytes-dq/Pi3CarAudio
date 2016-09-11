# LED_trace2 - Buf --resistor -- A1 -- LED -- Gnd
# Display the voltage curve across an LED an voltage applied to LED and resistor

from smbus import SMBus
import os, sys, pygame
from time import sleep
from pygame.locals import *
boardRevision = -1

def main():
 pygame.init()
 os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
 pygame.display.set_caption("Applied vs Measured voltage")
 screen = pygame.display.set_mode([300,260],0,32)
 findRevision()
 if boardRevision == 1 : bus = SMBus(0)
 if boardRevision == 2 : bus = SMBus(1)


 print("Esc to stop")
 address = 74
 control = 1<<6 | 1 # enable analogue output and read of A1

 while(0 == 0): # do forever
   checkForQuit()
   last_reading = 0
   for x in range (0, 255):
      bus.write_byte_data(address, control, x) # trigger last value to D/A 
      bus.write_byte_data(address, control, x) # trigger this value to D/A
      reading = bus.read_byte(address) # read to kick off conversion
      reading = bus.read_byte(address) # read value
      pygame.draw.line(screen,(255,255,128),(x-1,260-last_reading),(x,260-reading),4)
      pygame.display.update()
      last_reading = reading # save this reading for next time
   sleep(2) # hold graph
   screen.fill((0,0,0)) # blank screen
   pygame.display.update()

#end of main loop


# Function definitions
def terminate():
    print "Closing down please wait"
    pygame.quit()
    sys.exit()

def findRevision():
    global boardRevision
    fin = open('/proc/cpuinfo')
    boardRevision = -1
    while True: # go through the file line by line
       line = fin.readline()
       if not line: break # end if reached the end of the file
       if "Revision" in line:
         rev = line[11:15]
         if rev == "0002" or rev == "0003" :
           boardRevision = 1
         if rev == "0004" or rev == "0005" or rev == "0006" :
           boardRevision = 2
    fin.close()
    if boardRevision == -1:
        print "Error can't recognise board revision ", rev
        terminate()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key

if __name__ == '__main__':
    main()
