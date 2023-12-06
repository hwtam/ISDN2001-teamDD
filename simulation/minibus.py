class minibus :

  l = [] # static list to store all minibus

  def __init__(self, capacity = 19) :
    self.ppl = 0
    self.capacity = capacity
    minibus.l.append(self)