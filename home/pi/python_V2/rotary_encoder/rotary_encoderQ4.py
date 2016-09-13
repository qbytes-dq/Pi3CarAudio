# External module imports
import RPi.GPIO as GPIO
import time

val=0

def encodercount(pin):
    global val

    dir=GPIO.input(bPin)

    if dir==0:
      if val<10:
        val+=1
      #print "inc"
    else:
      if val>0:
        val-=1
      #print "dec"

    print dir, val


# Pin Definitons:
cPin = 16 
aPin = 20
bPin = 21

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(cPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(aPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(bPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # p

# Initialize the interrupts - these trigger on the both the rising and falling 
GPIO.add_event_detect(aPin, GPIO.RISING, callback = encodercount, bouncetime=100)   # Encoder A
#GPIO.add_event_detect(aPin, GPIO.BOTH, callback = encodercount)   # Encoder A
#GPIO.add_event_detect(bPin, GPIO.BOTH, callback = encodercount)   # Encoder B

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        time.sleep(0.01)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
