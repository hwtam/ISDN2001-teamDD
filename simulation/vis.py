import minibus
import stop
import openpyxl as xl

### const ###
vis_time_cylce = 30

def vis_time(t) :
  if (t % vis_time_cylce != 0) :
    return
  with open("visualization_time.txt", 'a') as f :
    f.write(f"time =\t{t} :\n")

    f.write("--- minibus ---\n")
    for bus in minibus.minibus.l_obj :
      if (bus.end()) :
        continue
      i = minibus.minibus.l_obj.index(bus)
      f.write(f"minibus\t{i} : \n")
      f.write(f"\tlocation : {bus.position}\n")
      f.write(f"\tamount of people : {bus.ppl}\n\n")

    f.write("--- minibus stop ---\n")
    i = 1
    for s in stop.stop.l_obj :
      f.write(f"stop\t{i}({s.location}) : \n")
      f.write(f"\tamount of people : {s.ppl}\n\n")
      i += 1
    
    f.write("###############\n\n")

def vis_excel(ws, t) :
  if (t % vis_time_cylce != 0) :
    return
  l = [t]
  # the amount of ppl at each stop
  for s in stop.stop.l_obj :
    l.append(s.ppl)
    l.append("")
  # the amount of ppl at the bus
  for bus in minibus.minibus.l_obj :
    if (bus.end()) :
      continue
    index = 2  # "C"
    for location in stop.stop.l_location[1:] :
      if bus.position < location :
        break
      index += 2
    l[index] = f"Bus{minibus.minibus.l_obj.index(bus)}: " + str(bus.ppl)
  ws.append(l)