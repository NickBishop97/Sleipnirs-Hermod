#include "Calculations.h"


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

void FuelSenor::set_FuelRemaining(double fuelR)
{
    FuelRemaining = fuelR;
}

double FuelSenor::get_FuelRemaining()
{
    return FuelRemaining;
}
