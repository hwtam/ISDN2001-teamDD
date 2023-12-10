import pygame

### const ###
MAX_TIME = 10000  # -1 -> inf

### var ###
pygame.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((1280, 720))

### functions ###
def write(string, location) :
  text = font.render(str(string), True, (255, 255, 255))
  screen.blit(text, location)

##### loop #####
running = True
time = 0
speed = 1
pause = False
while running:
  # when to stop

  if  (MAX_TIME != -1) and (time > MAX_TIME) :
    break

  for event in pygame.event.get():
    # quit
    if event.type == pygame.QUIT:
      running = False

    # control the speed
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        speed /= 2
        if speed < 0.25:
          speed = 0.25
      if event.key == pygame.K_RIGHT:
        speed *= 2
        if speed > 4:
          speed = 4
      if event.key == pygame.K_SPACE:
        pause = True

  if pause :
    pygame.event.wait()
    continue

  # fill the screen with a color to wipe away anything from last frame
  screen.fill("grey")


  write(speed, (400,600))
  write(time, (400,300))
  time += 1

  # RENDER YOUR GAME HERE

  # flip() the display to put your work on screen
  pygame.display.flip()
  
  pygame.time.wait(int(200/speed))

pygame.quit()