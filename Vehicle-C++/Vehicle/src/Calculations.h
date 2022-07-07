#ifndef CALCULATIONS_H
#define CALCULATIONS_H

#define TANK_CAP 10

#include <vector>
#include <iostream>

/**
 * @brief Enables communication between pub/sub in FuelSensor.h and does calculations that are required for functionality 
 * 
 */
class FuelSenor
{

private:
    unsigned long index = 0;
    unsigned long check = 1;
    double FuelSpent = 0.0;
    double FuelRemaining = 10.0;

public:
    double fuelspent(double fuelR);
    double get_FuelRemaining();
    unsigned long get_index();
    unsigned long get_check();
    void set_FuelRemaining(double fuelR);
    void set_index(unsigned long i);
    void set_check(unsigned long c);
};

/**
 * @brief Enables communication between pub/sub in Moving.h
 * 
 */
class Moving
{
    private:
        unsigned long index;
    public:
        unsigned long get_index();
        void set_index(unsigned long i);
};

/**
 * @brief Enables communication between pub/sub in MilesTraveled.h
 * 
 */
class MilesTraveled
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