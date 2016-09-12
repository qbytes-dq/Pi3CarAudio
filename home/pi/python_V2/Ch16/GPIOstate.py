#!/usr/bin/env python
#GPIO input state monitor on the Raspberry Pi
#GPIO state - show the state of all the GPIO inputs on P1
#non GPIO pins shown as x

import RPi.GPIO as GPIO

print "Display the GPIO input pin states"
print "Ctrl C to stop"

boardRevision =  GPIO.RPI_REVISION
print"Board revision ", boardRevision
ways = 26
 #define the pins to use
if boardRevision == 1:
     pinout = [-1,-1,0,-1,1,-1,4,14,-1,15,17,18,21,-1,22,23,-1,24,10,-1,9,25,11,8,-1,7]
if boardRevision == 2:    
     pinout = [-1,-1,2,-1,3,-1,4,14,-1,15,17,18,27,-1,22,23,-1,24,10,-1,9,25,11,8,-1,7] 

if boardRevision == 3:    
     pinout = [-1,-1,2,-1,3,-1,4,14,-1,15,17,18,27,-1,22,23,-1,24,10,-1,9,25,11,8,-1,7,0,1,5,-1,6,12,13,-1,19,16,26,20,-1,21] 
     ways = 40
GPIO.setmode(GPIO.BCM) # use real GPIO numbering
inputState = [ 5 for temp in range (0,ways)] # blank array for input levels

for pin in range(0,ways): # set all pins to inputs
  if pinout[pin] != -1:
     GPIO.setup(pinout[pin],GPIO.IN, pull_up_down=GPIO.PUD_UP)
     # replace line above with the line below to see the effect of floating inputs
     # GPIO.setup(pinout[pin],GPIO.IN, pull_up_down=GPIO.PUD_OFF) 
 
while True: # do forever
   needUpdate = False
   for check in range(0,ways): # look at each input in turn
     if pinout[check] != -1:
       if(GPIO.input(pinout[check])):
          latestState = 1
       else:
          latestState = 0
       if(latestState != inputState[check]):
           needUpdate = True
           print "GPIO ", pinout[check], "changed to a logic", latestState
           inputState[check] = latestState
   if needUpdate: # display all pin states
     print "Current state"
     for row in range(1,-1, -1):
        for show in range(row,ways,2) :
          if inputState[show] != 5:
            print inputState[show],
          else:  
            print "x",
        print " "
     
 #end of main loop


