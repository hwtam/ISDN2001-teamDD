import minibus
import stop
import vis
import random
import os
import openpyxl as xl


### const ###
MAX_TIME = 1000
bus_cycle = 7*60

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

### init ###
path = os.path.dirname(__file__)
os.chdir(path)

# make the bus stop (location, P_queue, P_off)
stop.stop(0, 20, 0) # start , most ppl get in, 0 ppl get off
stop.stop(90, 15, 20) # 2
stop.stop(318, 10, 40) # 3
stop.stop(366, 10, 5) # 4
stop.stop(404, 7.5, 10) # 5
stop.stop(488, 5, 30) # 6
stop.stop(553, 0, 100) # end , 0 ppl get in, all ppl get off

# init excel
wb = xl.Workbook()
ws = wb.active
l = ["Time",
     "HKUST (North Station)", "",
     "Clear Water Bay Road", "",
     "Shui Pin Tsuen", "",
     "Boon Kin Village", "",
     "Po Ning Road", "",
     "CHUNG WA ROAD", "",
     "Hang Hau Station"]  # https://gmb.hk/en/route/NT/11M/2
wb.active.append(l)

### simulation ###
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
      arrive(stop.stop.l_obj[i], bus)

    bus.position += 1
    # the minibus ends after it arrived the last stop
    if bus.position > stop.stop.l_location[-1] :
      bus.position = -1

  # random amount of ppl get in the queue of each stop
  for s in stop.stop.l_obj :
    s.ppl += getRandom(s.P_queue)

  #### data visualization ####
  #vis.vis_excel(wb.active, time)

# after simulation
ws.column_dimensions['A'].width = 7
for cell in ws["B1:O1"][0]:
  if cell.value :
    ws.column_dimensions[cell.column_letter].width = 18
  else :
    ws.column_dimensions[cell.column_letter].width = 6


wb.save("visualization_time.xlsx")
wb.close()
print("Simulation finished")