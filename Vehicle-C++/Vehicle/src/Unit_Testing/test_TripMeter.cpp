#include <iostream>
#include <boost/test/unit_test.hpp>
#include "../Calculations.h"

#define INIT_VALUE 0.0
#define NEG_VALUE -0.001
#define ERROR_CODE -1.0
#define POS_VALUE 13.2354
#define DIFF_POS_VALUE 21.54
#define LARGE_FR 226754.6785576899 // Overflow testing*
#define LARGE_MPG 223654.6735786819

using namespace std;

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
    BOOST_CHECK(td.getAvSpeed(NEG_VALUE, POS_VALUE) == ERROR_CODE);
}