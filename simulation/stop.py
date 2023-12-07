class stop :

  l_obj = [] # a static list, storing all stop
  l_location = [] # a static list to store the times

  def __init__(self, location = -1, P_queue = 0, P_off = 0) :
    self.ppl = 0  # current amount of ppl
    self.location = location  # relative "location" of the stop at the route , how many sec needed to go to from the start(by real data)
    self.P_queue = P_queue/100  # P(how many ppl get in the queue per time)%
    self.P_off = P_off/100  # P(how many ppl get off the minibus per people in bus)%
    stop.l_obj.append(self)
    stop.l_location.append(location)