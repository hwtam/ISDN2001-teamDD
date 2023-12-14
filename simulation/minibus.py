import pygame
import os

path = os.path.dirname(__file__)
os.chdir(path)

class minibus :  # simplify "minibus" to "bus"
  
  l_obj = [] # static list to store all minibus
  using_graph = False  # the graph of minibus is static
  rect = pygame.Rect(83, 270, 1115, 155)  # as a button to toggle the static graph for minibus
  
  image = pygame.image.load("asset/bus.png")

  def __init__(self, capacity = 19) :
    self.ppl = 0  # how maany ppl inside the bus
    self.position = 0  # current position of the bus
    self.capacity = capacity
    self.rec = pygame.Rect(83, 270, 100, 173)
    self.x = []
    minibus.l_obj.append(self)

  def end(self) -> bool :
    return (self.position == -1)  # postion = -1 to indicate the minibus arrived the ending of the route