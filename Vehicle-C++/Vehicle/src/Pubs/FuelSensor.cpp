#include "FuelSensor.h"

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