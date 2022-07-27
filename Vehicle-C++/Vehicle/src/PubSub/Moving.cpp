/**
 * @file Moving.cpp
 * @author Nick Bishop
 * @brief Starts up the isMoving Sensor that checks if the car is moving
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include "Moving.h"

/**
 * @brief Starts up Moving publisher and subscriber and assigns them threads to work off of
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

    Moving data;

    Moving::MovePublisher* mypub = new Moving::MovePublisher();
    Moving::fuelSubscriber* mysub = new Moving::fuelSubscriber();
    if (mypub->init() && mysub->init()) {
        //starts up two threads send fuel info and check tank
        std::thread isMoving(&Moving::MovePublisher::run, mypub, &data);
        std::thread readFuel(&Moving::fuelSubscriber::run, mysub, &data);
        isMoving.join();
        readFuel.join();
    }

    delete mypub;
    delete mysub;
    return 0;
}