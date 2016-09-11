#Pot a sketch - using the four pot box to draw
#A0 - X movement A1 - Y movement
#A2 - Hue A3 - Saturation

import colorsys
from smbus import SMBus
import os, sys, pygame
from pygame.locals import *

import pymouse
mouse = pymouse.PyMouse()
mouse.position()

boardRevision = -1

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Pot a sketch")
screen = pygame.display.set_mode([512,512],0,32)
 
def main(): 
 findRevision()
 if boardRevision == 1 : bus = SMBus(0)
 if boardRevision == 2 : bus = SMBus(1)

 address = 74
 control = 1 << 2 # enable analogue output & auto increment
# bus.write_byte(address, control) # set control register to read channel 0
# dum = bus.read_byte(address)

 current_reading = [0,0,0,0]
 last_reading = [0,0]
 blank_screen()
 col = [0,0,0]

 while(True): # do forever
      checkForQuit()
      print (mouse.position())
      for p in range(0,4): # read all 4 inputs
         #current_reading[p] = 2 * bus.read_byte(address) # read A/D to get current value
         current_reading[p] = 200
      if( (abs(current_reading[1] - last_reading[1]) >1) or (abs(current_reading[0] - last_reading[0]) >1) ):
         col = colorsys.hsv_to_rgb(current_reading[2]/512.0, current_reading[3]/512.0, 0.99)
         pygame.draw.line(screen,(col[0]*255,col[1]*255,col[2]*255),(last_reading[0],last_reading[1]),(current_reading[0],current_reading[1]),2)
         last_reading[0] = current_reading[0] # save this reading for next time
         last_reading[1] = current_reading[1]
         pygame.display.update()

#end of main loop


# Function definitions
def blank_screen():
    screen.fill((255,255,255)) # blank screen
    pygame.display.update()
    
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
        #terminate()
        boardRevision = 2 # assum e

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        if event.key == K_SPACE or event.key == K_DELETE:
           blank_screen()
            

if __name__ == '__main__':
    main()
