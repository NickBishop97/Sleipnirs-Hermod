#include "MilesTraveled.h"

int main(
    int argc,
    char** argv)
{
    std::cout << "Publishing Fuel Status." << std::endl;
    srand(time(0));

    MilesTraveled calc_;

    MilesPublisher* mypub = new MilesPublisher();
    MoveSubscriber* mysub = new MoveSubscriber();
    if (mypub->init() && mysub->init()) {
        //starts up two threads send fuel info and check tank
        std::thread milesT(&MilesPublisher::run, mypub, &calc_);
        std::thread ismoving(&MoveSubscriber::run, mysub, &calc_);
        milesT.join();
        ismoving.join();
    }

    delete mypub;
    delete mysub;
    return 0;
}