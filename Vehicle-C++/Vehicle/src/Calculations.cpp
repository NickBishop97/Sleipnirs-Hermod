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
    static double oldFuel;
    if (fuelR == 0) {
        FuelRemaining = fuelR;
        oldFuel = fuelR;
        FuelSpent = 0;
    } else if (oldFuel == 0) {
        oldFuel = fuelR;
    } else {
        FuelSpent = oldFuel - fuelR;
        oldFuel = fuelR;
    }
    return FuelSpent;
}

/**
 * @brief Sets the Fuel Remainging in the tank
 *
 * @param fuelR
 */
void FuelSenor::set_FuelRemaining(double fuelR)
{
    FuelRemaining = fuelR;
}

/**
 * @brief Gets the Fuel Remainging in the tank
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
        // sets mpg to 0 when either milesT or fuelS have a negative value
        temp = 0.0;
    } else if (milesT == 0.0 || Gal == 0.0) {
        if (milesT > 0) {
            // set mpg to max value when car is traveling but has no fuel
            temp = 99.9;
        } else {
            // set mpg to -1 when car is at idle or out of fuel
            temp = -1.0;
        }
    } else {
        temp = milesT / Gal;
        if (temp > 99.99) {
            // std::cout << "99.9" << std::endl;
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
    if (MPG == 0 || MPG == -1 || FR == 0) {
        return -1;
    }
    ML = MPG * Gal;
    return ML;
}

/**
 * @brief Updates the Trip data for the current selected trip
 *
 * @param newMiles Newly recieved Miles Traveled data
 * @param newMPG Newly recieved MPG data
 * @param newtime Newly recieved Time data
 */
void TD::updateData(double newMiles, double newMPG, double newtime)
{
    miles = miles + newMiles;
    time = time + newtime;
    if (newMPG != 0 && newMPG != -1) {
        MPG = getAvMpg(newMPG);
    }
    if (newMiles != 0 && newtime != 0) {
        speed = getAvSpeed(newMiles, newtime);
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
    SPtotal = SPtotal + (newMiles / newTime);
    SPcount++;
    return (SPtotal / SPcount);
}

/**
 * @brief Calculates the Avg MPG
 *
 * @param MPG
 * @return double
 */
double TD::getAvMpg(double MPG)
{
    total = total + MPG;
    MPGcount++;
    return (total / MPGcount);
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
void TM::AvSpeed(double newMiles, double newTime)
{
    tripPtr->getAvSpeed(newMiles, newTime);
}

/**
 * @brief calculates the avg MPG
 *
 * @param MPG
 */
void TM::AvMpg(double MPG)
{
    tripPtr->getAvMpg(MPG);
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
