import elements # self-define
import pandas as pd
import numpy as np
from datetime import datetime
import os
import pandas as pd

timestamp = datetime.now().strftime("%m%d-%H%M%S")
file_bus = f"asset/{timestamp}/bus.csv"
file_stop = f"asset/{timestamp}/stop.json"

def getValue(df:pd.DataFrame, col:str) -> int:
  return df[col].values[0]

def setValue(df:pd.DataFrame, col:str, change:int) -> None:
  df.loc[0][col] += change

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
  df = pd.DataFrame(np.zeros((1, len(elements.Stop.list_obj[:-1])), dtype=np.int8),
                    columns=["Stop" + str(i) for i in range(len(elements.Stop.list_obj[:-1]))])
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

def saveBus(df:pd.DataFrame) -> None:
  df.to_csv(file_bus, index=False)

def saveStop(df:pd.DataFrame) -> None:
  df.to_json(file_stop, orient='records')

def handleBus_ppl(id:int, change:int) -> None:  # change the amount of ppl in the bus
  if (change == 0) :
    return
  df = getBus()
  if any(df['id'] == id) :
    df.loc[df['id'] == id, 'ppl'] += change
  else :
    row = pd.DataFrame([[id, change, 0]], columns=['id', 'ppl', 'state'])
    df = pd.concat([df, row])
  saveBus(df)

def handleBus_state(id:int) -> None:  # change the state of the bus
  df = getBus()
  if id in df['id'].values :
    df.loc[df['id'] == id, 'state'] += 1
  else :
    row = pd.DataFrame([[id, 0, 0]], columns=['id', 'ppl', 'state'])
    df = pd.concat([df, row])
  saveBus(df)

def handleStop_ppl(index:int, change:int) -> None:  # change the amount of ppl at the stop queue
  df = getStop()
  df.loc[0]["Stop" + str(index)] += change
  saveStop(df)