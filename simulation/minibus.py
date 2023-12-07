class minibus :  # simplify "minibus" to "bus" for all the comments

  l_obj = [] # static list to store all minibus

  def __init__(self, capacity = 19) :
    self.ppl = 0  # how maany ppl inside the bus
    self.position = 0  # current position of the bus
    self.capacity = capacity
    minibus.l_obj.append(self)

  def end(self) -> bool:
    return (self.position == -1)  # postion = -1 to indicate the minibus arrived the ending of the route