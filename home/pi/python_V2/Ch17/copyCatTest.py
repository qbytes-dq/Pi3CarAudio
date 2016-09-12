#!/usr/bin/python
# run by sudo python copyCat.py

import RPi.GPIO as GPIO
from time import sleep

leds = [14, 15, 18, 23]
buttons = [24, 25, 8, 7]
words = ["red", "green", "yellow", "blue" ]
print"hi from pi - Copy Cat Hardware test"
print"press teh buttons to turn the LEDs off"
GPIO.setmode(GPIO.BCM)  # use real GPIO numbering
GPIO.setwarnings(False) # to remove spurious warnings on re running code
for pin in leds:
   GPIO.setup(pin, GPIO.OUT)
for pin in buttons:
   GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True: # loop forever
   for position in range(0,4): # look at each button in turn
      if GPIO.input(buttons[position]) == 0 : # if button pressed
         GPIO.output(leds[position], 0) #turn off LED
      else:
         GPIO.output(leds[position], 1) #turn on LED
 
