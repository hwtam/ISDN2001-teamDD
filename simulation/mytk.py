import elements  # self-define
import datahandling  # self-define
import tkinter as tk
from tkinter import ttk

### changeable parameters ###
period = 1 # period of update
### changeable parameters ###

class BusTable(tk.Tk):

  obj = None

  def __init__(self, variable_names):
    super().__init__()
    self.title("bus.csv")

    # Create the Treeview widget
    self.tree = ttk.Treeview(self)
    self.tree["columns"] = ("people", "state")

    # Format the columns
    self.tree.column("#0", width=150, minwidth=150)
    self.tree.column("people", width=150, minwidth=150)
    self.tree.column("state", width=150, minwidth=150)

    # Add headings
    self.tree.heading("#0", text="id")
    self.tree.heading("people", text="People")
    self.tree.heading("state", text="State")

    # Add the Treeview to the window
    self.tree.pack(side="left", fill="y")

    # Store the variable names and associated treeview item IDs
    self.variables = {}

    # Add the variables to the table
    for name in variable_names:
      item_id = self.tree.insert("", "end", text=name)
      self.variables[name] = item_id

  def update_variable(self, name, ppl, state):
    # Update the value of a variable in the table
    item_id = self.variables.get(name)
    if not item_id:
      item_id = self.tree.insert("", "end", text=name)
      self.variables[name] = item_id
    self.tree.set(item_id, "people", ppl)
    self.tree.set(item_id, "state", state)

  def getObj():
    if (BusTable.obj == None):
      BusTable.obj = BusTable([])
      BusTable.obj.mainloop()
    return BusTable.obj

class StopTable(tk.Tk):

  obj = None

  def __init__(self, variable_names):
    super().__init__()
    self.title("stop.json")

    # Create the Treeview widget
    self.tree = ttk.Treeview(self)
    self.tree["columns"] = ("people")

    # Format the columns
    self.tree.column("#0", width=150, minwidth=150)
    self.tree.column("people", width=150, minwidth=150)

    # Add headings
    self.tree.heading("#0", text="Station index")
    self.tree.heading("people", text="People")

    # Add the Treeview to the window
    self.tree.pack(side="left", fill="y")

    # Store the variable names and associated treeview item IDs
    self.variables = {}

    # Add the variables to the table
    for name in variable_names:
      item_id = self.tree.insert("", "end", text=name)
      self.variables[name] = item_id

  def update_variable(self, name, ppl):
    print(f"{name = }")
    print(f"{ppl = }")
    # Update the value of a variable in the table
    item_id = self.variables.get(name)
    if not item_id:
      item_id = self.tree.insert("", "end", text=name)
      self.variables[name] = item_id
    self.tree.set(item_id, "people", ppl)

  def getObj():
    if (StopTable.obj == None):
      StopTable.obj = StopTable(["Stop" + str(i) for i in range(len(elements.Stop.list_obj[:-1]))])
      StopTable.obj.mainloop()
    return StopTable.obj
  
### functions ###
def update(t) :
  if (t % period == 0) :
    df = datahandling.getBus()
    for i in range(len(df)) :
      BusTable.getObj().update_variable(df.iloc[i]['id'], df.iloc[i]['ppl'], df.iloc[i]['state'])
    df = datahandling.getStop()
    for i in range(len(df)) :
      StopTable.getObj().update_variable("Stop" + str(i), df.iloc[i].values[0])
    BusTable.getObj().update()
    BusTable.getObj().after(1000)
    StopTable.getObj().update()
    StopTable.getObj().after(1000)