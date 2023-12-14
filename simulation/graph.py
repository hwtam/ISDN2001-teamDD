import pygame
import minibus
import stop

class graph :

  # static memeber, such that there is only 1 graph on screen
  img = pygame.image.load("asset/graph.png")
  rect = img.get_rect()
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
  def write(screen, string, location, f) :  # to print string on the screen
    text = f.render(str(string), True, (255, 255, 255))
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
  def draw_stop(screen, s) :
    pass

  @staticmethod
  def draw_bus(screen) :

    # draw axises
    for i in range(7) :
      graph.line(screen, (45 + i*60, 205), (45 + i*60, 215))
    

    # draw lines
    # for bus in minibus.minibus.l_obj[:-5] :
    #   if bus.end() :
    #     color = "black"
    #   points = []
    #   for x in bus.x :