import minibus
import stop

### const ###
vis_time_cylce = 30

def vis_excel(ws, t) :  # add a row
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
    l[index] = f"Bus{minibus.minibus.l_obj.index(bus)+1}: " + str(bus.ppl)
  ws.append(l)