import pygame
import os
import random
import subprocess
import minibus
import stop

### const ###
MAX_TIME = 3000  # -1 -> inf
DELAY_TIME = [160, 80, 40, 20, 0]  # speed -1 = index , value = delay
bus_cycle = 7*60

### init ###
path = os.path.dirname(__file__)
os.chdir(path)

pygame.init()

# init the bus stop (location, P_queue, P_off)
stop.stop(0, 20, 0) # start , most ppl get in, 0 ppl get off
stop.stop(90, 15, 20) # 2
stop.stop(318, 10, 40) # 3
stop.stop(366, 10, 5) # 4
stop.stop(404, 7.5, 10) # 5
stop.stop(488, 5, 30) # 6
stop.stop(553, 0, 100) # end , 0 ppl get in, all ppl get off

### var ###
font_big = pygame.font.Font(None, 60)
font_small = pygame.font.Font(None, 16)
screen = pygame.display.set_mode((1280, 720))
bg = pygame.image.load("asset/bg.png")  # the background
backward = pygame.Rect(505, 75, 59, 43)
middle = pygame.Rect(575, 75, 129, 43)
forward = pygame.Rect(717, 75, 59, 43)
reset = pygame.Rect(862, 75, 60.63, 43)

### functions ###
def write(string, location, f) :  # to print string on the screen
  text = f.render(str(string), True, (255, 255, 255))
  screen.blit(text, location)

def change_speed(value):
  global speed
  speed += value
  if speed < 1 :
    speed = 1
  if speed > 5 :
    speed = 5

def getRandom(p) -> int :
  return int(random.random() < p)

def arrive(s, bus) :
  # get off the bus first
  off = 0
  for i in range(bus.ppl) :
    off += getRandom(s.P_off)  # off = (int) bus.ppl*s.P_off
  bus.ppl -= off
  # get on the bus
  on = bus.capacity - bus.ppl
  if on > s.ppl :
    on = s.ppl
  bus.ppl += on
  s.ppl -= on

##### loop #####
running = True
time = 0
speed = 3
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
        change_speed(-1)
      if event.key == pygame.K_RIGHT :
        change_speed(1)
      # pause
      if event.key == pygame.K_SPACE :
        pause = not pause

    # handle the buttons
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      mouse_pos = event.pos
      if backward.collidepoint(mouse_pos) :
        change_speed(-1)
      if middle.collidepoint(mouse_pos) :
        pause = not pause
      if forward.collidepoint(mouse_pos) :
        change_speed(1)
      if reset.collidepoint(mouse_pos) :
        time = 0  # reset the time
        minibus.minibus.l_obj = []  # clear all minibus
        for s in stop.stop.l_obj :
          s.ppl = int(s.P_queue/2)  # init all s.ppl
        pause = True  # continues
        
        
  if pause :
    continue

  ##### simulation #####
  # new a bus every cycle
  if (time % bus_cycle) == 0 :
    minibus.minibus()

  for bus in minibus.minibus.l_obj :
    # skip if the minibus is not on the road
    if (bus.end()) :
      continue  
    
    # if the minibus arrive the stop
    if bus.position in stop.stop.l_location :  
      i = stop.stop.l_location.index(bus.position)
      arrive(stop.stop.l_obj[i], bus)

    bus.position += 1
    # the minibus ends after it arrived the last stop
    if bus.position > stop.stop.l_location[-1] :
      bus.position = -1

    pre = 0
    for l in stop.stop.l_location[1:] :
      if bus.position in range(pre, l) :
        if (l - pre) % 170

  for s in stop.stop.l_obj :
    # random amount of ppl get in the queue of each stop
    s.ppl += getRandom(s.P_queue)
    


  # update the screen
  screen.blit(bg, (0,0))
  write(speed, (1150,58), font_big)
  write(str(time).zfill(5), (60,58), font_big)

  time += 1
  pygame.display.flip()
  pygame.time.wait(DELAY_TIME[speed-1])


pygame.quit()