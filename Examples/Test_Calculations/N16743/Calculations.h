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
    double FuelSpent;

public:
    double mpg(double milesT, double fuelS);
    double FuelRemainPercent(double fuelR);
    double get_FuelSpent(double fuelL);
    double get_MPG(int location);
    double get_avgMPG();
    double set_avgMPG(double MPG);
};

#endif