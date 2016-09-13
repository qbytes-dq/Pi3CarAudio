##-->> https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
# http://computationalphoto.mlog.taik.fi/2011/01/31/a-quick-webcam-application-using-pygame/
# https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/

# import the relevant libraries
import time
import pygame
import pygame.camera
from pygame.locals import *

### DRAW
import sys

red      = (255,0,0)
yellow   = (255,255,0)
green    = (0,255,0)
blue     = (0,0,255)
darkBlue = (0,0,128)
white    = (255,255,255)
black    = (0,0,0)
pink     = (255,200,200)

# this is where one sets how long the script
# sleeps for, between frames.sleeptime__in_seconds = 0.05
# initialise the display window
#screen = pygame.display.set_mode([800,420])
screen = pygame.display.set_mode([800,640])

pygame.init()
pygame.camera.init()

# set up a camera object
cam = pygame.camera.Camera("/dev/video0",(640,480))
# start the camera
cam.start()

def drawZones(x, y, width, height, screen):

    lineThickness = 5
    step = height / 3
    # red zone
    points = [(x,y)        
             ,(x,         y + height)
             ,(x + width ,y + height)
             ,(x + width ,y)
             ]
    pygame.draw.lines(screen, red, False, points, lineThickness)
    # yellow zone
    height = height - step
    points = [(x,y)
             ,(x,         y + height)
             ,(x + width ,y + height)
             ,(x + width ,y)
             ]
    pygame.draw.lines(screen, yellow, False, points, lineThickness)

    # green zone
    height = height - 150
    points = [(x,y)
             ,(x,         y + height)
             ,(x + width ,y + height)
             ,(x + width ,y)
             ]
    pygame.draw.lines(screen, green, False, points, lineThickness)


def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((2/3.0) * height)),
              (x,y), (x+width,y), 
              (x+width,y-(2/3.0) * height),
              (x,y- ((2/3.0) * height)), 
              (x + width/2.0,y-height), 
              (x+width,y-(2/3.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)
#
#
#   pygame.draw.line(screen, (0, 0, 255), (0, 0), (200, 100))
#   pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))

#    pygame.draw.rect ( screen, blue, pygame.Rect(90, 90, 190, 190))

while 1:

    # sleep between every frame
#    time.sleep( sleeptime__in_seconds )
    time.sleep(0.1)
####################################################
    # fetch the camera image
    image = cam.get_image()
#    drawHouse(150,150,100,100,image,red)
    drawZones(100,0,440,380,image)

####################################################
    ### DRAW
    #pygame.draw.lines(image, red, closed, pointlist, thickness)
    # blank out the screen
#    screen.fill([0,0,0])

####################################################
    # copy the camera image to the screen
    screen.blit( image, ( 100, 0 ) )
    # update the screen to show the latest screen image
    pygame.display.update()
