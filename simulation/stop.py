class stop :

  l = [] # a static list, storing all stop

  def __init__(self, location = -1, P_queue = 0, P_off = 0) :
    self.ppl = 0  # current amount of ppl
    self.time_next_arrival = -1  # remainning time for the next arrival
    self.location = location  # relative "location" of the stop at the route , how many sec needed to go to from the start(by real data)
    self.P_queue = P_queue  # P(how many ppl get in the queue per time)
    self.P_off = P_off  # P(how many ppl get off the minibus per people in bus)
    stop.l.append(self)