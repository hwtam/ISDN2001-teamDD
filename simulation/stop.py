class stop :

  l = [] # a static list, storing all stop

  def __init__(self, location = -1, P_queue = 0, P_off = 0) :
    self.ppl = 0
    self.time_next_arrival = -1
    self.location = location
    self.P_queue = P_queue
    self.P_off = P_off
    stop.l.append(self)