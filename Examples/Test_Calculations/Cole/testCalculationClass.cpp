#define BOOST_TEST_MODULE CalculationClassTest
#include <boost/test/included/unit_test.hpp>
#define BOOST_TEST_DYN_LINK

#include "CalculationClass.hpp"


/**
 * Boost unit tests for MPG and Miles Left calculations
 * Test Cases:
 *      No fuel spent and no miles travelled
 *      Negative fuel spent
 *      Valid fuel spent and miles travelled
 *      Empty tank
 *      Negative fuel remaining
 */
BOOST_AUTO_TEST_CASE(testCalculations){
    CalculationClass dut(DEFAULT_MAX_TANK, 0, 0);   // initialize object to 0 miles traveled and full tank

    // Check results when no fuel spent and no miles travelled
    // Expect undefined values for both
    BOOST_CHECK(dut.getMPG() == UNDEF);
    BOOST_CHECK(dut.getMilesLeft() == UNDEF);

    // Test results if negative fuel spent
    // Expect undefined values for both
    dut.setFuelSpent(-1);
    BOOST_CHECK(dut.getMPG() == UNDEF);
    BOOST_CHECK(dut.getMilesLeft() == UNDEF);

    // Test results for valid fuel spent and miles travelled
    // Expect normal mpg and miles travelled
    dut.setFuelRemaining(13);
    dut.setFuelSpent(12);
    dut.setMiles(240);
    BOOST_CHECK(dut.getMPG() == 20);
    BOOST_CHECK(dut.getMilesLeft() == 260);

    // Test results for valid fuel spent and miles travelled
    // Expect normal mpg and miles travelled
    dut.setFuelSpent(19);
    dut.setFuelRemaining(6);
    dut.setMiles(646);
    BOOST_CHECK(dut.getMPG() == 34);
    BOOST_CHECK(dut.getMilesLeft() == 204);

    // Test results for empty tank
    // Expect 0 miles left
    dut.setFuelSpent(25);
    dut.setFuelRemaining(0);
    dut.setMiles(550);
    BOOST_CHECK(dut.getMPG() == 22);
    BOOST_CHECK(dut.getMilesLeft() == 0);

    // Test results for negative fuel remaining
    // Expect 0 miles left
    dut.setFuelSpent(26);
    dut.setFuelRemaining(-1);
    dut.setMiles(546);
    BOOST_CHECK(dut.getMPG() == 21);
    BOOST_CHECK(dut.getMilesLeft() == 0);
}
