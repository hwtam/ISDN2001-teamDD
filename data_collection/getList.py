from hk_bus_eta import HKEta
import os 

os.chdir(os.path.dirname(__file__))
print("generating list.txt...")

hketa = HKEta()
route_ids = list( hketa.route_list.keys() )
with open("list.txt", "w", encoding="UTF-8") as txt :
  for i in route_ids :
    if ("Choi Hung Station" in i) and ("11" in i) :
      txt.write(i + "\n")

print("done")