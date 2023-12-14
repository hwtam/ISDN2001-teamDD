import_string = \
'''
import pygame
'''
### LINK START! (https://github.com/evnchn/linkstart.py)
for line in import_string.splitlines():
    if "import" in line:
        print(line)
        try:
            exec(line)
        except:
            if "#" in line:
                package_name = line.split("#")[-1]
            else:
                splits = line.split("import")
                if "from" in line:
                    package_name = splits[0].replace("from","")
                else:
                    package_name = splits[1]
            package_name = package_name.strip()
            print("Installing {}...".format(package_name))    
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            try:
                exec(line)
            except:
                print("Failed to install {}".format(package_name))
### DONE
import pygame
import os
import random
import minibus
import stop
import graph

### const ###
MAX_TIME = -1  # -1 -> inf
bus_cycle = 7*60

### init ###
path = os.path.dirname(__file__)
os.chdir(path)

pygame.init()
pygame.display.set_caption("ISDN 2001 Team DD Simulation")
random.seed(0)
# init the bus stop (location, P_queue, P_off)
stop.stop(0, 30, 0) # start , most ppl get in, 0 ppl get off
stop.stop(90, 10, 10) # 2
stop.stop(318, 7, 20) # 3
stop.stop(366, 5, 7) # 4
stop.stop(404, 4, 10) # 5
stop.stop(488, 3, 15) # 6
stop.stop(553, 0, 100) # end , 0 ppl get in, all ppl get off

### var ###
font_big = pygame.font.Font(None, 60)
font_small = pygame.font.Font(None, 36)
font_title = pygame.font.Font(None, 24)
font_label = pygame.font.Font(None, 15)
screen = pygame.display.set_mode((1280, 720))
bg = pygame.image.load("asset/bg.png")  # the background
play = pygame.image.load("asset/play.png")
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
  if speed > 9 :
    speed = 9

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
  bus.x.append(bus.ppl)
  s.ppl -= on
  s.change_img()
  if s.ppl == 0 :
    if s.count != 0 :
      s.count = 0
      s.image_ppl = stop.stop.img_ppl1
  else :  # still hv ppl after arrival
    s.count += 1
    if s.count == 1 :
      s.image_ppl = stop.stop.img_ppl2
    else :
      s.image_ppl = stop.stop.img_ppl3

##### loop #####
running = True
time = 0
speed = 7
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
    elif event.type == pygame.KEYDOWN :
      if event.key == pygame.K_LEFT :
        change_speed(-1)
      elif event.key == pygame.K_RIGHT :
        change_speed(1)
      # pause
      elif event.key == pygame.K_SPACE :
        pause = not pause

    # handle the buttons
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
      # move graph
      if graph.graph.show and graph.graph.rect.collidepoint(event.pos) :  # click inside the graph rect
        if graph.graph.rect_quit.collidepoint(event.pos) :  # click the quit rect
          graph.graph.show = 0
        else :
          graph.graph.is_dragging = True
          graph.graph.offset_x = event.pos[0] - graph.graph.rect.x
          graph.graph.offset_y = event.pos[1] - graph.graph.rect.y
      # change speed
      elif backward.collidepoint(event.pos) :
        change_speed(-1)
      elif middle.collidepoint(event.pos) :
        pause = not pause
      elif forward.collidepoint(event.pos) :
        change_speed(1)
      # reset
      elif reset.collidepoint(event.pos) :
        time = 0  # reset the time
        minibus.minibus.l_obj = []  # clear all minibus
        for s in stop.stop.l_obj :
          s.image_ppl = pygame.image.load("asset/stop_ppl1.png")
          s.ppl = int(s.P_queue/2)  # init all s.ppl
          s.change_img()
        pause = False  # continues
      elif minibus.minibus.rect.collidepoint(event.pos) :
        minibus.minibus.using_graph = True
        graph.graph.show = 1
    
    # move graph
    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 :
      if graph.graph.show :
        graph.graph.is_dragging = False
    elif event.type == pygame.MOUSEMOTION :
      if graph.graph.show and graph.graph.is_dragging :
        graph.graph.move(event.pos)
             
  if pause and time != 0 :
    screen.blit(play, middle)
    pygame.display.flip()
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

    # update the location of the bus rect
    index = (bus.rec.x - 83) // 170  # current stop round down
    if index == 6 :
      continue
    distance = stop.stop.l_location[index+1] - stop.stop.l_location[index]
    diff = bus.position - stop.stop.l_location[index]
    bus.rec.move_ip(int((index + diff / distance) * 170 + 83) - bus.rec.x, 0)

  for s in stop.stop.l_obj :
    # random amount of ppl get in the queue of each stop
    s.ppl += getRandom(s.P_queue)
    s.change_img()

  time += 1
  if time % speed != 0 :
    continue
  # update data on the screen
  screen.blit(bg, (0,0))
  write(speed, (1150,58), font_big)
  write(str(time).zfill(5), (60,58), font_big)
  for bus in minibus.minibus.l_obj :
    if (bus.end()) :
      continue
    screen.blit(minibus.minibus.image, bus.rec)
    write(str(bus.ppl).zfill(2), (bus.rec.x+50, bus.rec.y+8), font_small)
  
  for s in stop.stop.l_obj :
    screen.blit(s.image, (s.rec.x, s.rec.y))
    screen.blit(s.image_ppl, (s.rec.x, s.rec.y+123))
    write(str(s.ppl).zfill(2), (s.rec.x+50, s.rec.y+129), font_small)

  if graph.graph.show == 1 :
      screen.blit(graph.graph.img, graph.graph.rect)
      graph.graph.draw_bus(screen, font_title, font_label)
  elif graph.graph.show == 2 :
    screen.blit(graph.graph.img, graph.graph.rect)
    graph.graph.draw_stop(screen, font_title, font_label)

  pygame.display.flip()
  update = False
  pygame.time.wait(20 - speed)

pygame.quit()
print("\nSimulation finished")