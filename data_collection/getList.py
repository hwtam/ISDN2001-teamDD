from hk_bus_eta import HKEta #HK Bus Crawling@2021, https://github.com/hkbus/hk-bus-crawling
import os 

os.chdir(os.path.dirname(__file__))
print("generating list.txt...")

hketa = HKEta()
route_ids = list( hketa.route_list.keys() )
with open("list.txt", "w", encoding="UTF-8") as list, open("whole.txt", "w", encoding="UTF-8") as whole :
  for i in route_ids :
    whole.write(i + "\n")
    if ("Choi Hung Station" in i) and ("11" in i) :
      list.write(i + "\n")

print("done")