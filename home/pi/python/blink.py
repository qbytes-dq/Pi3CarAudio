#!/user/bin/env python
# Blink led on pin 4 and input test on pin 17
#

try:

 import RPi.GPIO as GPIO
 import time

 pinOut = 0
 pinIn  = 17

 GPIO.setmode(GPIO.BCM)
 GPIO.setup(pinOut, GPIO.OUT)
 GPIO.setup(pinIn, GPIO.IN)
 while True:
        GPIO.output(pinOut,True)
        time.sleep(0.1)
        GPIO.output(pinOut,False)
        time.sleep(0.1)
        input_value = GPIO.input(pinIn)
        print "Pin Out : ",pinOut, " Button ",pinIn, " : ", input_value
        if (input_value == True):
                pinOut = pinOut + 1
                if (pinOut > 27):
                        pinOut = 0
        if (pinOut == 14):
                pinOut=16
        if (pinOut == pinIn):
                pinOut = pinOut+1
        if (pinOut != pinIn):
                GPIO.setup(pinOut, GPIO.OUT)

except KeyboardInterrupt:
	GPIO.cleanup()
