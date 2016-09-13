# External module imports
import RPi.GPIO as GPIO
import time


def encodercount(pin):
    print pin

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
GPIO.add_event_detect(aPin, GPIO.BOTH, callback = encodercount)   # Encoder A
GPIO.add_event_detect(bPin, GPIO.BOTH, callback = encodercount)   # Encoder B



print("Here we go! Press CTRL+C to exit")
try:
    while 1:
#        if GPIO.input(butPin): # button is released
#            pwm.ChangeDutyCycle(dc)
#            GPIO.output(ledPin, GPIO.LOW)
#        else: # button is pressed:
#            pwm.ChangeDutyCycle(100-dc)
#            GPIO.output(ledPin, GPIO.HIGH)
#            time.sleep(0.075)
#            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.1)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO
