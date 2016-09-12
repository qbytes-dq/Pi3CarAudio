#!/usr/bin/env python
# Blast off marble game - python 2
# with sound effects
# run with - sudo python BlastOff.py
 

import RPi.GPIO as GPIO
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.quit()
pygame.mixer.init()

def checkContacts(pins):
    made = -1 # number of the contact made
    for test in range (0,7):
       if(GPIO.input(pins[test]) == False): # if contact is made
           made = test
    return made

print "Loading sound files"
effect = [ pygame.mixer.Sound("sounds/"+str(s)+".ogg") for s in range(0,6)]
abortSound = pygame.mixer.Sound("sounds/abort.ogg")
countWords = ["BLAST OFF", "ONE", "TWO", "THREE", "FOUR", "FIVE"]

print "Hi from Python :- Blast Off game"
print "start the count from five"
print "control-C to quit"
GPIO.setmode(GPIO.BCM)  # use real GPIO numbering
boardRevision =  GPIO.RPI_REVISION
if boardRevision == 1:
    inputs = [9, 10, 22, 21, 17, 4, 11]
if boardRevision > 1:
    inputs = [9, 10, 22, 27, 17, 4, 11]
# set up GPIO input pins with pull ups enabled
for pin in inputs:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
nextCount = 5 # the next trigger to hit
while True: # run the game forever
     newState = checkContacts(inputs)
     # check if something is making contact and it is not the last pad
     if newState != -1 and newState != nextCount +1: 
        if newState == 6 and nextCount !=5: # the abort bar touched during countdown
            print "Technical difficulty -- countdown aborted"
            print "Recommence at five"
            abortSound.play()
            nextCount = 5
            
        if newState == nextCount:  # the next pad is reached
           print countWords[nextCount]
           effect[nextCount].play()
           nextCount = nextCount -1
           counting = True
        else:
            if nextCount != 5:  # the wrong pad is reached
               print "Count down out of sequence -- countdown aborted"
               print "Start again at 5"
               abortSound.play()
               nextCount = 5
        if nextCount == -1: # successfully finished count down so reset game
            nextCount = 5     
 # end of main loop
