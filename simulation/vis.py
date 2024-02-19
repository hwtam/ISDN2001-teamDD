from elements import *
import openpyxl as xl # openpyxl
from datetime import datetime

### const ###

### functions ###
# def vis_excel(ws, t) :  # add a row
#   l = [t]
#   # the amount of ppl at each stop
#   for s in stop.stop.l_obj :
#     l.append(s.ppl)
#     l.append("")
#   # the amount of ppl at the bus
#   for bus in minibus.minibus.l_obj :
#     if (bus.end()) :
#       continue
#     index = 2  # "C"
#     for location in stop.stop.l_location[1:] :
#       if bus.position < location :
#         break
#       index += 2
#     l[index] = f"Bus{minibus.minibus.l_obj.index(bus)+1}: " + str(bus.ppl)
#   ws.append(l)

def add_header(ws) :
  ws.append(["time", "people at queue", "people get on the bus", "waiting time"])

def con_excel() :
  wb = xl.Workbook()
  ws = wb.active
  ws.title = 0
  add_header(ws)
  for i in range(1, len(Stop.list_location)) :
    ws = wb.create_sheet(i)
    add_header(ws)
  return wb

def des_excel(wb) :
  timestamp = datetime.now().strftime("%m%d-%H%M%S")
  while True:
    try:
      wb.save(f"{timestamp}.xlsx")
    except:
      print("\nPlease close the excel the file")
      input()
      continue
    break  
  wb.close()

def to_excel_ppl(wb, t) :  # add data to excel
  for stop in Stop.list_obj :
    ws = wb[Stop.list_obj.index(stop)]
    ws.append([t, len(stop.user_list), stop.current_on])
    stop.current_on = 0