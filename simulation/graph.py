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
    x = location[0] + graph.rect.x - text.get_width()/2
    y = location[1] + graph.rect.y - text.get_height()/2
    screen.blit(text, (x, y))

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
  def draw_stop(screen, font_title, font_label) :
    stop_x = numpy.linspace(35, 405, 10)
    stop_xx = numpy.linspace(35, 405, 100)
    stop_y = numpy.linspace(210, 50, 26)  # max is 25
    for s in stop.stop.l_obj :
      if s.using_graph :
        ind = stop.stop.l_obj.index(s)
        break
    graph.write(screen, f"Historical   data   of   {s.name[ind]}", (225, 25), font_title, (00, 129, 251))
    for i in range(10) :
      graph.line(screen, (stop_x[i], 205), (stop_x[i], 215))
      try :
        graph.write(screen, stop.stop.times[i*10], (stop_x[i], 220), font_label, (0, 0, 0))
      except :
        pass
    for i in range(26) :
      if i % 5 == 0 :
        if (i != 0) :
          graph.write(screen, i, (20, stop_y[i]), font_label, (0, 0, 0))
        graph.line(screen, (28, stop_y[i]), (44, stop_y[i]))
    
    points = []
    i = 0
    for y in stop.stop.l_obj[ind].y :
      if y > 25 :
         y = 25
      points.append((stop_xx[i] + graph.rect.x, stop_y[y] + graph.rect.y))
      i += 1
    if len(points) > 1 :
        pygame.draw.lines(screen, "black", False, points, 3)
       

  @staticmethod
  def draw_bus(screen, font_title, font_label) :  # update when arrive
    bus_y = numpy.linspace(210, 50, 20)
    bus_x = numpy.linspace(35, 405, 7)
    # draw axises
    graph.write(screen, "Historical   data   of   last   5   minibuses", (225, 25), font_title, (00, 129, 251))
    for i in range(7) :
      if i % 2 == 0 :
        graph.line(screen, (bus_x[i], 205), (bus_x[i], 215))
        graph.write(screen, stop.stop.name[i], (bus_x[i], 223), font_label, (0, 0, 0))
      else :
         graph.line(screen, (bus_x[i], 205), (bus_x[i], 225))
         graph.write(screen, stop.stop.name[i], (bus_x[i], 236), font_label, (0, 0, 0))
    for i in range(20) :
      if (i == 19) or (i % 5 == 0) :
        if (i != 0) :
          graph.write(screen, i, (20, bus_y[i]), font_label, (0, 0, 0))
        graph.line(screen, (28, bus_y[i]), (44, bus_y[i]))
      else :
         graph.line(screen, (32, bus_y[i]), (40, bus_y[i]))

    # draw lines
    for bus in minibus.minibus.l_obj[-5:] :
      if bus.end() :
        color = "black"
      else :
        color = (220,58,58)
      points = []
      i = 0
      for y in bus.y :
        points.append((bus_x[i] + graph.rect.x, bus_y[y] + graph.rect.y))
        i += 1
      if len(points) > 1 :
        pygame.draw.lines(screen, color, False, points, 5)