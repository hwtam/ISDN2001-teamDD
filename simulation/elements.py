import random

### functions ###
def getRandom(p) -> int :
  return int(random.random() < (p / 100))

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
      self.user_list.append(user(0, True))
    stop.list_obj.append(self)
    stop.list_location.append(location)

    def enqueue(self, t, bool) -> int :  # enqueue with given P
      num = getRandom(self.P_queue)
      for i in range(num) :
        self.user_list.append(user(t, bool))
      return num
    
    def dequeue_leave(self) -> int :  # dequeue without getting on the bus, quit by no reason
      count = 0
      if (stop.P_leave > 0) :
        for person in self.user_list :
          if (getRandom(stop.P_leave)) :
            count += 1
            self.user_list.pop(person)
      return count
    
    def dequeue_bus(self, num) -> int :  # dequeue due to bus arrival
      count = 0
      


class user :

  def __init__(self, t) :
    self.enqueue_time = t
    self.waiting_time = 0
