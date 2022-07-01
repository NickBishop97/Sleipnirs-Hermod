#ifndef CALCULATIONS_H
#define CALCULATIONS_H

#define TANK_CAP 10

#include <vector>
#include <iostream>

class Calculations
{

private:
    std::vector<double> MPG;
    double avgMPG;
    double gallon;
    double FuelSpent;
    double FuelRemaining = 0;

public:
    double mpg(double milesT, double fuelS);
    double FuelRemainPercent(double fuelR);
    double fuelspent(double fuelR);
    double get_LtoG(double fuelL);
    double get_MPG(int location);
    double get_avgMPG();
    double get_FuelRemaining();
    double set_avgMPG(double MPG);
    void set_FuelRemaining(double fuelR);
};

#endif