#ifndef CALCULATIONS_H
#define CALCULATIONS_H

#define TANK_CAP 10

#include <vector>
#include <iostream>

class FuelSenor
{

private:
    unsigned long index = 0;
    double FuelSpent = 0.0;
    double FuelRemaining = 0.0;

public:
    double fuelspent(double fuelR);
    double get_FuelRemaining();
    unsigned long get_index();
    void set_FuelRemaining(double fuelR);
    void set_index(unsigned long i);
};

class Moving
{
    private:
        unsigned long index;
    public:
        unsigned long get_index();
        void set_index(unsigned long i);
};

//std::vector<double> MPG;
//double avgMPG;

//double get_avgMPG();
//double set_avgMPG(double MPG);
//double get_MPG(int location);
//double FuelRemainPercent(double fuelR);
//double mpg(double milesT, double fuelS);

#endif