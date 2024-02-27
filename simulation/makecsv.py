from elements import *
import os
from datetime import datetime
import numpy as np
import pandas as pd

path = os.path.dirname(__file__)
os.chdir(path)
timestamp = datetime.now().strftime("%m%d-%H%M%S")
stops = []

def init() -> None :
  try :
    os.mkdir("csv")
  except :
    pass

  try :
    os.mkdir(f"csv/{timestamp}")
  except :
    pass

def save() -> None :
  columns = ["time"] + list(range(len(Stop.list_obj[:-1])))
  df = pd.DataFrame(stops, columns = columns)
  df.to_csv(f"csv/{timestamp}/stop.csv", index=False)

def append_queue(t) -> None :  # append a new row to store the queue at time t
  arr = [len(stop.user_list) for stop in Stop.list_obj[:-1]]
  arr.insert(0, t)
  stops.append(arr)

def append_bus(t) :
  pass