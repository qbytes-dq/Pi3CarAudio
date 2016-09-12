import sys, pygame
from pygame.locals import *

import pygame.mixer

if __name__=="__main__":
    pygame.display.set_mode((120, 120), DOUBLEBUF | HWSURFACE)

    pygame.init()

    try:
        filename = sys.argv[1]
#        if filename == '':
#           filename = './sounds/go.ogg'
        pygame.mixer.init()
        sound = pygame.mixer.Sound(filename)
        print 'Press ESC to quit, any other key retriggers sound'
        sound.play()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    else:
                        sound.play()

    except IndexError:
        print 'Usage tplay.py filename'
