from elements import *  # self-define
import pandas as pd
import numpy as np
from datetime import datetime
import os

timestamp = datetime.now().strftime("%m%d-%H%M%S")
file_bus = f"asset/{timestamp}/bus.csv"
file_stop = f"asset/{timestamp}/stop.json"

def getBus() -> pd.DataFrame:
  path = os.path.dirname(__file__)
  os.chdir(path)
  df = pd.read_csv(file_bus)
  return df

def getStop() -> pd.DataFrame:
  path = os.path.dirname(__file__)
  os.chdir(path)
  df = pd.read_json(file_stop)
  return df

def handleStop_init() -> None:  # init the stop
  df = pd.DataFrame(columns=list(range(len(Stop.list_obj[:-1]))))
  try :
    df.loc[0] = 0  # try to set the first row to 0
  except :
    pass
  saveStop(df)

def handleBus_init() -> None:  # init the bus
  df = pd.DataFrame(columns=['id', 'ppl', 'state'])
  saveBus(df)

def init() -> None:  # init all stuff
  path = os.path.dirname(__file__)
  os.chdir(path)
  os.makedirs(f"asset/{timestamp}", exist_ok=True)
  handleStop_init()
  handleBus_init()

def saveBus(df) -> None:
  df.to_csv(file_bus, index=False)

def saveStop(df) -> None:
  df.to_json(file_stop)

def handleBus_ppl(id:int, change:int) -> None:  # change the amount of ppl in the bus
  df = getBus()
  if any(df['id'] == id) :
    row = df.loc[df['id'] == id]
    row['ppl'] += change
  else :
    row = pd.DataFrame([[id, change, 0]], columns=['id', 'ppl', 'state'])
    df = df.append(row)
  saveBus(df)

def handleBus_state(id:int) -> None:  # change the state of the bus
  df = getBus()
  if any(df['id'] == id) :
    row = df.loc[df['id'] == id]
    row['state'] += 1
  else :
    row = pd.DataFrame([[id, 0, 0]], columns=['id', 'ppl', 'state'])
    df = df.append(row)
  saveBus(df)

def handleStop_ppl(index:int, change:int) -> None:  # change the amount of ppl at the stop queue
  df = getStop()
  df.loc[index] += change
  saveStop(df)