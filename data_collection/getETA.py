from hk_bus_eta import HKEta #HK Bus Crawling@2021, https://github.com/hkbus/hk-bus-crawling
import subprocess
import os 
import sys

if len(sys.argv) > 1:
  seq = sys.argv[1]
else :
  seq = 0

os.chdir(os.path.dirname(__file__))
if not(os.path.exists("list.txt")):
  subprocess.run("py getList.py", shell=True)
f_name = "ETA-" + str(seq) + ".txt"
print("generating " + f_name + "...")

hketa = HKEta()
with open("list.txt", encoding="UTF-8") as f, open(f_name, "w", encoding="UTF-8") as out:
  txt = f.readlines()
  for s in txt :
    s = s.rstrip()
    try:
      out.write(s + " : \n")
      etas = hketa.getEtas(route_id = s, seq=int(seq), language="en") # seq -> which bus stop
      out.write(str(etas) + "\n")
    except Exception as e :
      print(e)
      out.write("error" + "\n")
    finally :
      out.write("\n")

print("done")