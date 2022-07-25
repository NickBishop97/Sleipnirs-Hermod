/**
 * @file Calculations.cpp
 * @author Team Sleipnir
 * @brief Contains all the calculations functions for data processing for Hermod
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include "Calculations.h"
#include <tuple>

/**
 * @brief Calculates the full spent when given the current fuel Remaning, needs
 *to be run twice to get the first fuel spent reading(only applies during first
 *run)
 *
 * @param fuelR
 * @return double
 */
double FuelSenor::fuelspent(double fuelR)
{
    static double oldFuel = 0;
    if (fuelR > TANK_CAP) {
        return -1;
    }
    if (fuelR == 0) {
        FuelRemaining = fuelR;
        oldFuel = fuelR;
        FuelSpent = 0;
    } else if (fuelR < 0) {
        return -1;
    } else if (oldFuel == 0) {
        oldFuel = fuelR;
    } else {
        FuelSpent = oldFuel - fuelR;
        oldFuel = fuelR;
    }
    return FuelSpent;
}

/**
 * @brief Sets the Fuel Remaining in the tank
 *
 * @param fuelR Fuel Remaining
 */
void FuelSenor::set_FuelRemaining(double fuelR)
{
    if (0 <= fuelR && fuelR <= TANK_CAP) {
        FuelRemaining = fuelR;
    }
}

/**
 * @brief Gets the Fuel Remaining in the tank
 *
 * @return double
 */
double FuelSenor::get_FuelRemaining()
{
    return FuelRemaining;
}

/**
 * @brief Calculates the MPG using miles traveled and fuel spent
 *
 * @param milesT
 * @param fuelS
 * @return double
 */
double MPG::mpg(double milesT, double fuelS)
{
    double temp;
    double Gal = fuelS * 0.264172;
    if (milesT < 0 || Gal < 0) {
        // sets mpg to -1 when either milesT or fuelS have a negative value
        temp = -1;
    } else if (milesT == 0.0 || Gal == 0.0) {
        if (milesT > 0) {
            // set mpg to max value when car is traveling but has no fuel
            temp = 99.9;
        } else {
            // set mpg to 0.0 when car is at idle or out of fuel
            temp = -1;
        }
    } else {
        temp = milesT / Gal;
        if (temp > 99.99) {
            temp = 99.9;
        }
    }
    if (temp > 0) {
        MpG.push_back(temp);
    }
    return temp;
}

/**
 * @brief Return current MPG
 *
 * @return double
 */
double MPG::get_MPG()
{
    return MpG.back();
}

/**
 * @brief Calculates the Miles Left till the tank is empty
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining
 * @return double
 */
double ML::get_MilesLeft(double MPG, double FR)
{
    double Gal = FR * 0.264172;
    double ML;
    if (MPG <= 0 || FR <= 0 || FR > TANK_CAP) {
        return -1;
    }
    ML = MPG * Gal;
    return ML;
}

/**
 * @brief Updates the Trip data for the current selected trip
 *
 * @param newMiles Newly received Miles Traveled data
 * @param newMPG Newly received MPG data
 * @param newtime Newly received Time data
 */
void TD::updateData(double newMiles, double newMPG, double newtime)
{
    if (newMiles >= 0 || newMPG >= 0 || newtime > 0) {
        double temp;
        temp = getAvMpg(newMPG);
        if (temp == -1) {
            return;
        } else {
            MPG = temp;
        }
        if (newMiles != 0 && newtime != 0) {
            double data;
            data = getAvSpeed(newMiles, newtime);
            if (data == -1) {
                return;
            } else {
                speed = data;
            }
        }
        miles = miles + newMiles;
        time = time + newtime;
    }
}
 
/**
 * @brief Calculates the Avg speed
 *
 * @param newMiles current miles traveled
 * @param newTime time that pasted during the distance traveled
 * @return double Returns avg speed of the car
 */
double TD::getAvSpeed(double newMiles, double newTime)
{
    // Return error code if time 0 or less or if newMiles is negative
    if (newTime <= 0 || newMiles < 0) {
        return -1.0;
    } else {
        SPtotal = SPtotal + (newMiles / newTime);
        SPcount++;
    }
    if (SPcount <= 0) {
        return -1.0;

    }
    // Return error code if SPcount is 0 or less
    else {
        return (SPtotal / SPcount);
    }
}

/**
 * @brief Calculates the Avg MPG
 *
 * @param MPG
 * @return double
 */
double TD::getAvMpg(double MPG)
{
    // If MPG is negative, return a error code
    if (MPG < 0) {
        return -1.0;
    } else {
        total = total + MPG;
        MPGcount++;
    }
    // If MPGcount is negative, return a error code
    if (MPGcount < 0) {
        return -1.0;
    } else {
        return (total / MPGcount);
    }
}

/**
 * @brief Sets all the values in the tripdata to zero
 *
 */
void TD::clear()
{
    miles = 0;
    speed = 0;
    time = 0;
    MPG = 0;
    MPGcount = 0;
    total = 0;
}

/**
 * @brief returns Miles stored in the current trip
 *
 * @return double
 */
double TD::getmiles()
{
    return miles;
}

/**
 * @brief returns speed data in the current trip
 *
 * @return double
 */
double TD::getspeed()
{
    return speed;
}

/**
 * @brief returns time data in the current trip
 *
 * @return double
 */
double TD::gettime()
{
    return time;
}

/**
 * @brief returns MPG data in the current trip
 *
 * @return double
 */
double TD::getMPG()
{
    return MPG;
}

/**
 * @brief Toggles between the two trips and saves the currently selected
 * trip in a pointer.
 *
 */
void TM::toggleTrip()
{
    if (tripPtr == &trip1) {
        tripPtr = &trip2;
    } else {
        tripPtr = &trip1;
    }
}

/**
 * @brief Updates the trip Data that is stored in the tripPtr
 *
 * @param newMiles
 * @param newMPG
 * @param newtime
 */
void TM::updateTrip(double newMiles, double newMPG, double newtime)
{
    tripPtr->updateData(newMiles, newMPG, newtime);
}

/**
 * @brief Clears the trip Data that is stored in the tripPtr
 *
 */
void TM::clear()
{
    tripPtr->clear();
}

/**
 * @brief calculates the avg speed of the car based on miles and time traveled
 *
 * @param newMiles
 * @param newTime
 */
double TM::AvSpeed(double newMiles, double newTime)
{
    return tripPtr->getAvSpeed(newMiles, newTime);
}

/**
 * @brief calculates the avg MPG
 *
 * @param MPG
 */
double TM::AvMpg(double MPG)
{
    return tripPtr->getAvMpg(MPG);
}

/**
 * @brief returns trip data info of the current trip
 *
 * @return std::tuple<double, double, double, double>
 */
std::tuple<double, double, double, double> TM::GetTripData()
{
    return std::make_tuple(tripPtr->getmiles(), tripPtr->getspeed(),
                           tripPtr->gettime(), tripPtr->getMPG());
}
