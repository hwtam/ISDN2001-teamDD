from elements import *
import openpyxl as xl # openpyxl
from datetime import datetime
import subprocess

### const ###

### functions ###

def add_header(ws) :
  ws.append(["time", "people at queue", "people get on the bus", "waiting time"])

def con_excel() :
  wb = xl.Workbook()
  ws = wb.active
  ws.title = "0"
  add_header(ws)
  for i in range(1, len(Stop.list_location)-1) :
    ws = wb.create_sheet(str(i))
    add_header(ws)
  return wb

def des_excel(wb) :
  timestamp = datetime.now().strftime("%m%d-%H%M%S")
  wb.save(f"excel/{timestamp}.xlsx")
  wb.close()
  try :
    subprocess.run("visualization_time.xlsx", shell=True, timeout=1, stderr=subprocess.DEVNULL)
  except TimeoutError :  # stop the program after 5s 
    pass

def to_excel_ppl(wb, t) :  # add data to excel
  for stop in Stop.list_obj[:-1] :
    ws = wb[str(Stop.list_obj.index(stop))]
    row = [t, len(stop.user_list)]
    if (stop.current_on != 0) :
      row.append(stop.current_on)
    ws.append(row)
    stop.current_on = 0

def to_excel_waiting(wb) :
  for user in User.list_obj :
    ws = wb[str(Stop.list_obj.index(user.stop))]
