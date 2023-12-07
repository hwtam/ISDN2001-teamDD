import minibus
import stop

### var ###
MAX_TIME = 1000
NUM_STOP = 7
num_bus = 1

##### main #####

### init ###
# make the bus stop (location, P_queue, P_off)
stop.stop(0, 5, 0) # start , most ppl get in, 0 ppl get off
stop.stop(90, 5, .15) # 2
stop.stop(318, 5, .35) # 3
stop.stop(366, 5, .5) # 4
stop.stop(404, 5, .10) # 5
stop.stop(488, 5, .25) # 6
stop.stop(553, 0, 1) # end , 0 ppl get in, all ppl get off