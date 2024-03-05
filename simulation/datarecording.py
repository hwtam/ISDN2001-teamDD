from elements import *  # self-define
import datahandling  # self-define
import pandas as pd
import numpy as np
import os

file_bus = f"asset/{datahandling.timestamp}/record_bus.csv"
file_stop = f"asset/{datahandling.timestamp}/record_stop.csv"

def getBus() -> pd.DataFrame:
  path = os.path.dirname(__file__)
  os.chdir(path)
  df = pd.read_csv(file_bus)
  return df

def getStop() -> pd.DataFrame:
  path = os.path.dirname(__file__)
  os.chdir(path)
  df = pd.read_csv(file_stop)
  return df

def handleStop_init() -> None:  # init the stop
  df = pd.DataFrame(columns=list(range(len(Stop.list_obj[:-1]))))
  saveStop(df)

def handleBus_init() -> None:  # init the bus
  df = pd.DataFrame(columns=['time', 'id', 'ppl', 'state'])
  saveBus(df)

def init() -> None:  # init all stuff
  datahandling.init()
  handleStop_init()
  handleBus_init()

def saveBus(df:pd.DataFrame) -> None:
  df.to_csv(file_bus, index=False)

def saveStop(df:pd.DataFrame) -> None:
  df.to_csv(file_stop)

def recordBus_ppl(id:int, change:int) -> None:  # same as handleBus_ppl, but always new row
  datahandling.handleBus_ppl(id, change)
  df = getBus()
  if any(df['id'] == id) :
    prev = df.loc[df['id'] == id]
    row = pd.DataFrame([[id, prev['ppl'] + change, prev['state']]], columns=['id', 'ppl', 'state'])
  else :
    row = pd.DataFrame([[id, change, 0]], columns=['id', 'ppl', 'state'])
  df = df.append(row)
  saveBus(df)

def recordBus_state(id:int) -> None:  # same as handleBus_state, but always new row
  datahandling.handleBus_state(id)
  df = getBus()
  if any(df['id'] == id) :
    prev = df.loc[df['id'] == id]
    row = pd.DataFrame([[id, prev['ppl'], prev['state'] + 1]], columns=['id', 'ppl', 'state'])
  else :
    row = pd.DataFrame([[id, 0, 0]], columns=['id', 'ppl', 'state'])
  df = df.append(row)
  saveBus(df)

def recordStop_ppl(index:int, change:int) -> None:  # change the amount of ppl at the stop queue
  datahandling.handleStop_ppl(index, change)
  df = getStop()
  try :
    last_row = df.tail(1)
    new_row = last_row.copy()
  except :
    new_row = pd.DataFrame(np.zeros((1,len(Stop.list_obj[:-1])), columns=list(range(len(Stop.list_obj[:-1])))))
  new_row[index] += change
  df = df.append(new_row)
  saveStop(df)