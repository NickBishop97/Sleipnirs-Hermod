#include "MpG.h"

int main(
    int argc,
    char** argv)
{
    std::cout << "Publishing MPG Status." << std::endl;
    srand(time(0));

    MPG calc_;
    MilesPerGallon data;

    MilesPerGallon::MTSubscriber* myMTsub = new MilesPerGallon::MTSubscriber();
    MilesPerGallon::FRSubscriber* myFRsub = new MilesPerGallon::FRSubscriber();
    MilesPerGallon::MPGPublisher* myMPGpub = new MilesPerGallon::MPGPublisher();
    if (myMTsub->init() && myFRsub->init() && myMPGpub->init()) {
        //starts up two threads send fuel info and check tank
        std::thread milesT(&MilesPerGallon::MTSubscriber::run, myMTsub, &calc_, &data);
        std::thread fuelR(&MilesPerGallon::FRSubscriber::run, myFRsub, &calc_, &data);
        std::thread MPG(&MilesPerGallon::MPGPublisher::run, myMPGpub, &calc_, &data);
        milesT.join();
        fuelR.join();
        MPG.join();
    }

    delete myMTsub;
    delete myFRsub;
    delete myMPGpub;
    return 0;
}