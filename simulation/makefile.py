from elements import *  # self-define
import os
from datetime import datetime
import numpy as np
import pandas as pd

if (__name__ == "__main__") :
  path = os.path.dirname(__file__)
  os.chdir(path)

### global var ###
timestamp = datetime.now().strftime("%m%d-%H%M%S")
stops = []
buses = []

def init() -> None :
  os.makedirs(f"asset/{timestamp}", exist_ok=True)

def save() -> None :
  columns = ["time"] + list(range(len(Stop.list_obj[:-1])))
  df = pd.DataFrame(stops, columns = columns)
  df.to_csv(f"asset/{timestamp}/stop.csv", index=False)

def append_queue(t) -> None :  # append a new row to store the queue at time t
  arr = [len(stop.user_list) for stop in Stop.list_obj[:-1]]
  arr.insert(0, t)
  stops.append(arr)

def append_bus(t) :  # append a new row to store the bus at time t when bus arrive the stop
  pass