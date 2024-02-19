import_string = \
'''
import openpyxl as xl # openpyxl
'''
### LINK START! (https://github.com/evnchn/linkstart.py)
for line in import_string.splitlines():
    if "import" in line:
        print(line)
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
import vis  # self-define
import os
import subprocess
import openpyxl as xl # openpyxl

### init ###
path = os.path.dirname(__file__)
os.chdir(path)

# init the bus stop (location, P_queue, P_off)
Stop(0, 20, 0) # start , most ppl get in, 0 ppl get off
Stop(90, 15, 20) # 2
Stop(318, 10, 40) # 3
Stop(366, 10, 5) # 4
Stop(404, 7.5, 10) # 5
Stop(488, 5, 30) # 6
Stop(553, 0, 100) # end , 0 ppl get in, all ppl get off

wb = vis.con_excel()

### simulation ###
for time in range(MAX_TIME + 1) :
  loop(time)
  vis.to_excel_ppl(wb, time)

vis.des_excel(wb)
print("\nSimulation finished")