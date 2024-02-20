from elements import *
import openpyxl as xl # openpyxl
from datetime import datetime
import os
import matplotlib.pyplot as plt # matplotlib

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

def plt_waiting_time() :
  fig, axes = plt.subplots(3, 2)
  axes = axes.flatten()

  for stop in Stop.list_obj[:-1] :
    index = Stop.list_obj.index(stop)
    x = []
    y = []
    for user in User.list_obj :
      if (user.stop != index) :
        continue # only search for the current stop
      if user not in stop.user_list :  # if not queueing
        x.append(user.enqueue_time)
        y.append(user.waiting_time)
    axes[index].scatter(x, y, s=10)
    axes[index].set_xlabel('time')
    axes[index].set_ylabel('waiting time')
    axes[index].set_title(index)
    axes[index].set_xlim(0, MAX_TIME+1)

  plt.tight_layout()
  plt.show()
