/**
 * @file MilesLeft.cpp
 * @author Nick Bishop
 * @brief Starts up and runs all the publishers and subscribers for MilesLeft
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include "MilesLeft.h"

int main(
    int argc,
    char** argv)
{
    std::cout << "Publishing Miles Left Status." << std::endl;
    srand(time(0));

    ML calc_;
    MilesLeft data;

    MilesLeft::MPGSubscriber* MPG = new MilesLeft::MPGSubscriber();
    MilesLeft::FRSubscriber* FR = new MilesLeft::FRSubscriber();
    MilesLeft::MLPublisher* ML = new MilesLeft::MLPublisher();
    if (MPG->init() && FR->init() && ML->init()) {
        //starts up two threads send fuel info and check tank
        std::thread MPGsub(&MilesLeft::MPGSubscriber::run, MPG, &data);
        std::thread FRsub(&MilesLeft::FRSubscriber::run, FR, &data);
        std::thread MLpub(&MilesLeft::MLPublisher::run, ML, &calc_, &data);
        MPGsub.join();
        FRsub.join();
        MLpub.join();
    }

    delete MPG;
    delete FR;
    delete ML;
    return 0;
}