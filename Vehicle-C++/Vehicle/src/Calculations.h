/**
 * @file Calculations.h
 * @author Team Sleipnir
 * @brief Defines all the Calculations classes
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#ifndef CALCULATIONS_H
#define CALCULATIONS_H

#define TANK_CAP 10

#include <vector>
#include <iostream>

/**
 * @brief Does calculations that are required for functionality of the Full Sensor
 *
 */
class FuelSenor {

private:
    double FuelSpent;
    double FuelRemaining;

public:
    /**
     * @brief Construct a new Fuel Senor object
     * 
     */
    FuelSenor()
        : FuelSpent(0.0)
        , FuelRemaining(10.0)
    {
    }

    /**
     * @brief Destroy the Fuel Senor object
     * 
     */
    ~FuelSenor()
    {
    }
    double fuelspent(double fuelR);
    double get_FuelRemaining();
    void set_FuelRemaining(double fuelR);
};

/**
 * @brief Calculates MPG and stores them in a vector
 *
 */
class MPG {
private:
    std::vector<double> MpG{ 0 };

public:
    /**
     * @brief Construct a new MPG object
     * 
     */
    MPG()
    {
    }

    /**
     * @brief Destroy the MPG object
     * 
     */
    ~MPG()
    {
    }
    double get_MPG();
    double mpg(double milesT, double fuelS);
};

/**
 * @brief Calculates Miles Left using MPG and Fuel Remaining
 *
 */
class ML {
public:
    double get_MilesLeft(double MPG, double FR);
};

/**
 * @brief Calculates the Trip data to get the required values for the dashboard
 *
 */
class TD {
private:
    double miles;
    double speed;
    double time;
    double MPG;
    double MPGcount, total, SPcount, SPtotal;

public:
    /**
     * @brief Construct a new Default TD object
     * 
     */
    TD()
    {
    }

    /**
     * @brief Construct a new TD object
     * 
     * @param iMiles New Miles Traveled
     * @param ispeed New Speed
     * @param itime New Time data
     * @param iMPG New MPG
     */
    TD(double iMiles, double ispeed, double itime, double iMPG)
    {
        miles = iMiles;
        speed = ispeed;
        time = itime;
        MPG = iMPG;
        MPGcount = 0;
        total = 0;
        SPcount = 0;
        SPtotal = 0;
    }

    /**
     * @brief Destroy the TD object
     * 
     */
    ~TD()
    {
    }
    void updateData(double newMiles, double newMPG, double newtime);
    double getAvSpeed(double newMiles, double newTime);
    double getAvMpg(double MPG);
    double getmiles();
    double getspeed();
    double gettime();
    double getMPG();
    void clear();
};

/**
 * @brief Sets the current trip and calls TD to update the data on that specific
 *trip
 *
 */
class TM {
private:
    TD trip1;
    TD trip2;
    TD* tripPtr;

public:
    /**
     * @brief Construct a new TM object
     * 
     */
    TM()
        : trip1(TD(0, 0, 0, 0))
        , trip2(TD(0, 0, 0, 0))
        , tripPtr(&trip1)
    {
    }
    /**
     * @brief Destroy the TM object
     * 
     */
    ~TM()
    {
    }
    void toggleTrip();
    void AvSpeed(double newMiles, double newTime);
    void AvMpg(double MPG);
    void updateTrip(double newMiles, double newMPG, double newtime);
    std::tuple<double, double, double, double> GetTripData();
    void clear();
};

#endif