/**
 * @file TripMeter.cpp
 * @author Nick Bishop
 * @brief Starts up the Trip Meter pub/subs
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include "TripMeter.h"

/**
 * @brief Starts up TripMeter publisher and subscribers and assigns them threads to work off of
 * 
 * @param argc 
 * @param argv 
 * @return int returns exit code 0
 */
int main(
    int argc,
    char** argv)
{
    std::cout << "Publishing Trip Data Status." << std::endl;
    srand(time(0));

    TM calc_;
    TripMeter data;

    TripMeter::MPGSubscriber* MPG = new TripMeter::MPGSubscriber();
    TripMeter::MTSubscriber* MT = new TripMeter::MTSubscriber();
    TripMeter::TMPublisher* TM = new TripMeter::TMPublisher();
    if (MPG->init() && MT->init() && TM->init()) {
        //starts up 4 threads to so it can publish trip data
        std::thread MPGsub(&TripMeter::MPGSubscriber::run, MPG, &data);
        std::thread MTsub(&TripMeter::MTSubscriber::run, MT, &data);
        std::thread TMpub(&TripMeter::TMPublisher::run, TM, &calc_, &data);
        std::thread time(&TripMeter::TMPublisher::time, TM, &data);
        MPGsub.join();
        MTsub.join();
        TMpub.join();
        time.join();
    }

    delete MPG;
    delete MT;
    delete TM;
    return 0;
}