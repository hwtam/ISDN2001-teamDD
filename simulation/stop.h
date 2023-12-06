// obj for the stop

#include <iostream>
using namespace std;

class stop {
  public:
    int ppl; // current ppl at the queue // by camera
    int time_next_arrival; // remainning time for the next arrival // by eta
    int location; // relative "location" of the stop at the route // by real data
    double P_queue;  // P(how many ppl get in the queue per time) // by history, forecast
    double P_off;  // P(how many ppl get off the minibus per people in bus) // by history, forecast

    stop() : ppl{0}, time_next_arrival{-1}, location{-1}, P_queue{0}, P_off{0} {};
    stop(int location, double P_queue, double P_off) : stop() {
      location = location;
      P_queue = P_queue;
      P_off = P_off;
    }
  
};