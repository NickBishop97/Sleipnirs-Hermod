#include "MpG.h"

int main(
        int argc,
        char** argv)
{
    std::cout << "Publishing Fuel Status." << std::endl;
    srand(time(0));

    MPG calc_;

    MTSubscriber* myMTsub = new MTSubscriber();
    FRSubscriber* myFRsub = new FRSubscriber();
    MPGPublisher* myMPGpub = new MPGPublisher();
    if(myMTsub->init() && myFRsub->init() && myMPGpub->init())
    {
        //starts up two threads send fuel info and check tank
        std::thread milesT (&MTSubscriber::run, myMTsub, &calc_);
        std::thread fuelR (&FRSubscriber::run, myFRsub, &calc_);
        std::thread MPG (&MPGPublisher::run, myMPGpub, &calc_);
        std::thread AvgMPG (&MPGPublisher::AvgMPG, myMPGpub, &calc_);
        milesT.join();
        fuelR.join();
        MPG.join();
        AvgMPG.join();
    }

    delete myMTsub;
    delete myFRsub;
    delete myMPGpub;
    return 0;
}