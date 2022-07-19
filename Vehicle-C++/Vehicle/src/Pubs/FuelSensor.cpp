#include "FuelSensor.h"

int main(
    int argc,
    char** argv)
{
    std::cout << "Publishing Fuel Status." << std::endl;
    srand(time(0));

    FuelSenor calc_;

    FuelRemainPublisher* myFRpub = new FuelRemainPublisher();
    FuelSpentPublisher* myFSpub = new FuelSpentPublisher();
    if (myFRpub->init() && myFSpub->init()) {
        //starts up two threads send fuel info and check tank
        std::thread sendfuelR(&FuelRemainPublisher::run, myFRpub, &calc_);
        std::thread checktank(&FuelRemainPublisher::check, myFRpub, &calc_);
        std::thread sendfuelS(&FuelSpentPublisher::run, myFSpub, &calc_);
        sendfuelR.join();
        checktank.join();
        sendfuelS.join();
    }

    delete myFRpub;
    delete myFSpub;
    return 0;
}