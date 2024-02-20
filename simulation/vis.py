from elements import *
import openpyxl as xl # openpyxl
from datetime import datetime
import os

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
  try :
    os.mkdir("excel")
  except :
    pass
  wb.save(f"excel/{timestamp}.xlsx")
  wb.close()

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
    ws = wb[str(user.stop)]
    ws.cell(row = user.enqueue_time + 2, column = 4).value = user.waiting_time
  for stop in Stop.list_obj[:-1] :  # remove waiting time of all the users that are still waiting at the queue
    ws = wb[str(Stop.list_obj.index(stop))]
    for user in stop.user_list :
      ws.cell(row = user.enqueue_time + 2, column = 4).value = None