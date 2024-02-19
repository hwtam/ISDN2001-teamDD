import_string = \
'''

import openpyxl as xl # openpyxl
'''
### LINK START! (https://github.com/evnchn/linkstart.py)
for line in import_string.splitlines():
    if "import" in line:
        print(line)
        try:
            exec(line)
        except:
            if "#" in line:
                package_name = line.split("#")[-1]
            else:
                splits = line.split("import")
                if "from" in line:
                    package_name = splits[0].replace("from","")
                else:
                    package_name = splits[1]
            package_name = package_name.strip()
            print("Installing {}...".format(package_name))    
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            try:
                exec(line)
            except:
                print("Failed to install {}".format(package_name))
### DONE
from elements import *  # self-define
import vis  # self-define
import os
import subprocess
import openpyxl as xl # openpyxl

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
  vis.vis_excel(ws, time)

# after simulation
ws.column_dimensions['A'].width = 5.5
for cell in ws["B1:O1"][0]:
  if cell.value :
    ws.column_dimensions[cell.column_letter].width = 18
  else :
    ws.column_dimensions[cell.column_letter].width = 8.5

# loops until can save
while True:
  try:
    wb.save("visualization_time.xlsx")
  except:
    print("\nPlease close the excel the file")
    input()
    continue
  break  

wb.close()
try :
  subprocess.run("visualization_time.xlsx", shell=True, timeout=1, stderr=subprocess.DEVNULL)
except TimeoutError :  # stop the program after 5s 
  pass
print("\nSimulation finished")