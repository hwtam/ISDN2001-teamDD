import pygame

class minibus :  # simplify "minibus" to "bus"

  w = 100
  h = 173
  
  l_obj = [] # static list to store all minibus

  def __init__(self, capacity = 19) :
    self.ppl = 0  # how maany ppl inside the bus
    self.position = 0  # current position of the bus
    self.capacity = capacity
    self.y = 270
    self.x = 83
    self.image = pygame.image.load("asset/bus.png")
    minibus.l_obj.append(self)

  def end(self) -> bool :
    return (self.position == -1)  # postion = -1 to indicate the minibus arrived the ending of the route