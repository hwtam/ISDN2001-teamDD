import elements # self-define
import pandas as pd
import numpy as np
from datetime import datetime
import os

### changeable parameters ###
record : bool = False  # record mode
### changeable parameters ###

timestamp = datetime.now().strftime("%m%d-%H%M%S")
file_bus = f"asset/{timestamp}/bus.csv"
file_stop = f"asset/{timestamp}/stop.json"
file_record_bus = f"asset/{timestamp}/record_bus.csv"
file_record_stop = f"asset/{timestamp}/record_stop.json"

def getBus(b = False) -> pd.DataFrame:  # getBus(True) to get the record
  path = os.path.dirname(__file__)
  os.chdir(path)
  if b :
    df = pd.read_csv(file_record_bus)
  else :
    df = pd.read_csv(file_bus)
  return df

def getStop(b = False) -> pd.DataFrame:  # getStop(True) to get the record
  path = os.path.dirname(__file__)
  os.chdir(path)
  if b :
    df = pd.read_json(file_record_stop)
  else :
    df = pd.read_json(file_stop)
  return df


def handleStop_init() -> None:  # init the stop
  df = pd.DataFrame(np.zeros((1, len(elements.Stop.list_obj[:-1])), dtype=np.int8),
                    columns=["Stop" + str(i) for i in range(len(elements.Stop.list_obj[:-1]))])
  saveStop(df)
  if record :
    df = pd.DataFrame(np.zeros((1, len(elements.Stop.list_obj[:-1])+1), dtype=np.int8),
                 columns=["Time"] + ["Stop" + str(i) for i in range(len(elements.Stop.list_obj[:-1]))])
    saveStop(df, True)

def handleBus_init() -> None:  # init the bus
  df = pd.DataFrame(columns=['id', 'ppl', 'state'])
  saveBus(df)
  if record :
    df = pd.DataFrame(columns=['time', 'id', 'ppl', 'state'])
    saveBus(df, True)

def init() -> None:  # init all stuff
  path = os.path.dirname(__file__)
  os.chdir(path)
  os.makedirs(f"asset/{timestamp}", exist_ok=True)
  handleStop_init()
  handleBus_init()


def saveBus(df:pd.DataFrame, b = False) -> None:
  if b :
    df.to_csv(file_record_bus, index=False)
  else :
    df.to_csv(file_bus, index=False)

def saveStop(df:pd.DataFrame, b = False) -> None:
  if b :
    df.to_json(file_record_stop, orient='records')
  else :
    df.to_json(file_stop, orient='records')


def handleBus_ppl(id:int, change:int, time:int) -> None:  # change the amount of ppl in the bus
  if (change == 0) :
    return
  df = getBus()
  if any(df['id'] == id) :
    df.loc[df['id'] == id, 'ppl'] += change
  else :
    row = pd.DataFrame([[id, change, 0]], columns=['id', 'ppl', 'state'])
    df = pd.concat([df, row])
  saveBus(df)
  record_bus(time)

def handleBus_state(id:int, time:int) -> None:  # change the state of the bus
  df = getBus()
  if id in df['id'].values :
    df.loc[df['id'] == id, 'state'] += 1
  else :
    row = pd.DataFrame([[id, 0, 0]], columns=['id', 'ppl', 'state'])
    df = pd.concat([df, row])
  saveBus(df)
  record_bus(time)

def handleStop_ppl(index:int, change:int, time:int) -> None:  # change the amount of ppl at the stop queue
  df = getStop()
  df.loc[0]["Stop" + str(index)] += change
  saveStop(df)
  record_stop(time)


def record_bus(t) -> None:  # record the bus state
  if record :
    df = getBus()
    df_record = getBus(True)
    temp = df.tail(1).copy()
    temp.insert(0, "time", t)
    if (not temp.reset_index(drop=True).equals(df_record.tail(1).reset_index(drop=True))) :
      df_record = pd.concat([df_record, temp])
      saveBus(df_record, True)

def record_stop(t) -> None:  # record the stop state
  if record :
    df = getStop()
    df_record = getStop(True)
    temp = df.tail(1).copy()
    temp.insert(0, "Time", t)
    df_record = pd.concat([df_record, temp])
    saveStop(df_record, True)