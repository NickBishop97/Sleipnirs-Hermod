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

double MPG::mpg(double milesT, double fuelS)
{
   double temp;
   double Gal = fuelS * 0.264172;
   if(milesT < 0 || Gal < 0)
   {
       //sets mpg to 0 when either milesT or fuelS have a negative value
       temp = 0.0;
   }
   else if(milesT == 0 || Gal == 0)
   {
       if(milesT > 0)
       {
           //set mpg to max value when car is traveling but has no fuel
           temp = 99.9;
       }
       else
       {
           //set mpg to -1 when car is at idle or out of fuel
           temp = -1.0;
       }
   }
   else {
       temp = milesT/Gal;
       if(temp > 99.99)
        {
            temp = 99.9;
        }
   }
   if(temp > 0)
   {
        MpG.push_back(temp);
   }
   return temp;
}

double MPG::FuelRemainPercent(double fuelR)
{
   return (fuelR/TANK_CAP)*100;
}

double MPG::get_MPG()
{
   return MpG.back();
}

double MPG::get_avgMPG()
{
   if(MPG::MpG.size() >= 10)
   {
       double temp = 0;
       int MAX = MPG::MpG.size();
       for(int i = 0; i < MAX; ++i)
       {
           temp += get_MPG();
       }
       MPG::set_avgMPG(temp/MAX);
       MPG::MpG.clear();
       return MPG::avgMPG;
   }
   else
   {
       return -1;
   }
}

double MPG::set_avgMPG(double MPG)
{
   return MPG::avgMPG = (MPG::avgMPG + MPG)/2 ; 
}

double MPG::get_MT()
{
    return MT;
}
double MPG::get_FS()
{
    return FS;
}
void MPG::set_MT(double mt)
{
    MT = mt;
}
void MPG::set_FS(double fs)
{
    FS = fs;
}
unsigned long MPG::get_MTindex()
{
    return MTindex;
}
unsigned long MPG::get_FSindex()
{
    return FSindex;
}
void MPG::set_MTindex(unsigned long i)
{
    MTindex = i;
}
void MPG::set_FSindex(unsigned long i)
{
    FSindex = i;
}
void MPG::set_MPGindex(unsigned long i)
{
    MPGindex = i;
}
unsigned long MPG::get_MPGindex()
{
    return MPGindex;
}