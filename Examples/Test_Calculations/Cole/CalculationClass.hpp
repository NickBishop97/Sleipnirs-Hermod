#ifndef CALCULATIONCLASS_HPP
#define CALCULATIONCLASS_HPP

#define DEFAULT_MAX_TANK 25     // Tank size in Gallons
#define UNDEF -1        // Status when MPG and MilesLeft should not be calculated
                        // i.e. when 0 fuel spent


/**
 * Class to perform MPG and Miles Left calculations on given DDS data 
 */
class CalculationClass{
    public:
        CalculationClass();
        CalculationClass(double fuelRemaining, double fuelSpent, double miles);
        void setFuelRemaining(double fuelRemaining);
        void setFuelSpent(double fuelSpent);
        void setMiles(double miles);
        double getMPG();
        double getMilesLeft();
    private:
        double fuelRemaining;
        double fuelSpent;
        double miles;
        double mpg;
        double milesLeft;
};

#endif
