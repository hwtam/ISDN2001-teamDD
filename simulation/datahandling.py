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
  # init the bus stop (location, P_queue, P_off)
  Stop(0, 50, 0) # start , most ppl get in, 0 ppl get off
  Stop(90, 7.5, 20) # 1
  Stop(318, 10, 35) # 2
  Stop(366, 7.5, 10) # 3
  Stop(404, 7, 20) # 4
  Stop(488, 5, 30) # 5
  Stop(553, 0, 100) # end , 0 ppl get in, all ppl get off

  df = pd.DataFrame(np.zeros((1,len(Stop.list_obj[:-1])), dtype=np.int8),
                    columns=list(range(len(Stop.list_obj[:-1]))))
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
  df.to_json(file_stop, orient='records')

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