import os
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
pic = pygame.image.load("images/MeterV270.png")
pic = pygame.transform.scale(pic,(100,100))
screen.blit(pygame.transform.scale(pic, (100, 100)), (0, 0))
pygame.display.flip()
while True:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.display.quit()
    elif event.type == VIDEORESIZE:
        screen = pygame.display.set_mode(
            event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
        pygame.display.flip()
