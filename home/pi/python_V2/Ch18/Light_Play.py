#!/usr/bin/env python
# Light play - play music from light sensors

import pygame, os, sys
from pygame.locals import *
from time import sleep
import random
from smbus import SMBus

pygame.init()
pygame.mixer.quit()
pygame.mixer.init()
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Light Play")
screen = pygame.display.set_mode([200,148],0,32)
barCol = [ (0, 128, 0), (180, 180, 0), (50, 50, 180), (128, 0, 0) ]

def main():
 address = 74
 findRevision()
 if boardRevision == 1 : bus = SMBus(0)
 if boardRevision == 2 : bus = SMBus(1)

 print "Loading sound files"
 tone = [ pygame.mixer.Sound("sounds/"+str(s)+".ogg") for s in range(0,4)]
 lable() # lable the window
 
 cont = [0,128,128,128] # initial values
 bus.write_byte(address, 4) # set control register to auto increment
 temp = bus.read_byte(address)

 print "Hi from Python :- LDR light play"
 # define the thresholds
 threshold = 64 # note play threshold value
 sensitivity = [1.5,2,2,2] # value to multiply each of the readings by
    
 while True: # run the game forever
    checkForQuit() 
    for c in range (0,4): # read in all the controls
        temp = int(sensitivity[c] * bus.read_byte(address))
        if abs(temp - cont[c]) >2:
            if temp > threshold and cont[c] <= threshold:
               tone[c].play() 
            cont[c] = temp
            drawControls(c,temp)
            
 # end of main loop
 
# Function definitions
def lable():
    font = pygame.font.Font(None, 16)
    text = font.render("Doh", True, (255,255,255), (0,0,0) )
    textRect = text.get_rect()
    textRect.centerx = 20
    textRect.centery = 135
    screen.blit(text, textRect)
    
    text = font.render("Ray", True, (255,255,255), (0,0,0) )
    textRect = text.get_rect()
    textRect.centerx = 70
    textRect.centery = 135
    screen.blit(text, textRect)
    
    text = font.render("Me", True, (255,255,255), (0,0,0) )
    textRect = text.get_rect()
    textRect.centerx = 120
    textRect.centery = 135
    screen.blit(text, textRect)

    text = font.render("Far", True, (255,255,255), (0,0,0) )
    textRect = text.get_rect()
    textRect.centerx = 170
    textRect.centery = 135
    screen.blit(text, textRect)


def drawControls(number,value):
    if value > 255:
        value = 255
    x = 22 + (number *50)
    pygame.draw.line(screen,barCol[value/64], (x,128),(x,128-(value/2)),40)
    pygame.draw.line(screen,(0,0,0),(x,128-(value/2)),(x, 0),40)
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
        terminate()


def checkForQuit():
    #print "checking for quit"
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key

if __name__ == '__main__':
    main()
