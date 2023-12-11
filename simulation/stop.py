import pygame

class stop :

  l_obj = [] # a static list, storing all stop
  l_location = [] # a static list to store the times

  def __init__(self, location = -1, P_queue = 0, P_off = 0) :
    self.ppl = int(P_queue/2)  # current amount of ppl
    self.location = location  # relative "location" of the stop at the route
    self.P_queue = P_queue/1000  # P(how many ppl get in the queue per time)/1000
    self.P_off = P_off/100  # P(how many ppl get off the minibus per people in bus)/100
    self.count = 0  # how many time the minibus arrival cant clear the stop
    self.rec = pygame.Rect(80 + len(stop.l_obj)*170, 425, 100, 157)
    self.image = pygame.image.load("asset/stop1.png")
    stop.l_obj.append(self)
    stop.l_location.append(location)


