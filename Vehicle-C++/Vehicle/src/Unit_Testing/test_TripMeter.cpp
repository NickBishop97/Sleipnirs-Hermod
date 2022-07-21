#include <iostream>
#include <boost/test/unit_test.hpp>
#include "../Calculations.h"

#define INIT_VALUE 0.0
#define NEG_VALUE -0.001
#define ERROR_CODE -1.0
#define POS_VALUE 13.2354
#define DIFF_POS_VALUE 21.54
#define LARGE_FR 226754.6785576899
#define LARGE_MPG 223654.6735786819

using namespace std;

/** 
 * @brief Assert that when getAvSpeed 
 * then get_MilesLeft returns ERROR_CODE 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(zeroTime) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(NEG_VALUE, POS_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when getAvSpeed 
 * then get_MilesLeft returns ERROR_CODE 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negativeTime) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(NEG_VALUE, POS_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when getAvSpeed 
 * then get_MilesLeft returns ERROR_CODE 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negativeSPcount) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(NEG_VALUE, POS_VALUE) == ERROR_CODE);
}


/** 
 * @brief Assert that when getAvSpeed 
 * then get_MilesLeft returns ERROR_CODE 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negativeSPcount) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(NEG_VALUE, POS_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when getAvSpeed 
 * then get_MilesLeft returns ERROR_CODE 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(zeroSPcount) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(NEG_VALUE, POS_VALUE) == ERROR_CODE);

}
/** 
 * @brief Assert that when getAvSpeed 
 * then get_MilesLeft returns ERROR_CODE 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(zeroNewMiles) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(NEG_VALUE, POS_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when getAvSpeed 
 * then get_MilesLeft returns ERROR_CODE 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negativeNewMiles) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(NEG_VALUE, POS_VALUE) == ERROR_CODE);
}