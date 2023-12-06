class stop :

  ppl = 0
  time_next_arrival = -1
  location = -1
  P_queue = 0
  P_off = 0

  def __init__(self, location = -1, P_queue = 0, P_off = 0) :
    self.location = location
    self.P_queue = P_queue
    self.P_off = P_off