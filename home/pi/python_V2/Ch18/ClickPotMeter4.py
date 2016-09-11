#Read a value from all analogue input
#in A/D in the PCF8591P @ address 0x4A or 74
#display it as a 270 degree meter in volts as well as printing the reading

import math
from smbus import SMBus
import os, pygame, sys
from pygame.locals import *
import random
import time

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Works with mouse mover over box - Four Analogue Channel Input Meters")
screen = pygame.display.set_mode([768,160],0,32)
meter = pygame.image.load("images/MeterV270.png").convert_alpha()
meterSurface = pygame.Surface((191,159))
meterSurface.blit(meter,[0,0])
font = pygame.font.Font(None, 16)
meterPositionX = [0, 192, 384, 576]
meterPositionY = [0, 0, 0, 0]
boardRevision = -1
Vref = 4.42
chipAddress = 74

def main():
 findRevision()
 if boardRevision == 1 : bus = SMBus(0)
 if boardRevision == 2 : bus = SMBus(1)

 print("Read the A/D display it as a four voltage meters")
 print("Escape to stop")
 last_reading = [-10, -10, -10, -10] # so you show on the first reading
 ###bus.write_byte(chipAddress, 4) # set control register auto increment
 ###bus.read_byte(chipAddress) # read A/D dummy to flush out the last value
    
 while(0 == 0): # do forever
   checkForQuit()
#   print "Time: %s" % time.ctime()
   time.sleep(0.25)
   for m in range(0,4): # read the channels
###    reading = bus.read_byte(chipAddress) # read A/D
       reading = random.uniform(230.0, 255.0)
###    if(abs(last_reading[m] - reading) >= 2): # we have a significant change not just noise
       draw270Meter(reading,m)
       last_reading[m] = reading # save this reading for next time
 #end of main loop

# Function definitions
def draw270Meter(needle, meter):
    V = Vref * (needle / 256.0)
    angle = (1.5 * math.pi * ((-V / 5.0))) + (1.25 * math.pi)
    volts = str.format( "{0:.2f}", V)
    mpX = 95 + meterPositionX[meter]
    mpY = 95 + meterPositionY[meter]
    screen.blit(meterSurface,[meterPositionX[meter],meterPositionY[meter]])
    dx = mpX + 86 * math.cos(angle)
    dy = mpY - 86 * math.sin(angle)
    pygame.draw.line(screen,(30,30,30),(mpX,mpY),(dx,dy),2)
    text = font.render("A"+ str(meter) + " Reading " + volts +" V", True, (0,0,0), (180,180,180) )
    textRect = text.get_rect()
    textRect.centerx = mpX
    textRect.centery = mpY + 56
    screen.blit(text, textRect)
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
	boardRevision = 2 ## assume RPi 3

LEFT=1

def checkForQuit():
    #print "checking for quit"
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
#        pygame.event.post(event) # put the other KEYUP event objects back
    for event in [pygame.event.wait()]+pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
         elif event.type == pygame.MOUSEBUTTONDOWN:
             print "You pressed the left mouse button at (%d, %d)" % event.pos
             print "event.button", event.button
#         elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
         elif event.type == pygame.MOUSEBUTTONUP:
             print "You released the left mouse button at (%d, %d)" % event.pos
             print "event.button", event.button

if __name__ == '__main__':
    main()
