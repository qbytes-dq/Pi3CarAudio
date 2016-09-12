#!/usr/bin/env python
#GPIO input monitor on the Raspberry Pi

import os, pygame, sys
from pygame.locals import *
import RPi.GPIO as GPIO

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("GPIO monitor")
boardRevision =  GPIO.RPI_REVISION
if boardRevision ==3:
   screen = pygame.display.set_mode([500,282],0,32)  
else:     
   screen = pygame.display.set_mode([400,282],0,32)
pinSurface = pygame.Surface((500,282))
pygame.event.set_allowed(None)
pygame.event.set_allowed([pygame.KEYDOWN,pygame.QUIT,pygame.MOUSEBUTTONDOWN])
picture = True
if boardRevision == 3:
     pinPicture = pygame.image.load("images/Gpio3.jpg").convert_alpha()
else:
     pinPicture = pygame.image.load("images/Gpio.jpg").convert_alpha()
pinSurface.blit(pinPicture,[0,0])

font = pygame.font.Font(None, 28)
# positions of pins on the picture
if boardRevision == 3:
   pinx = [45,58,73,88,103,118,134,150,165,178,196,210,225,241,255,270,286,302,317,333]
   piny = [100, 84]
   boxX = [ (box * 24) - 18 for box in range (1,21)]
else:     
   pinx = [99, 113, 127, 142, 157, 172, 185, 200, 214, 228, 243, 258, 272]
   piny = [92, 77]
   boxX = [ (box * 24) - 18 for box in range (1,14)]
 #calculate box positions

boxCol = (160,60,0)

def main():
 boardRevision =  GPIO.RPI_REVISION
 ways = 26
 totPins = 17
 #define the pins to use
 if boardRevision == 1:
     inputs = [0,1,4,17,21,22,10,9,11,14,15,18,23,24,25,8,7]
 if boardRevision == 2:    
     inputs = [2,3,4,17,27,22,10,9,11,14,15,18,23,24,25,8,7]
 if boardRevision == 3:    
     inputs = [2,3,4,17,27,22,10,9,11,14,15,18,23,24,25,8,7,0,1,5,6,12,13,19,16,26,20,21] 
     ways = 40
     totPins = 28
     
 print "Display the GPIO input pin states"
 print "Escape to stop"
 # use real GPIO numbering
 GPIO.setmode(GPIO.BCM)
 if boardRevision == 3:
     pinouts = [3,5,7,11,13,15,19,21,23,8,10,12,16,18,22,24,26,27,28,29,31,32,33,35,36,37,38,40] # position of pins
 else:     
     pinouts = [3,5,7,11,13,15,19,21,23,8,10,12,16,18,22,24,26] # position of pins
 
 inputState = [ 5 for temp in range (0,29)] # blank array for input levels
 for pin in range(0,totPins):
     GPIO.setup(inputs[pin],GPIO.IN, pull_up_down=GPIO.PUD_UP)
 # draw the background screen
 screen.blit(pinSurface,[0,0])
 text = font.render("Board Revision " + str(boardRevision), True, (0,0,0), (220,220,220) )
 textRect = text.get_rect()
 textRect.topleft = 14, 200
 screen.blit(text, textRect)
 text = font.render("Reading all input pins ", True, (0,0,0), (220,220,220) )
 textRect = text.get_rect()
 textRect.topleft = 14, 230
 screen.blit(text, textRect)

 for pin in range(1,ways+1):
     if (pin & 1) == 1: # if it is an odd number
        pygame.draw.line(screen,boxCol,(boxX[(pin-1)/2] , 38),(pinx[(pin-1)/2],piny[1]),2)
        pygame.draw.rect(screen,(180,180,180), (boxX[(pin-1)/2], 12, 20,26), 0)
        pygame.draw.rect(screen,boxCol, (boxX[(pin-1)/2], 12, 20,26), 1)
     else:
        pygame.draw.line(screen,boxCol,(boxX[(pin-1)/2] , 170),(pinx[(pin-1)/2],piny[0]),2)
        pygame.draw.rect(screen,(180,180,180), (boxX[(pin-1)/2], 170, 20,26), 0)
        pygame.draw.rect(screen,boxCol, (boxX[(pin-1)/2], 170, 20,26), 1)
 pygame.display.update()

 # Display fixed pins
 showLogicState("3", 1) # logic state, pin number
 showLogicState("3", 17)
 showLogicState("5", 2)
 showLogicState("5", 4)
 showLogicState("G", 6)
 showLogicState("G", 9)
 showLogicState("G", 25)
 showLogicState("G", 14)
 showLogicState("G", 20)
 if boardRevision==3:
    showLogicState("G", 30)
    showLogicState("G", 34)
    showLogicState("G", 39)
            
 while True: # do forever
   checkForEvent() # see if we have a quit event
   for check in range(0,totPins):
     checkForEvent()   
     if(GPIO.input(inputs[check])):
        latestState = 1
     else:
        latestState = 0
     if(latestState != inputState[check]):
         showLogicState(str(latestState),pinouts[check])
         inputState[check] = latestState
 #end of main loop

# Function definitions
def showLogicState(state, pin):
    textCol = (0,0,0) # default black
    if state == "0":
       textCol = (0,0,230)
    if state == "1":
       textCol = (230,0,0)
    text = font.render(state, True, textCol, (180,180,180) )
    textRect = text.get_rect()
    textRect.topleft = boxX[(pin-1)/2] + 4, 14 + 158 * (pin & 1)
    screen.blit(text, textRect)
    pygame.display.update()

def terminate():
    print "Closing down please wait"
    pygame.quit()
    sys.exit()
    
def checkForEvent():
    #print "checking for quit"
     event = pygame.event.poll()
     if event.type == pygame.QUIT:
          terminate()
     if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
               terminate()               
     if event.type == pygame.MOUSEBUTTONDOWN:
          print pygame.mouse.get_pos()
          
if __name__ == '__main__':
    main()
