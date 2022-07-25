/**
 * @file test_FuelSensor.cpp
 * @author Team Sleipnir
 * @brief Runs unit testing on FuelSensor calculations
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include <boost/test/unit_test.hpp>
#include "../Calculations.h"

#define INIT_VALUE 0.0
#define NEG_VALUE -0.001
#define HIGHNEG_VALUE -100
#define ERROR_CODE -1.0
#define NORMAL_VALUE 9.5
#define LARGER_THAN_TANK 0.001 + TANK_CAP

BOOST_AUTO_TEST_SUITE(FUEL_TEST)

/**
 * @brief Assert that when FuelReamining is 0 
 * then fuelspent returns INIT_VALUE
 * 
 * @param fuelR Fuel Remaining
 * @return bool
 */
BOOST_AUTO_TEST_CASE(zero_case)
{
    FuelSenor FS;
    BOOST_CHECK(FS.fuelspent(INIT_VALUE) == INIT_VALUE);
}

/**
 * @brief Assert that when FuelReamining is 0 
 * then get_FuelRamaining returns INIT_VALUE
 * 
 * @param fuelR Fuel Remaining
 * @return bool
 */
BOOST_AUTO_TEST_CASE(zero_case2)
{
    FuelSenor FS;
    FS.set_FuelRemaining(INIT_VALUE);
    BOOST_CHECK(FS.get_FuelRemaining() == INIT_VALUE);
}

/**
 * @brief Assert that when FuelReamining is negative
 * then fuelspent returns ERROR_CODE
 * 
 * @param fuelR Fuel Remaining
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negative_case)
{
    FuelSenor FS;
    BOOST_CHECK(FS.fuelspent(NEG_VALUE) == ERROR_CODE);
    BOOST_CHECK(FS.fuelspent(HIGHNEG_VALUE) == ERROR_CODE);
}

/**
 * @brief Assert that when FuelRemaining is negative
 * then get_FuelRemaining returns perviously held value
 * 
 * @param fuelR Fuel Remaining
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negative_case2)
{
    FuelSenor FS;
    FS.set_FuelRemaining(TANK_CAP);
    FS.set_FuelRemaining(NEG_VALUE);
    BOOST_CHECK(FS.get_FuelRemaining() == TANK_CAP);
}

/**
 * @brief Assert that when FuelRemaining is normal value
 * then fuelspent returns expected value
 * 
 * @param fuelR Fuel Remaining
 * @return bool
 */
BOOST_AUTO_TEST_CASE(normal_case)
{
    FuelSenor FS;
    BOOST_CHECK(FS.fuelspent(NORMAL_VALUE) == INIT_VALUE);
    BOOST_CHECK(FS.fuelspent(NORMAL_VALUE - 1) == NORMAL_VALUE - (NORMAL_VALUE - 1));
}

/**
 * @brief Assert that when FuelRemaining has Tank Larger
 * than TANK_CAP then fuelspent should return ERROR_CODE
 * 
 * @param fuelR Fuel Remaining
 * @return bool
 */
BOOST_AUTO_TEST_CASE(tank_larger_case)
{
    FuelSenor FS;
    BOOST_CHECK(FS.fuelspent(LARGER_THAN_TANK) == ERROR_CODE);
}

/**
 * @brief Assert that when FuelRemaining has Tank Larger
 * than TANK_CAP then get_FuelRemaining should return previously held value
 * 
 * @param fuelR Fuel Remaining
 * @return bool
 */
BOOST_AUTO_TEST_CASE(tank_larger_case2)
{
    FuelSenor FS;
    FS.set_FuelRemaining(INIT_VALUE);
    FS.set_FuelRemaining(LARGER_THAN_TANK);
    BOOST_CHECK(FS.get_FuelRemaining() == INIT_VALUE);
}

BOOST_AUTO_TEST_SUITE_END()