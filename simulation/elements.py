import random

### functions ###
def getRandom(p) -> int :
  return int(random.random() < (p / 100))  # 0 / 1

def arrive(stop, bus) :
  # get off the bus first
  off = 0
  for i in range(bus.ppl) :
    off += getRandom(stop.P_off)
  bus.ppl -= off
  # get on the bus
  on = bus.capacity - bus.ppl
  if on > len(stop.user_list) :
    on = len(stop.user_list)
  bus.ppl += on
  s.ppl -= on

### classes ###
class bus :  # simplify "minibus" to "bus" for all the comments

  list_obj = [] # static list to store all minibus

  def __init__(self, capacity = 19) :
    self.ppl = 0  # how many ppl inside the bus
    self.position = 0  # current position of the bus
    self.capacity = capacity
    bus.list_obj.append(self)

  def end(self) -> bool:
    return (self.position == -1)  # postion = -1 to indicate the minibus arrived the ending of the route
  
class stop :

  list_obj = [] # a static list storing all stop
  list_location = [] # a static list to store the times
  P_leave = 0 # P(a person leave the queue without getting on the bus)

  def __init__(self, location = -1, P_queue = 0, P_off = 0) :
    self.location = location  # relative "location" of the stop at the route , how many sec needed to go to from the start(by real data)
    self.P_queue = P_queue/10  # P(how many ppl get in the queue per time)/1000
    self.P_off = P_off  # P(how many ppl get off the minibus per people in bus)/100
    self.user_list = []  # a list to store the people waiting at the queue
    for i in range(int(P_queue/2)) :  # init value of people waiting
      self.user_list.append(user(len(stop.list_obj), 0))
    stop.list_obj.append(self)
    stop.list_location.append(location)

    def enqueue(self, t) -> int :  # enqueue with given P
      if (getRandom(self.P_queue)) :
        self.user_list.append(user(len(stop.list_obj), t))
        return 1
      return 0
    
    def renege(self) -> int :  # dequeue without getting on the bus
      count = 0
      if (stop.P_leave > 0) :
        for person in self.user_list :
          if (getRandom(stop.P_leave)) :
            count += 1
            dequeue(person)
      return count
    
    def dequeue(self, person = None) -> None :  # dequeue
      if (person == None) :
        person = self.user_list[0]  # remove the first person if not specified
      self.user_list.pop(person)

    def update_waiting_time(self) -> None :
      for user in self.user_list :
        user.waiting_time += 1

      


class user :

  list_obj = []  # to store all users (include "got off the bus", "on the bus", "waiting the bus", "renege")

  def __init__(self, stop, t) :
    self.stop = stop  # belongs to which bus stop, the index of the stop
    self.enqueue_time = t
    self.waiting_time = 0
