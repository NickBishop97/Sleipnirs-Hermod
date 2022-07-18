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
    FuelSenor()
    {
        index = 0;
        check = 1;
        FuelSpent = 0.0;
        FuelRemaining = 10.0;
    }
    ~FuelSenor()
    {
    }
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
        unsigned long index = 0;
    public:
        Moving()
        {
            index = 0;
        }
        ~Moving()
        {
        }
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
        unsigned long index = 0;
    public:
        MilesTraveled()
        {
            index = 0;
        }
        ~MilesTraveled()
        {
        }
        unsigned long get_index();
        void set_index(unsigned long i);
};

/**
 * @brief Enables communication between pub/sub in MPG.h, and computes MPG
 * 
 */
class MPG
{
    private:
        std::vector<double> MpG{0};
        double avgMPG = 0.0;
        long avgMPGcount = 0;
        double MT = 0.0;
        double FS = 0.0;
        unsigned long MTindex = 0, FSindex = 0, MPGindex = 0;
    public:
        MPG()
        {
            avgMPG = 0.0;
            MT = 0.0;
            MTindex = 0;
            FSindex = 0;
            MPGindex = 0;
        }
        ~MPG()
        {
        }
        double get_avgMPG();
        double set_avgMPG(double MPG);
        double get_MPG();
        double FuelRemainPercent(double fuelR);
        double mpg(double milesT, double fuelS);
        double get_MT();
        double get_FS();
        unsigned long get_MPGindex();
        unsigned long get_MTindex();
        unsigned long get_FSindex();
        void set_MT(double mt);
        void set_FS(double fs);
        void set_MTindex(unsigned long i);
        void set_FSindex(unsigned long i);
        void set_MPGindex(unsigned long i);
};

/**
 * @brief Calculates Miles Left using MPG and Fuel Remaining
 * 
 */
class ML
{
    public:
        double get_MilesLeft(double MPG, double FR);
};

/**
 * @brief Calculates the Trip data to get the required values for the dashboard
 * 
 */
class TD
{
    private:
        double miles;
        double speed;
        double time;
        double MPG;
        double MPGcount, total, SPcount, SPtotal;
    public:
        TD()
        {
        }
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
 * @brief Sets the current trip and calls TD to update the data on that specific trip
 * 
 */
class TM
{
    private:
        TD trip1;
        TD trip2;
        TD* tripPtr;
    public:
        TM() 
            : trip1(TD(0,0,0,0)), trip2(TD(0,0,0,0)), tripPtr(&trip1)
        {
        }
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