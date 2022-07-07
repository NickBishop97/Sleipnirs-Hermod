#include "Calculations.h"

/**
 * @brief Calculates the full spent when given the current fuel Remaning, needs to be run twice to get the first fuel spent reading(only applies during first run)
 * 
 * @param fuelR 
 * @return double 
 */
double FuelSenor::fuelspent(double fuelR)
{
    static double oldFuel;
    if(fuelR == 0)
    {
        FuelRemaining = fuelR;
        oldFuel = fuelR;
        FuelSpent = 0;
    }
    else if(oldFuel == 0)
    {
        oldFuel = fuelR;
    }
    else
    {
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
 * @brief Gets the current index count of the Fuel remaining sensor
 * 
 * @return unsigned long 
 */
unsigned long FuelSenor::get_index()
{
    return index;
}

/**
 * @brief Gets the current Check tank status, if its 1 it will indicate the tank has been refilled recently
 * 
 * @return unsigned long 
 */
unsigned long FuelSenor::get_check()
{
    return check;
}

/**
 * @brief Sets the current index count of the Fuel remaining sensor
 * 
 * @param i 
 */
void FuelSenor::set_index(unsigned long i)
{
    index = i;
}

/**
 * @brief Sets the current Check tank status, if its 1 it will indicate the tank has been refilled recently
 * 
 * @param c 
 */
void FuelSenor::set_check(unsigned long c)
{
    check = c;
}

/**
 * @brief Gets the if the car if it is moving or not, 1 equals moving
 * 
 * @return unsigned long 
 */
unsigned long Moving::get_index()
{
    return index;
}

/**
 * @brief Sets the if the car if it is moving or not, 1 equals moving
 * 
 * @param i 
 */
void Moving::set_index(unsigned long i)
{
    index = i;
}

/**
 * @brief Returns 1 or 0 if car is moving or not
 * 
 * @return unsigned long 
 */
unsigned long MilesTraveled::get_index()
{
    return index;
}

/**
 * @brief Sets index to 1 or 0 if car is moving or not
 * 
 * @param i 
 */
void MilesTraveled::set_index(unsigned long i)
{
    index = i;
}

//double Calculations::mpg(double milesT, double fuelS)
//{
//    double temp;
//    double Gal = fuelS * 0.264172;
//    if(milesT < 0 || Gal < 0)
//    {
//        //sets mpg to 0 when either milesT or fuelS have a negative value
//        temp = 0.0;
//    }
//    else if(milesT == 0 || Gal == 0)
//    {
//        if(milesT > 0)
//        {
//            //set mpg to max value when car is traveling but has no fuel
//            temp = 99.99;
//        }
//        else
//        {
//            //set mpg to -1 when car is at idle or out of fuel
//            temp = -1.0;
//        }
//    }
//    else {
//        temp = milesT/Gal;
//    }
//    MPG.push_back(temp);
//    return temp;
//}

//double Calculations::FuelRemainPercent(double fuelR)
//{
//    return (fuelR/TANK_CAP)*100;
//}

//double Calculations::get_MPG(int location)
//{
//    return MPG.at(location);
//}

//double Calculations::get_avgMPG()
//{
//    if(Calculations::MPG.size() >= 10)
//    {
//        double temp = 0;
//        int MAX = Calculations::MPG.size();
//        for(int i = 0; i < MAX; ++i)
//        {
//            temp += get_MPG(i);
//        }
//        Calculations::set_avgMPG(temp/MAX);
//        Calculations::MPG.clear();
//        return Calculations::avgMPG;
//    }
//    else
//    {
//        return 0;
//    }
//}

//double Calculations::set_avgMPG(double MPG)
//{
//    return Calculations::avgMPG = (Calculations::avgMPG + MPG)/2 ; 
//}
