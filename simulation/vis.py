from elements import *
import openpyxl as xl # openpyxl
from datetime import datetime

### const ###

### functions ###

def add_header(ws) :
  ws.append(["time", "people at queue", "people get on the bus", "waiting time"])

def con_excel() :
  wb = xl.Workbook()
  ws = wb.active
  ws.title = "0"
  add_header(ws)
  for i in range(1, len(Stop.list_location)) :
    ws = wb.create_sheet(str(i))
    add_header(ws)
  return wb

def des_excel(wb) :
  timestamp = datetime.now().strftime("%m%d-%H%M%S")
  while True:
    try:
      wb.save(f"excel/x{timestamp}.xlsx")
    except:
      print("\nPlease close the excel the file")
      input()
      continue
    break  
  wb.close()

def to_excel_ppl(wb, t) :  # add data to excel
  for stop in Stop.list_obj :
    ws = wb[str(Stop.list_obj.index(stop))]
    ws.append([t, len(stop.user_list), stop.current_on])
    stop.current_on = 0

def to_excel_waiting(wb) :
  for user in User.list_obj :
    ws = wb[str(Stop.list_obj.index(user.stop))]
    