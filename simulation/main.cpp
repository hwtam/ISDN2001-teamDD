// main program for the simulation

#include<iostream>
using namespace std;

#include"minibus.h"
#include"stop.h"

const int MAX_TIME = 1000;  // max number of unit time , -1 for infinte max time
const int NUM_STOP = 7;  // number of bus stop
int num_bus = 1;  // current number of buses

void arrive(stop, minibus) {

}

minibus* moreBUS(minibus* buses) {  // to double the size of the 
  minibus** temp = new minibus*[num_bus*2];
  for (int i = 0; i < num_bus; i++) {
    temp[i] = buses[i];
  }
  delete[] buses;
  buses = temp;
  num_bus *= 2;
  return buses;
}

int main() {
  // init
  minibus buses[num_bus];  // list to store the minibuses
  buses[0] = minibus();
  stop stops[NUM_STOP];  // list to store the bus stop // 11M have 7 stops


  // simulate
  for (int time = 0; MAX_TIME == -1 | time < MAX_TIME; time++) {  // each loop = 1 unit time in reality

  }
}