#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE

#include "Calculations.h"
#include <iostream>
#include <boost/test/unit_test.hpp>

void Calculations::setCalculations(double m_milesTraveled, double m_fuelSpent, double m_milesPerGallon)
{
    milesTraveled = m_milesTraveled;
    fuelSpent = m_fuelSpent;
    milesPerGallon = m_milesPerGallon;
}

// Normal behavior
BOOST_AUTO_TEST_CASE(normalMPG)
{
    Calculations cal;
    BOOST_CHECK_CLOSE(cal.calculateMilesPerGallon(1, 1), 3.785409668390542, 0.001);
}

// Zero behavior
BOOST_AUTO_TEST_CASE(zero_miles_MPG)
{
    Calculations cal;
    BOOST_CHECK_CLOSE(cal.calculateMilesPerGallon(0, 1), 0, 0.001);
}

// Zero behavior
BOOST_AUTO_TEST_CASE(zero_both_MPG)
{
    Calculations cal;
    BOOST_CHECK(cal.calculateMilesPerGallon(0, 0) == 0);
}

// Zero behavior
BOOST_AUTO_TEST_CASE(zero_fuel_MPG)
{
    Calculations cal;
    BOOST_CHECK_CLOSE(cal.calculateMilesPerGallon(3, 0), -1, 0.001);
}