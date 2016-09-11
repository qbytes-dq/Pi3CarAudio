#!/usr/bin/env python
# Pot Reich - a Steve Reich like composer
# For potentiometers
#A0 controls the speed - continuously variable
#A1 controls the number of repeated bars 1 to 4
#A2 controls the mutation rate 0 to 4 changes in a bar
#A3 controls the stop / go - lower than half to stop above that to go

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
pygame.display.set_caption("Reich Machine")
screen = pygame.display.set_mode([200,148],0,32)
barCol = [ (0, 128, 0), (180, 180, 0), (50, 50, 180), (128, 0, 0) ]


def main():
 address = 74
 findRevision()
 if boardRevision == 1 : bus = SMBus(0)
 if boardRevision == 2 : bus = SMBus(1)

 print "Loading sound files"
 seqLength = 8
 tone = [ pygame.mixer.Sound("sounds/"+str(s)+".ogg") for s in range(0,8)]
 seq1 = [ random.randint(0,7) for c in range(0,seqLength) ]
 lable()

 
 cont = [0,128,128,128]
 bus.write_byte(address, 4) # set control register to auto increment
 temp = bus.read_byte(address)

 print "Hi from Python :- Steve Reich machine"
    
 while True: # run the game forever
   for rep in range (0,1 + cont[1]/64): # bars to repeat
      checkForQuit() 
      for s in range (0,8): # play each note in the sequence
        for c in range (0,4): # read in all the controls
            temp = bus.read_byte(address)
            if abs(temp - cont[c]) >1:
               cont[c] = temp
               drawControls(c,temp)
        if cont[3]>127: # do not play notes if not running
          tone[seq1[s]].play()
        sleep(cont[0]/512.0)
   if cont[3] > 127: # skip mutate if not running  
      for mutate in range(0,cont[2]/64): 
         seq1[random.randint(0,7)] = random.randint(0,7)
      print seq1
 # end of main loop
 
# Function definitions
def lable():
    font = pygame.font.Font(None, 16)
    text = font.render("Speed", True, (255,255,255), (0,0,0) )
    textRect = text.get_rect()
    textRect.centerx = 20
    textRect.centery = 135
    screen.blit(text, textRect)
    
    text = font.render("Repeat", True, (255,255,255), (0,0,0) )
    textRect = text.get_rect()
    textRect.centerx = 70
    textRect.centery = 135
    screen.blit(text, textRect)
    
    text = font.render("Mutate", True, (255,255,255), (0,0,0) )
    textRect = text.get_rect()
    textRect.centerx = 120
    textRect.centery = 135
    screen.blit(text, textRect)

    text = font.render("Stop/Go", True, (255,255,255), (0,0,0) )
    textRect = text.get_rect()
    textRect.centerx = 170
    textRect.centery = 135
    screen.blit(text, textRect)


def drawControls(number,value):
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
