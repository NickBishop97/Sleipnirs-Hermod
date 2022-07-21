#include <boost/test/unit_test.hpp>
#include "../Calculations.h"

#define INIT_VALUE 0.0
#define NEG_VALUE -0.001
#define HIGHNEG_VALUE -100
#define NORMAL_VALUE 9.5
#define ERROR_CODE -1.0

BOOST_AUTO_TEST_SUITE(MPG_TEST)

/**
 * @brief Assert that when milesT, fuelS, or both is INIT_VALUE
 * then mpg should return a NEG_VALUE, unless miles is
 * greater than zero and fuelS is 0 then mpg should return 99.9
 * 
 * @param fuelS Fuel Spent
 * @param milesT Miles Traveled
 * @return bool
 */
BOOST_AUTO_TEST_CASE(ZERO_MPG_CASE)
{
    MPG mpg;
    BOOST_CHECK(mpg.mpg(INIT_VALUE, INIT_VALUE) == ERROR_CODE);
    BOOST_CHECK(mpg.mpg(NORMAL_VALUE, INIT_VALUE) == 99.9);
    BOOST_CHECK(mpg.mpg(INIT_VALUE, NORMAL_VALUE) == ERROR_CODE);
}

/**
 * @brief Assert that when milesT, fuelS, or both is NEG_VALUE
 * then mpg should return a ERROR_CODE
 * 
 * @param fuelS Fuel Spent
 * @param milesT Miles Traveled
 * @return bool
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
 * 
 * @param fuelS Fuel Spent
 * @param milesT Miles Traveled
 * @return bool
 */
BOOST_AUTO_TEST_CASE(HIGHNEG_MPG_CASE)
{
    MPG mpg;
    BOOST_CHECK(mpg.mpg(HIGHNEG_VALUE, HIGHNEG_VALUE) == ERROR_CODE);
    BOOST_CHECK(mpg.mpg(NORMAL_VALUE, HIGHNEG_VALUE) == ERROR_CODE);
    BOOST_CHECK(mpg.mpg(HIGHNEG_VALUE, NORMAL_VALUE) == ERROR_CODE);
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