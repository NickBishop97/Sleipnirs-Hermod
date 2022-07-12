#include "DisDisplay.h"

int main(
        int argc,
        char** argv)
{

    DDSubscriber* mysub = new DDSubscriber();
    if(mysub->init())
    {
        //starts up two threads send fuel info and check tank
        std::thread DisDisplay (&DDSubscriber::run, mysub);
        DisDisplay.join();
    }

    delete mysub;
    return 0;
}