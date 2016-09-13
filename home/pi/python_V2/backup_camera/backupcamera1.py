# http://code.activestate.com/recipes/521884-play-sound-files-with-pygame-in-a-cross-platform-m/

import pygame
import pygame.camera


BLACK  = (0,0,0)
GREEN  = (0,255,0)
YELLOW = (255,255,0)
RED    = (255,0,0)

pygame.init() #initialize pygame
lcd = pygame.display.set_mode() #Initialize a screen
pygame.mouse.set_visible(True) #Don't display the mouse
lcd.fill(BLACK) #Set background color for the screen
pygame.display.update() #Actually display it

pygame.camera.init() #Initialize the camera

size = (640, 480) #Size of the camera on the screen

camera = pygame.camera.Camera('/dev/video0', size, 'RGB') #Load a camera

camera.start() #start capturing

textSize = pygame.font.Font(None, 35) #set text size
surface = pygame.Surface(size) #Images as object

while True:
 lcd.fill(BLACK)
 camera.get_image(surface) #Captures image as surface
 lcd.blit(surface, (0,0)) #Project camera image above everything else

 distance = 5.0 
 x = 0
 y = 440
 width = 640
 height = 480

#Just the rectangle changes color
if (distance >= 2):
 #Display the text
 text = textSize.render('%.1fft'%distance,True, BLACK)#Set Text
 rect = text.get_rect(center = (350,460)) #Center the text with the Rectangle
 pygame.draw.rect(lcd, GREEN, (x,y,width,height), 0) #Draw the rectangle
 lcd.blit(text,rect) #Project the text ontop of the

 pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
 pygame.mixer.music.load("/home/pi/Desktop/Projects/GreenSound.ogg")
 pygame.mixer.music.play(0)

 pygame.display.update()
