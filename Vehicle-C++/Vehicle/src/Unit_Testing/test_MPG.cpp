/**
 * @file test_MPG.cpp
 * @author Nick Bishop
 * @brief Runs unit testing on Miles Per Gallong Calculations
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include <boost/test/unit_test.hpp>
#include "../Calculations.h"

/**
 * @def INIT_VALUE 
 * Initial 0 value for testing purposes 
 * 
 * @def NEG_VALUE 
 * A random negative decimal value for testing purposes 
 * 
 * @def HIGHNEG_VALUE 
 * A high negative value for testing purposes 
 * 
 * @def NORMAL_VALUE 
 * A normal number value for testing purposes 
 * 
 * @def ERROR_CODE 
 * The return value for an error
 * 
 * @def MAX_MILEAGE
 * A max allowed value for miles per gallon
 * 
 * @def EXPECTED_VALUE
 * A calculated expected value for comparison purposes
 */
#define INIT_VALUE 0.0
#define NEG_VALUE -0.001
#define HIGHNEG_VALUE -100
#define NORMAL_VALUE 9.5
#define ERROR_CODE -1.0
#define MAX_MILEAGE 99.9
#define EXPECTED_VALUE (NORMAL_VALUE / (1 * 0.264172))

BOOST_AUTO_TEST_SUITE(MPG_TEST)

/**
 * @brief Assert that when milesT, fuelS, or both is INIT_VALUE
 * then mpg should return a NEG_VALUE, unless miles is
 * greater than zero and fuelS is 0 then mpg should return 99.9
 */
BOOST_AUTO_TEST_CASE(ZERO_MPG_CASE)
{
    MPG mpg;
    BOOST_CHECK(mpg.mpg(INIT_VALUE, INIT_VALUE) == ERROR_CODE);
    BOOST_CHECK(mpg.mpg(NORMAL_VALUE, INIT_VALUE) == MAX_MILEAGE);
    BOOST_CHECK(mpg.mpg(INIT_VALUE, NORMAL_VALUE) == ERROR_CODE);
}

/**
 * @brief Assert that when milesT, fuelS, or both is NEG_VALUE
 * then mpg should return a ERROR_CODE
 */
BOOST_AUTO_TEST_CASE(NEG_MPG_CASE)
{
    MPG mpg;
    BOOST_CHECK(mpg.mpg(NEG_VALUE, NEG_VALUE) == ERROR_CODE);
    BOOST_CHECK(mpg.mpg(NORMAL_VALUE, NEG_VALUE) == ERROR_CODE);
    BOOST_CHECK(mpg.mpg(NEG_VALUE, NORMAL_VALUE) == ERROR_CODE);
}

/**
 * @brief Assert that when milesT, fuelS, or both is HIGHNEG_VALUE
 * then mpg should return a ERROR_CODE
 */
BOOST_AUTO_TEST_CASE(HIGHNEG_MPG_CASE)
{
    MPG mpg;
    BOOST_CHECK(mpg.mpg(HIGHNEG_VALUE, HIGHNEG_VALUE) == ERROR_CODE);
    BOOST_CHECK(mpg.mpg(NORMAL_VALUE, HIGHNEG_VALUE) == ERROR_CODE);
    BOOST_CHECK(mpg.mpg(HIGHNEG_VALUE, NORMAL_VALUE) == ERROR_CODE);
}

/**
 * @brief Assert mpg with a normal value equals the EXPECTED_VALUE and when
 * called again it should return MAX_MILEAGE
 * 
 */
BOOST_AUTO_TEST_CASE(Normal_CASE)
{
    MPG mpg;
    BOOST_CHECK(mpg.mpg(NORMAL_VALUE, 1) == EXPECTED_VALUE);
    BOOST_CHECK(mpg.mpg(55, 0.5) == MAX_MILEAGE);
}

/**
 * @brief Assert get_MPG and it should return 0 since
 * there weren't any values input in.
 * 
 */
BOOST_AUTO_TEST_CASE(GET_MPG_CASE)
{
    MPG mpg;
    BOOST_CHECK(mpg.get_MPG() == INIT_VALUE);
}

BOOST_AUTO_TEST_SUITE_END()