import pygame
import os

### init ###
pygame.init()
path = os.path.dirname(__file__)
os.chdir(path)

### const ###
MAX_TIME = 10000  # -1 -> inf

### var ###
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((1280, 720))
# obj
bg = pygame.image.load("asset/bg.png")  # the background

### functions ###
def write(string, location) :
  text = font.render(str(string), True, (255, 255, 255))
  screen.blit(text, location)

##### loop #####
running = True
time = 0
speed = 1
pause = False
while running :
  # when to stop

  if  (MAX_TIME != -1) and (time > MAX_TIME) :
    break

  for event in pygame.event.get() :

    # quit
    if event.type == pygame.QUIT :
      running = False

    # control the speed
    if event.type == pygame.KEYDOWN :
      if event.key == pygame.K_LEFT :
        speed /= 2
      if event.key == pygame.K_RIGHT :
        speed *= 2
      if event.key == pygame.K_SPACE :
        pause = not pause

    if event.type == pygame.MOUSEBUTTONUP :
      pause = False



  if pause :
    continue

  # fill the screen with a color to wipe away anything from last frame
  screen.blit(bg, (0,0))


  write(speed, (400,600))
  write(time, (400,300))
  time += 1

  # RENDER YOUR GAME HERE

  # flip() the display to put your work on screen
  pygame.display.flip()
  
  pygame.time.wait(int(200/speed))

pygame.quit()