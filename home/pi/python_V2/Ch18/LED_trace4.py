#Plot the voltage across the LED against the current through it.
#For three analogue input channels
from smbus import SMBus
import os, sys, pygame
from time import sleep
from pygame.locals import *
boardRevision = -1
pygame.init()
font = pygame.font.Font(None, 24)
YaxisX = [0, 7, 286, 562]
yaxis = [font.render("^", True, (0,0,0), (255,255,255) ),font.render("|", True, (0,0,0), (255,255,255) ),font.render("I", True, (0,0,0), (255,255,255) )]
XaxisX = [0, 140, 416, 692]
                       
def main():
 os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
 pygame.display.set_caption("Voltage vs Current")
 screen = pygame.display.set_mode([828,286],0,32)
 findRevision()
 if boardRevision == 1 : bus = SMBus(0)
 if boardRevision == 2 : bus = SMBus(1)

 print("Ctrl C to stop")
 address = 74
 control = 1<<6 | 1 << 2 # enable analogue output & auto increment
 Xoff = [0, 22, 298, 574] # plotting X offset
 Yoff = 264 # plotting Y offset
 last_reading = [0,0,0,0]
 reading = [0,0,0,0]
 plotCol = [ (128,128,0), (0, 0, 128), (0,128,0), (128, 0, 0) ]
 Vref = 4.44
 bufOffset = int((256.0 / Vref) * 0.7)


 while(True): # do forever
   drawAxis(screen)
   for p in range (0,4):       
       last_reading[p] = 0
   for x in range (0, 256):
      bus.write_word_data(address, control, x | x<<8) # output to D/A
      dum = bus.read_byte(address) # read A/D to trigger next reading
      for p in range(0,4): # read all 4 inputs
         reading[p] = bus.read_byte(address)
      checkForQuit()
      for p in range(1,4): # plot A1 to A3
         i = ((x- bufOffset) - reading[p]) # current reading
         if i<0: # compensate for lower part of ramp
             i=0
         # scale factors
         i = i * 2 

         pygame.draw.line(screen,plotCol[p],(reading[p]+Xoff[p],Yoff-last_reading[p]),(reading[p]+Xoff[p],Yoff-i),2)
         last_reading[p] = i # save this reading for next time
      pygame.display.update()
      
   sleep(3) # hold graph to see it

#end of main loop


# Function definitions
def drawAxis(screen):
    screen.fill((255,255,255)) # blank white screen
    pygame.draw.line(screen,(0,0,0),(10,266),(276,266),2)
    pygame.draw.line(screen,(0,0,0),(286,266),(542,266),2)
    pygame.draw.line(screen,(0,0,0),(552,266),(808,266),2)

    pygame.draw.line(screen,(0,0,0),(20,10),(20,276),2)
    pygame.draw.line(screen,(0,0,0),(296,10),(296,276),2)
    pygame.draw.line(screen,(0,0,0),(572,10),(572,276),2)

    text = font.render("V -->", True, (0,0,0), (255,255,255) )
    textRect = text.get_rect()
    for a in range (1,4):
         textRect.centerx = XaxisX[a]
         textRect.centery = 278
         screen.blit(text, textRect)

    for ch in range (1,4):
        ttext = font.render("Channel "+str(ch), True, (0,0,0), (255,255,255) )
        ttextRect = ttext.get_rect()
        ttextRect.centerx = XaxisX[ch]
        ttextRect.centery = 24
        screen.blit(ttext, ttextRect)

    for a in range (1,4):
       for c in range (0,3):
         textRect1 = yaxis[c].get_rect()    
         textRect1.centerx = YaxisX[a]
         textRect1.centery = 128 + c*14
         screen.blit(yaxis[c], textRect1)
 
    pygame.display.update()
    
def terminate():
    print "Closing down please wait"
    pygame.quit()
    sys.exit()

def findRevision():
    global boardRevision
    fin = open('/proc/cpuinfo')
    boardRevision = -1
    while True: # go through the file line by line
       line = fin.readline()
       if not line: break # end if reached the end of the file
       if "Revision" in line:
         rev = line[11:15]
         if rev == "0002" or rev == "0003" :
           boardRevision = 1
         if rev == "0004" or rev == "0005" or rev == "0006" :
           boardRevision = 2
    fin.close()
    if boardRevision == -1:
        print "Error can't recognise board revision ", rev
        terminate()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key

if __name__ == '__main__':
    main()
