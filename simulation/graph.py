import_string = \
'''
import pygame
import numpy
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
import numpy
import minibus
import stop

class graph :

  # static memeber, such that there is only 1 graph on screen
  img = pygame.image.load("asset/graph.png")
  rect = img.get_rect()
  rect.topleft = (415, 235)
  is_dragging = False
  offset_x = 0
  offset_y = 0
  show = 0  # 0 = no show, 1 = showing minibus, 2 = showing stop
  rect_quit = pygame.Rect(rect.x + 410, rect.y + 10, 30, 25)
  l_y = numpy.linspace(210, 50, 20)
  l_x = numpy.linspace(35, 405, 7)

  def __init__(self) -> None:
    pass  # should not construct any instance

  @staticmethod
  def move(pos) :
    graph.rect.x = pos[0] - graph.offset_x
    graph.rect.y = pos[1] - graph.offset_y
    if graph.rect.x < 0 :
      graph.rect.x = 0
    if graph.rect.y < 0 :
      graph.rect.y = 0
    if graph.rect.x + graph.rect.w > 1280 :
      graph.rect.x = 1280 - graph.rect.w
    if graph.rect.y + graph.rect.h > 720 :
      graph.rect.y = 720 - graph.rect.h
    graph.rect_quit.update(graph.rect.x + 410, graph.rect.y + 10, 30, 25)

  @staticmethod
  def write(screen, string, location, f, color = (255, 255, 255)) :  # to print string on the screen
    text = f.render(str(string), True, color)
    screen.blit(text, (location[0] + graph.rect.x, location[1] + graph.rect.y))

  def line(screen, start, end, color = "black", w = 1) :
    pygame.draw.line(screen, color, (start[0] + graph.rect.x, start[1] + graph.rect.y),
                     (end[0] + graph.rect.x, end[1] + graph.rect.y), w)

  @staticmethod
  def quit() :
    graph.show = False
    minibus.minibus.using_graph = False
    for s in stop.stop.l_obj :
      s.using_graph = False

  @staticmethod
  def draw_stop(screen, s, font_title, font_label) :
    pass

  @staticmethod
  def draw_bus(screen, font_title, font_label, font_even_smaller) :  # update when arrive

    # draw axises
    l = numpy.linspace(35, 405, 7)
    for i in range(7) :
      graph.line(screen, (l[i], 205), (l[i], 215))
      if i % 2 == 0 :
        graph.write(screen, stop.stop.name[i], (l[i]-32, 218), font_even_smaller, (0, 0, 0))
      else :
         graph.write(screen, stop.stop.name[i], (l[i]-32, 228), font_even_smaller, (0, 0, 0))
    l = numpy.linspace(210, 50, 20)
    for i in range(20) :
      if (i == 19) or (i % 5 == 0) :
        graph.write(screen, str(i).zfill(2), (18, l[i]-4), font_label, (0, 0, 0))
        graph.line(screen, (31, l[i]), (41, l[i]))
      else :
         graph.line(screen, (33, l[i]), (39, l[i]))
         
    

    # draw lines
    # for bus in minibus.minibus.l_obj[:-5] :
    #   if bus.end() :
    #     color = "black"
    #   points = []
    #   for x in bus.x :