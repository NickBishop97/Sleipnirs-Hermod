/**
 * @file test_MilesLeft.cpp
 * @author Spencer Williams
 * @brief Runs unit testing on Miles Left calculations
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include <iostream>
#include <boost/test/unit_test.hpp>
#include "../Calculations.h"

/**
 * @def INIT_VALUE 
 * Initial 0 value for testing purposes 
 * 
 * @def NEG_VALUE 
 * A random negative decimal value for testing purposes 
 * 
 * @def ERROR_CODE 
 * The return value for an error
 * 
 * @def POS_VALUE
 * A random positive value for testing purposes
 * 
 * @def DIFF_POS_VALUE
 * A random positive value fro testing purposes
 * 
 * @def LARGER_THAN_TANK 
 * A value that is larger than TANK_CAP for testing purposes 
 * 
 * @def EXPECTED
 * A calculated expected value for comparison purposes
 */
#define INIT_VALUE 0.0
#define NEG_VALUE -0.001
#define ERROR_CODE -1.0
#define POS_VALUE 13.2354
#define DIFF_POS_VALUE 21.54
#define LARGER_THAN_TANK 0.001 + TANK_CAP
#define EXPECTED (POS_VALUE*(5 * 0.264172))

BOOST_AUTO_TEST_SUITE(MILES_LEFT_TEST)

/** 
 * @brief Assert that when MPG is negative, 
 * then get_MilesLeft returns ERROR_CODE 
 *
 */
BOOST_AUTO_TEST_CASE(negativeMPG)
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(NEG_VALUE, POS_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when MPG is 0 or init, 
 * then get_MilesLeft returns ERROR_CODE 
 *
 */
BOOST_AUTO_TEST_CASE(zeroMPG)
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(INIT_VALUE, POS_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when FR is 0 or init, 
 * then get_MilesLeft returns  
 *
 */
BOOST_AUTO_TEST_CASE(zeroFR)
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(POS_VALUE, INIT_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when FR is negative, 
 * then get_MilesLeft returns ERROR_CODE
 *
 */
BOOST_AUTO_TEST_CASE(negativeFR)
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(POS_VALUE, NEG_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when FR is larger than tank,  
 * then get_MilesLeft returns ERROR_CODE
 */
BOOST_AUTO_TEST_CASE(excessiveFR)
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(POS_VALUE, LARGER_THAN_TANK) == ERROR_CODE);
}

/** 
 * @brief Assert that when FR is larger than tank,  
 * then get_MilesLeft returns ERROR_CODE
 */
BOOST_AUTO_TEST_CASE(correct_value)
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(POS_VALUE, 5) == EXPECTED);
}

BOOST_AUTO_TEST_SUITE_END()