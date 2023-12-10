import minibus
import stop
import random
import os

### const ###
MAX_TIME = 1000
bus_cycle = 5*60

### init ###
path = os.path.dirname(__file__)
os.chdir(path)
try :
  os.remove("output.txt")
except :
  pass

# make the bus stop (location, P_queue, P_off)
stop.stop(0, 20, 0) # start , most ppl get in, 0 ppl get off
stop.stop(90, 15, 20) # 2
stop.stop(318, 10, 40) # 3
stop.stop(366, 10, 5) # 4
stop.stop(404, 7.5, 10) # 5
stop.stop(488, 5, 30) # 6
stop.stop(553, 0, 100) # end , 0 ppl get in, all ppl get off

### functions ###
def getRandom(p) -> int:
  return int(random.random() < p)

def arrive(s, bus, t) :
  with open("output.txt", 'a') as f :
    index_bus = minibus.minibus.l_obj.index(bus)
    index_s = stop.stop.l_obj.index(s)
    f.write(f"##### Arrive at {t} #####\n")
    f.write(f"--- Minibus {index_bus} arrives stop {index_s} ---\n")
    # get off the bus first
    f.write(f"\tMinibus {index_bus} : {bus.ppl} -> ")
    off = 0
    for i in range(bus.ppl) :
      off += getRandom(s.P_off)  # off = (int) bus.ppl*s.P_off
    bus.ppl -= off
    # get on the bus
    on = bus.capacity - bus.ppl
    if on > s.ppl :
      on = s.ppl
    bus.ppl += on
    f.write(f"{bus.ppl} (-{off})(+{on})\n\tStop {index_s} : {s.ppl} -> ")
    s.ppl -= on
    f.write(f"{s.ppl} (-{on})\n\n\n")

def vis_time(t) :
  with open("output.txt", 'a') as f :
    f.write(f"##### Time = {t} : #####\n")

    f.write("--- minibus ---\n")
    for bus in minibus.minibus.l_obj :  # print minibuses
      if (bus.end()) :
        continue
      i = minibus.minibus.l_obj.index(bus)
      f.write(f"\tminibus {i} ({bus.position}) : {bus.ppl}\n")

    f.write("--- minibus stop ---\n")
    i = 1
    for s in stop.stop.l_obj :
      f.write(f"\tstop {i} ({s.location}) : {s.ppl}\n")
      i += 1
    f.write(f"\n\n")

##### main #####
for time in range(MAX_TIME + 1) :
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
      i = stop.stop.l_location.index(bus.position)
      arrive(stop.stop.l_obj[i], bus, time)

    bus.position += 1
    # the minibus ends after it arrived the last stop
    if bus.position > stop.stop.l_location[-1] :
      bus.position = -1

  # random amount of ppl get in the queue of each stop
  for s in stop.stop.l_obj :
    s.ppl += getRandom(s.P_queue)

  if (time % 30 == 0) :  # update every 30 sec
    vis_time(time)

print("\nSimulation finished")