// to control the minibus and the bustop

#include <iostream>
using namespace std;

#include"minibus.h"
#include"stop.h"

class arrival {
  public:
    int ppl_in;
    int ppl_out;

    static void arrive(minibus minibus, stop stop) {

    }

    arrival() = delete;
    arrival(arrival &other) = delete;
};