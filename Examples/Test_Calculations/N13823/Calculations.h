#ifndef CALCULATIONS_H
#define CALCULATIONS_H

class Calculations {
  private:
        double milesTraveled;
        double fuelSpent;
        double milesPerGallon;
  
  public:

    void setCalculations(double milesTraveled, double fuelSpent, double milesPerGallon);
    double getmilesTraveled() { return milesTraveled; }
    double getfuelSpent() { return fuelSpent; }
    double getmilesPerGallon() { return milesPerGallon; }

    static double calculateMilesPerGallon(double milesTraveled, double fuelSpent) { 
        if (fuelSpent <= 0 && milesTraveled > 0)
        {
            return -1;
        }
        else if (fuelSpent == 0)
        {
            return 0;
        }
        else 
        {
            return (milesTraveled / (fuelSpent * 0.2641722)); 
        }   
        
    }
    static double calculateMilesRemaining(double milesPerGallon, double fuelRemaining) { return (milesPerGallon * fuelRemaining); }
};

#endif