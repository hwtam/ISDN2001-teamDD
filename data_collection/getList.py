from hk_bus_eta import HKEta
import subprocess
import os 

os.chdir(os.path.dirname(__file__))
subprocess.run("cls", shell=True)
#subprocess.run("touch list.txt", shell=True)
hketa = HKEta()
route_ids = list( hketa.route_list.keys() )
with open("list.txt", "w", encoding="UTF-8") as txt :
  for i in route_ids :
    txt.write(i + "\n")

print("ok")