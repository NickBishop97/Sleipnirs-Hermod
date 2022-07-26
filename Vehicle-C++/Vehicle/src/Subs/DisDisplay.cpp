/**
 * @file DisDisplay.cpp
 * @author Nick Bishop
 * @brief Starts up the Distance display subscriber
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include "DisDisplay.h"

int main(
    int argc,
    char** argv)
{

    DDSubscriber* mysub = new DDSubscriber();
    if (mysub->init()) {
        //starts up two threads send fuel info and check tank
        std::thread DisDisplay(&DDSubscriber::run, mysub);
        DisDisplay.join();
    }

    delete mysub;
    return 0;
}