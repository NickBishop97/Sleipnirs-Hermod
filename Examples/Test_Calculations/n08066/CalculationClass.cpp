#include <iostream>
#include "CalculationClass.hpp"


CalculationClass::CalculationClass(){
    this->fuelSpent = 0;
    this->fuelRemaining = DEFAULT_MAX_TANK;
    this->miles = 0;
    this->mpg = UNDEF;
    this->milesLeft = UNDEF;
}


CalculationClass::CalculationClass(double fuelRemaining, double fuelSpent, double miles){
    this->fuelSpent = fuelSpent;
    this->fuelRemaining = fuelRemaining;
    this->miles = miles;
    this->mpg = UNDEF;
    this->milesLeft = UNDEF;
}


void CalculationClass::setFuelRemaining(double fr){
    fuelRemaining = fr;
}

void CalculationClass::setFuelSpent(double fs){
    fuelSpent = fs;
}


void CalculationClass::setMiles(double m){
    miles = m;
}


double CalculationClass::getMPG(){
    if(fuelSpent <= 0){
        mpg = UNDEF;
    }
    else{
        mpg = miles/fuelSpent;
    }

    return mpg;
}


double CalculationClass::getMilesLeft(){
    if(mpg == UNDEF){
        milesLeft = UNDEF;
    }
    else{
        milesLeft = mpg * fuelRemaining;
        if(milesLeft < 0){
            milesLeft = 0;
        }
    }

    return milesLeft;
}