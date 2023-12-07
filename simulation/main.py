import minibus
import stop
import random


### const ###
MAX_TIME = 10000
bus_cycle = 5*60

### init ###
# make the bus stop (location, P_queue, P_off)
stop.stop(0, 15, 0) # start , most ppl get in, 0 ppl get off
stop.stop(90, 5, 15) # 2
stop.stop(318, 5, 35) # 3
stop.stop(366, 5, 5) # 4
stop.stop(404, 5, 10) # 5
stop.stop(488, 5, 25) # 6
stop.stop(553, 0, 100) # end , 0 ppl get in, all ppl get off

### functions ###
def getRandom(p) -> int:
  return int(random.random() < p)

def arrive(stop, bus) :
  # get off the bus first
  off = 0
  for i in range(bus.ppl) :
    off += getRandom(stop.P_off)  # off = (int) bus.ppl*stop.P_off
  bus.ppl -= off
  # get on the bus
  on = bus.capacity - bus.ppl
  if on > stop.ppl :
    on = stop.ppl
  bus.ppl += on
  stop.ppl -= on

def in_queue(stop) :
  stop.ppl += getRandom(stop.P_queue)

##### main #####
for time in range(MAX_TIME) :
  # check if any bus at the bus stop
  for bus in minibus.minibus.l_obj :
    if (bus.end()) :
      continue  # skip if the minibus is not on the road
    if bus.position in stop.stop.l_location :  # if the minibus arrive the stop
      i = minibus.minibus.l_obj.index(bus)
      arrive(stop.stop.l_obj[i], bus)
      