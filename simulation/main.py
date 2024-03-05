import_string = \
'''
import numpy as np
import pandas as pd
'''
### LINK START! (https://github.com/evnchn/linkstart.py)
for line in import_string.splitlines():
    if "import" in line:
        #print(line)
        try:
            exec(line)
        except:
            if "#" in line:
                package_name = line.split("#")[-1]
            else:
                splits = line.split("import")
                if "from" in line:
                    package_name = splits[0].replace("from","")
                else:
                    package_name = splits[1]
            package_name = package_name.strip()
            #print("Installing {}...".format(package_name))    
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            try:
                exec(line)
            except:
                print("Failed to install {}".format(package_name))
### DONE
from elements import *  # self-define
import datahandling  # self-define
import os

### init ###
path = os.path.dirname(__file__)
os.chdir(path)

datahandling.init()

### simulation ###
for time in range(MAX_TIME + 1) :
  loop(time)