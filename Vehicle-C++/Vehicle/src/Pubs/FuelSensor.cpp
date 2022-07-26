/**
 * @file FuelSensor.cpp
 * @author Nick Bishop
 * @brief Starts up and runs Fuel Sensor publishers
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include "FuelSensor.h"

/**
 * @brief Starts up FuelSensor publishers and assigns them threads to work off of
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

    FuelSenor calc_;
    FS data;

    FS::FuelRemainPublisher* myFRpub = new FS::FuelRemainPublisher();
    FS::FuelSpentPublisher* myFSpub = new FS::FuelSpentPublisher();
    if (myFRpub->init() && myFSpub->init()) {
        //starts up two threads send fuel info and check tank
        std::thread sendfuelR(&FS::FuelRemainPublisher::run, myFRpub, &calc_, &data);
        std::thread checktank(&FS::FuelRemainPublisher::check, myFRpub, &calc_, &data);
        std::thread sendfuelS(&FS::FuelSpentPublisher::run, myFSpub, &calc_, &data);
        sendfuelR.join();
        checktank.join();
        sendfuelS.join();
    }

    delete myFRpub;
    delete myFSpub;
    return 0;
}