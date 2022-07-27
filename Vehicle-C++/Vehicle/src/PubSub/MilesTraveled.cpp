/**
 * @file MilesTraveled.cpp
 * @author Nick Bishop
 * @brief Starts up the Miles Traveled Sensor
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include "MilesTraveled.h"

/**
 * @brief Starts up MilesTraveled publisher and subscriber and assigns them threads to work off of
 * 
 * @param argc 
 * @param argv 
 * @return int returns exit code 0
 */
int main(
    int argc,
    char** argv)
{
    std::cout << "Publishing Fuel Status." << std::endl;
    srand(time(0));

    MT data;

    MT::MilesPublisher* mypub = new MT::MilesPublisher();
    MT::MoveSubscriber* mysub = new MT::MoveSubscriber();
    if (mypub->init() && mysub->init()) {
        //starts up two threads send fuel info and check tank
        std::thread milesT(&MT::MilesPublisher::run, mypub, &data);
        std::thread ismoving(&MT::MoveSubscriber::run, mysub, &data);
        milesT.join();
        ismoving.join();
    }

    delete mypub;
    delete mysub;
    return 0;
}