/**
 * @file Testing_Main.cpp
 * @author Nick Bishop
 * @brief Main Unit Testing File
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */

/**
 * @def BOOST_TEST_DYN_LINK
 * Setups the dynamic link for boost test case
 * 
 * @def BOOST_TEST_MODULE
 * defines the Main module name for this test module
 */
#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE Main
#include "test_MilesLeft.cpp"
#include "test_FuelSensor.cpp"
#include "test_MPG.cpp"
#include "test_TripMeter.cpp"