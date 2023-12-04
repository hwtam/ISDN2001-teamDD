from hk_bus_eta import HKEta
import subprocess
import os 

os.chdir(os.path.dirname(__file__))
subprocess.run("cls", shell=True)
hketa = HKEta()
with open("list.txt", encoding="UTF-8") as f, open("detail.txt", "w", encoding="UTF-8") as out:
  txt = f.readlines()
  for s in txt :
    s = s.rstrip()
    if "Choi Hung Station" in s :
      if "11" in s :
        try:
          out.write(s + " : \n")
          etas = hketa.getEtas(route_id = s, seq=0, language="en")
          out.write(str(etas) + "\n")
        except Exception as e :
          print(e)
          out.write("error" + "\n")
        finally :
          out.write("\n")

print("ok")