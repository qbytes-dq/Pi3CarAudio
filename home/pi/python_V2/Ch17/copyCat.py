#!/usr/bin/python
# run by sudo python copyCat.py

import RPi.GPIO as GPIO
from time import sleep
import random
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.quit()
pygame.mixer.init()

def getPress():
   pressed = False
   while pressed == False:
    for test in range(0,4):
      if GPIO.input(buttons[test]) == False: # button held down
         GPIO.output(leds[test],17)
         effect[test].play()
         pressed = True
         sleep(0.05) # debounce delay
         while GPIO.input(buttons[test]) == False: #hold until button released
            sleep(0.05)
         GPIO.output(leds[test],0)
         return test
         
def saySeq(length):
   for number in range(0,length):
      effect[sequence[number]].play()
      GPIO.output(leds[sequence[number]],1) # turn LED on      
      sleep(1.2)
      GPIO.output(leds[sequence[number]],0) # turn LED off
      sleep(0.5)

def getSeq(length):
    goSound.play()
    print"Now you try"
    for press in range(0,length):
       attempt = getPress()
       #uncomment next line to show what you are pressing
       #print"key press ", colours[attempt], "looking for",colours[sequence[press]]
       #note the game is too easy with the above line
       if attempt != sequence[press]:
          sleep(0.8)
          return -1
    return 1
   
colours = ["red", "green", "yellow", "blue" ]
# colours = ["blue","red", "green", "yellow"] # uncomment for a hard game
print "Loading sound files"
effect = [ pygame.mixer.Sound("sounds/"+colours[c]+".ogg") for c in range(0,4)]
goSound = pygame.mixer.Sound("sounds/go.ogg")
dohSound = pygame.mixer.Sound("sounds/doh.ogg")
maxLength = 35
sequence = [ random.randint(0,3) for c in range(0,maxLength)] 

leds = [14, 15, 18, 23]
buttons = [24, 25, 8, 7]

print"hi from Pi - Copy Cat, you coppy the sequence"
print"Ctrl C to quit"
GPIO.setmode(GPIO.BCM)  # use real GPIO numbering
GPIO.setwarnings(False) # to remove spurious warnings on re running code
for pin in leds:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, 0) # turn LEDs off
for pin in buttons:
   GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
maxFails = 3

daq=False

while (True): #repeat forever
  sleep(1.0)
  if daq == False:
     daq = True
#     pygame.mixer.set_volume(1.0)
#     vol = pygame.mixer.get_volume()
#     print "volume:", vol
     sleep(0.5)
     dohSound.play()
     sleep(1.0)
     dohSound.play() 
     sleep(1.0)
     goSound.play()
     sleep(1.0)
     effect[0].play()
     sleep(1.0)
     effect[1].play()
     sleep(1.0)
     effect[2].play()
     sleep(1.0)
     effect[3].play()
     print"play sounds"
  fail = 0  # number of fails
  #generate new sequence
  for c in range(0,maxLength):
     sequence[c] = random.randint(0,3)
  far = 2
  while fail < maxFails: # number of fail attempts before reset
     print"a sequence of",far
     saySeq(far)
     if getSeq(far) != -1:   
        far = far + 1
        print"Yes - now try a longer one"
        fail = 0 # reset number of fails
     else:
         fail = fail +1
         print"Wrong",fail,"fail"
         if fail < maxFails:
            dohSound.play()
            print"try that one again"
     sleep(1.5)
     if far > maxLength:
        print"Well done Master Mind"
        exit() # suspect a cheat

  dohSound.play()
  print"Game over - Your score is",far-1
  print"Try again"
  sleep(2.0)
