#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE

#include <iostream>
#include <boost/test/unit_test.hpp>
#include "../Calculations.h"

#define NEG_VALUE -0.001
#define POS_VALUE 13.2354
#define DIFF_POS_VALUE 21.54
#define LARGE_FR 226754.6785576899
#define LARGE_MPG 223654.6735786819

using namespace std;

/** 
 * @brief Boost test to verify that when MPG is negative, 
 * then Miles remaining returns 0 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negativeMPG) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(-0.001, 22) == 0);
}

/** 
 * @brief Boost test to verify that when MPG is 0, 
 * then Miles remaining returns 0 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(zeroMPG) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(5.0, 0) == 0);
}

/** 
 * @brief Boost test to verify that when FR is 0, 
 * then Miles remaining returns 0 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(zeroFR) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(5.0, 0) == 0);
}

/** 
 * @brief Boost test to verify that when MPG is a double, 
 *  
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negtaiveFR) 
{
    
}

/** 
 * @brief Boost test to verify that when MPG is -1,  
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(extremeCheck) 
{
    
}