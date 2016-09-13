import RPi.GPIO as GPIO
#print GPIO.VERSION

#setup GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

#setup GPIO using Board numbering
#   GPIO.setmode(GPIO.BOARD)

GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if (GPIO.input(20) ==1):
        print ("button 20 pressed")
    if (GPIO.input(21) ==1):
        print ("button 21 pressed")
    GPIO.cleanup()
