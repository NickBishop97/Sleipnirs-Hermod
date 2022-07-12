#include "Moving.h"

int main(
        int argc,
        char** argv)
{
    std::cout << "Publishing Fuel Status." << std::endl;
    srand(time(0));

    Moving calc_;

    MovePublisher* mypub = new MovePublisher();
    fuelSubscriber* mysub = new fuelSubscriber();
    if(mypub->init() && mysub->init())
    {
        //starts up two threads send fuel info and check tank
        std::thread isMoving (&MovePublisher::run, mypub, &calc_);
        std::thread readFuel (&fuelSubscriber::run, mysub, &calc_);
        isMoving.join();
        readFuel.join();
    }

    delete mypub;
    delete mysub;
    return 0;
}