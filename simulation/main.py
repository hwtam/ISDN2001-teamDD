import minibus
import stop
import random
import os

### const ###
MAX_TIME = 10000
bus_cycle = 5*60

### init ###
path = os.path.dirname(__file__)
try :
  os.remove("output.txt")
except :
  pass

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

def arrive(s, bus) :
  # get off the bus first
  off = 0
  for i in range(bus.ppl) :
    off += getRandom(s.P_off)  # off = (int) bus.ppl*s.P_off
  bus.ppl -= off
  # get on the bus
  on = bus.capacity - bus.ppl
  if on > s.ppl :
    on = s.ppl
  bus.ppl += on
  s.ppl -= on

def vis(t) :
  with open("output.txt", 'a') as f :
    f.write(f"time =\t{t}s :\n")

    f.write("--- minibus ---\n")
    for bus in minibus.minibus.l_obj :  # print minibuses
      if (bus.end()) :
        continue
      i = minibus.minibus.l_obj.index(bus)
      f.write(f"minibus\t{i} : \n")
      f.write(f"\tlocation : {bus.location}\n")
      f.write(f"\tamount of people : {bus.ppl}\n\n")

    f.write("--- minibus stop ---")
    i = 1
    for s in stop.stop.l_obj :
      f.write(f"stop\t{i}({s.location}) : \n")
      f.write(f"\tamount of people : {s.ppl}\n\n")
    
    f.write("###############")
      

##### main #####
for time in range(MAX_TIME) :
  # start a new bus for each bus_cycle
  if (time % bus_cycle) == 0 :
    minibus.minibus()

  # check if any bus at the bus stop
  for bus in minibus.minibus.l_obj :
    # skip if the minibus is not on the road
    if (bus.end()) :
      continue  
    
    # if the minibus arrive the stop
    if bus.position in stop.stop.l_location :  
      i = minibus.minibus.l_obj.index(bus)
      arrive(stop.stop.l_obj[i], bus)

    bus.position += 1
    # the minibus ends after it arrived the last stop
    if bus.position > stop.stop.l_location[-1] :
      bus.position = -1

  # random amount of ppl get in the queue of each stop
  for s in stop.stop.l_obj :
    s.ppl += getRandom(s.P_queue)
      