#include <iostream>
#include <boost/test/unit_test.hpp>
#include "../Calculations.h"

#define INIT_VALUE 0.0
#define NEG_VALUE -0.001
#define ERROR_CODE -1.0
#define POS_VALUE 13.2354
#define DIFF_POS_VALUE 21.54
#define LARGE_DOUBLE1 226754.6785576899 // Overflow testing*
#define LARGE_DOUBLE2 223654.6735786819

using namespace std;

BOOST_AUTO_TEST_SUITE(Trip_Data_AvSpeed)

/** 
 * @brief Assert that when getAvSpeed receives 0 time
 * then it returns ERROR_CODE 
 *
 * @param MPG New Miles
 * @param FR New Time
 * @return bool
 */
BOOST_AUTO_TEST_CASE(zeroTime) 
{
    TD td;
    BOOST_CHECK(td.getAvSpeed(POS_VALUE, INIT_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when getAvSpeed receives neg time 
 * then it returns ERROR_CODE 
 *
 * @param MPG New Miles
 * @param FR New Time
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negativeTime) 
{
    TD td;
    BOOST_CHECK(td.getAvSpeed(POS_VALUE, NEG_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when getAvSpeed receives neg new miles
 * then it returns ERROR_CODE 
 *
 * @param MPG New Miles
 * @param FR New Time
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negativeMiles) 
{
    TD td;
    BOOST_CHECK(td.getAvSpeed(NEG_VALUE, POS_VALUE) == ERROR_CODE);

}

BOOST_AUTO_TEST_SUITE_END()

BOOST_AUTO_TEST_SUITE(Trip_Data_AvMPG)

/** 
 * @brief Assert that when getAvMpg receives neg MPG
 * then it returns ERROR_CODE 
 *
 * @param MPG Miles Per Gallon
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negativeMPG) 
{
    TD td;
    BOOST_CHECK(td.getAvMpg(NEG_VALUE) == ERROR_CODE);
}

BOOST_AUTO_TEST_SUITE_END()

