// obj for the stop

#include <iostream>
using namespace std;

class stop {
  public:
    int ppl;
    int time_next_arrival;
  
  friend class arrival;
};