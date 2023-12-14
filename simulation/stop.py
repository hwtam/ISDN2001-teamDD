import pygame

class stop :

  l_obj = [] # a static list, storing all stop
  l_location = [] # a static list to store the times
  name = ["HKUST", "Clear Water Bay Road", "Shui Pin Tsuen", "Boon Kin Village", "Po Ning Road", "CHUNG WA ROAD", "Hang Hau Station"]

  img_stop0 = pygame.image.load("asset/stop0.png")
  img_stop1 = pygame.image.load("asset/stop1.png")
  img_stop2 = pygame.image.load("asset/stop2.png")
  img_stop3 = pygame.image.load("asset/stop3.png")
  img_ppl1 = pygame.image.load("asset/stop_ppl1.png")
  img_ppl2 = pygame.image.load("asset/stop_ppl2.png")
  img_ppl3 = pygame.image.load("asset/stop_ppl3.png")

  def __init__(self, location = -1, P_queue = 0, P_off = 0) :
    self.ppl = int(P_queue/2)  # current amount of ppl
    self.location = location  # relative "location" of the stop at the route
    self.P_queue = P_queue/1000  # P(how many ppl get in the queue per time)/1000
    self.P_off = P_off/100  # P(how many ppl get off the minibus per people in bus)/100
    self.count = 0  # how many time the minibus arrival cant clear the stop
    self.rec = pygame.Rect(80 + len(stop.l_obj)*170, 425, 100, 157)  # also act as a button to toggle the graph
    self.image = stop.img_stop0
    self.image_ppl = stop.img_ppl1
    self.using_graph = False
    stop.l_obj.append(self)
    stop.l_location.append(location)

  def change_img(self) :
    if self.ppl < 2 :
      self.image = stop.img_stop0
    elif self.ppl < 5 :
      self.image = stop.img_stop1
    elif self.ppl < 10 :
      self.image = stop.img_stop2
    else :
      self.image = stop.img_stop3
