#!/usr/bin/python

import struct
import binhex

# You'll need to find the name of your particular mouse to put in here...
#file = open("/dev/input/by-id/usb-Logitech_USB_Trackball-event-mouse","rb")
file = open( "/dev/input/by-id/usb-WWW.PowerMCU.COM_Multi_Media_Development_Board_V1.0_6D8514984957e-event-mouse","rb")


while True:


    byte = file.read(16)
#    h = ":".join("{:02x}".format(ord(c)) for c in byte)
#    print "byte=",h

    (type,code,value) =  struct.unpack_from('hhi', byte, offset=8)

    if type == 1 and value == 1:
        if code == 272:
            print "LEFT PRESS", value
        if code == 273:
            print "RIGHT PRESS", value

    if type == 2:
        if code == 0:
            print "MOVE L/R",value
        if code == 1:
            print "MOVE U/D",value

