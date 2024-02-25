import random

### const ###
BUS_CYCLE = 7*60
MAX_TIME = 3000

### functions ###
def getRandom(p) -> int :
  return int(random.random() < (p / 100))  # 0 / 1

def loop(t) :
  for stop in Stop.list_obj :  # handle the queue
    stop.renege()
    stop.enqueue(t)

  for bus in Bus.list_obj :  # handle buses
    if (bus.end()) :
      continue
    elif (bus.position == 0) :  # waiting for start
      bus.get_on(Stop.list_obj[0])  # direct get on the bus
      if (t % BUS_CYCLE == 0) or (bus.ppl == bus.capacity) :  # if full or next bus arrive
        bus.position = 1  # start moving
        bus.ppl_list.append(bus.ppl)
        Stop.list_obj[0].leave_time_list.append(t)
        Stop.list_obj[0].update_waiting_num_bus()
      continue
    elif bus.position in Stop.list_location[1:] :  # if bus at bus stop
      i = Stop.list_location.index(bus.position)
      bus.get_off(Stop.list_obj[i])
      bus.get_on(Stop.list_obj[i])
      bus.ppl_list.append(bus.ppl)
      Stop.list_obj[i].leave_time_list.append(t)
      Stop.list_obj[i].update_waiting_num_bus()

    bus.position += 1  # move, for every bus
    if bus.position > Stop.list_location[-1] :  # after arrive last stop
      bus.position = -1
  
  if (t % BUS_CYCLE == 0) :  # start a new bus for each bus_cycle
    Bus()
  for stop in Stop.list_obj :
    stop.update_waiting_time()  # waiting time ++

### classes ###
class Bus :  # simplify "minibus" to "bus"

  list_obj = [] # static list to store all minibus

  def __init__(self, capacity = 19) :
    self.ppl = 0  # how many ppl inside the bus
    self.position = 0  # current position of the bus
    self.capacity = capacity
    self.ppl_list = []  # store the amount of ppl in the bus after the bus leave the stop
    Bus.list_obj.append(self)

  def get_on(self, stop) -> int:
    on = self.capacity - self.ppl
    if on > len(stop.user_list) :
      on = len(stop.user_list)
    self.ppl += on
    for i in range(on) :
      stop.dequeue()
    stop.current_on = on
    return on

  def get_off(self, stop) -> int :
    off = 0
    for i in range(self.ppl) :
      off += getRandom(stop.P_off)
    self.ppl -= off
    stop.leave_ppl_list.append(off)
    return off

  def end(self) -> bool:
    return (self.position == -1)  # postion = -1 to indicate the minibus arrived the ending of the route
  
class Stop :

  list_obj = [] # a static list storing all stop
  list_location = [] # a static list to store the times
  P_leave = 0 # P(a person leave the queue without getting on the bus)

  def __init__(self, location = -1, P_queue = 0, P_off = 0) :
    self.location = location  # relative "location" of the stop at the route , how many sec needed to go to from the start(by real data)
    self.P_queue = P_queue/10  # P(how many ppl get in the queue per time)/1000
    self.P_off = P_off  # P(how many ppl get off the minibus per people in bus)/100
    self.user_list = []  # a list to store the people waiting at the queue
    self.leave_time_list = []  # list to store the time when a bus leave the stop
    self.leave_ppl_list = []  # list to store the amount of ppl when a bus leave the stop
    self.current_on = 0  # amount of people getting on the bus
    Stop.list_obj.append(self)
    Stop.list_location.append(location)

  def enqueue(self, t) -> int :  # enqueue with given P
    if (getRandom(self.P_queue)) :
      self.user_list.append(User(Stop.list_obj.index(self), t))
      return 1
    return 0
  
  def renege(self) -> int :  # dequeue without getting on the bus
    count = 0
    if (Stop.P_leave > 0) :
      for person in self.user_list :
        if (getRandom(Stop.P_leave)) :
          count += 1
          self.dequeue(person)
    return count
  
  def dequeue(self, person = None) -> None :  # dequeue
    if (person == None) :
      self.user_list.pop(0)  # remove the first person if not specified
      return
    self.user_list.remove(person)
    User.list_obj.remove(person)  # remove the person from the system

  def update_waiting_time(self) -> None :
    for user in self.user_list :
      user.waiting_time += 1

  def update_waiting_num_bus(self) -> None :
    for user in self.user_list :
      user.waiting_num_bus += 1

class User :

  list_obj = []  # to store all users (include "got off the bus", "on the bus", "waiting the bus", "renege")

  def __init__(self, stop, t) :
    self.stop = stop  # belongs to which bus stop, the index of the stop
    self.enqueue_time = t
    self.waiting_time = 0
    self.waiting_num_bus = 1  # 1 = able to get on the next bus
    User.list_obj.append(self)