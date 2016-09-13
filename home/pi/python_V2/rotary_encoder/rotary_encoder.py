# External module imports
import RPi.GPIO as GPIO
import time

val=0

# Pin Definitons:
cPin = 16
aPin = 20
bPin = 21

def encoderswitch(pin):
    print "switch", pin

def encodercount(pin):
    global val
    
##    dir=GPIO.input(bPin)

    if GPIO.input(bPin)==0:
      dir="U"
      if val<20:
        val+=1
      #print "inc"
    else:
      dir="D"
      if val>0:
        val-=1
      #print "dec"

    print dir, val

# Pin Definitons:
#cPin = 16 
#aPin = 20
#bPin = 21

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(cPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 
GPIO.setup(aPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(bPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #

# Initialize the interrupts - these trigger on the both the rising and falling 
GPIO.add_event_detect(cPin, GPIO.FALLING, callback = encoderswitch, bouncetime=5)   # Encoder A
GPIO.add_event_detect(aPin, GPIO.RISING, callback = encodercount, bouncetime=5)   # Encoder A
#GPIO.add_event_detect(aPin, GPIO.BOTH, callback = encodercount)   # Encoder A
#GPIO.add_event_detect(bPin, GPIO.BOTH, callback = encodercount)   # Encoder B

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        time.sleep(0.01)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.remove_event_detect(aPin) # remove event
    GPIO.remove_event_detect(cPin) # remove event
    GPIO.cleanup() # cleanup all GPIO
     
