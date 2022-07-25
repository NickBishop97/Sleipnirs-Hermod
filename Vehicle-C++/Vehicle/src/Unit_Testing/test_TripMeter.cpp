/**
 * @file test_TripMeter.cpp
 * @author Team Sleipnir
 * @brief Runs Unit testing on Trip Meter Calculations
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
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
    TM tm;
    BOOST_CHECK(tm.AvSpeed(NEG_VALUE, POS_VALUE) == ERROR_CODE);
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
    TM tm;
    BOOST_CHECK(tm.AvMpg(NEG_VALUE) == ERROR_CODE);
}

BOOST_AUTO_TEST_SUITE_END()

BOOST_AUTO_TEST_SUITE(Trip_Data_UpdateTrip)

/**
 * @brief Assert that when GetTripData is called 
 * and the last updateTrip had negative values
 * then all resulting return values should be zero or
 * the perviously held value.
 * 
 */
BOOST_AUTO_TEST_CASE(GetTripData_NegCase)
{
    TM tm;
    tm.updateTrip(NEG_VALUE, NEG_VALUE, NEG_VALUE);
    double test[4] = { INIT_VALUE, INIT_VALUE, INIT_VALUE, INIT_VALUE };
    std::tie(test[0], test[1], test[2], test[3]) = tm.GetTripData();
    BOOST_CHECK(test[0] == INIT_VALUE);
    BOOST_CHECK(test[1] == INIT_VALUE);
    BOOST_CHECK(test[2] == INIT_VALUE);
    BOOST_CHECK(test[3] == INIT_VALUE);
}

/**
 * @brief Assert that when GetTripData is called 
 * and the newMiles has data of INIT_VALUE then the return of 
 * miles and speed should be zero.
 * 
 */
BOOST_AUTO_TEST_CASE(GetTripData_MilesZeroCase)
{
    TM tm;
    tm.updateTrip(INIT_VALUE, POS_VALUE, POS_VALUE);
    double test[4] = { INIT_VALUE, INIT_VALUE, INIT_VALUE, INIT_VALUE };
    std::tie(test[0], test[1], test[2], test[3]) = tm.GetTripData();
    BOOST_CHECK(test[0] == INIT_VALUE);
    BOOST_CHECK(test[1] == INIT_VALUE);
    BOOST_CHECK(test[2] == POS_VALUE);
    BOOST_CHECK(test[3] == POS_VALUE);
}

/**
 * @brief Assert that when GetTripData is called 
 * and the newMiles has data of INIT_VALUE then the return of 
 * miles and speed should be zero.
 * 
 */
BOOST_AUTO_TEST_CASE(GetTripData_MpgZeroCase)
{
    TM tm;
    tm.updateTrip(POS_VALUE, INIT_VALUE, POS_VALUE);
    double test[4] = { INIT_VALUE, INIT_VALUE, INIT_VALUE, INIT_VALUE };
    std::tie(test[0], test[1], test[2], test[3]) = tm.GetTripData();
    BOOST_CHECK(test[0] == POS_VALUE);
    BOOST_CHECK(test[1] == (POS_VALUE / POS_VALUE));
    BOOST_CHECK(test[2] == POS_VALUE);
    BOOST_CHECK(test[3] == INIT_VALUE);
}

/**
 * @brief Assert that when data is stored into tripdata
 * and tripmeter is calls to clear tripdata that all values in
 * tripdata ar set to INIT_VALUE.
 * 
 */
BOOST_AUTO_TEST_CASE(GetTripData_ClearCase)
{
    TM tm;
    tm.updateTrip(POS_VALUE, POS_VALUE, POS_VALUE);
    double test[4] = { INIT_VALUE, INIT_VALUE, INIT_VALUE, INIT_VALUE };
    tm.clear();
    std::tie(test[0], test[1], test[2], test[3]) = tm.GetTripData();
    BOOST_CHECK(test[0] == INIT_VALUE);
    BOOST_CHECK(test[1] == INIT_VALUE);
    BOOST_CHECK(test[2] == INIT_VALUE);
    BOOST_CHECK(test[3] == INIT_VALUE);
}

/**
 * @brief Assert that when data is stored into tripdata
 * and tripmeter calls to switch to trip2 that all the tripdata
 * should still be at INIT_VALUE.
 * 
 */
BOOST_AUTO_TEST_CASE(GetTripData_ChangeTripCase)
{
    TM tm;
    tm.updateTrip(POS_VALUE, POS_VALUE, POS_VALUE);
    double test[4] = { INIT_VALUE, INIT_VALUE, INIT_VALUE, INIT_VALUE };
    tm.toggleTrip();
    std::tie(test[0], test[1], test[2], test[3]) = tm.GetTripData();
    BOOST_CHECK(test[0] == INIT_VALUE);
    BOOST_CHECK(test[1] == INIT_VALUE);
    BOOST_CHECK(test[2] == INIT_VALUE);
    BOOST_CHECK(test[3] == INIT_VALUE);
    tm.toggleTrip();
    std::tie(test[0], test[1], test[2], test[3]) = tm.GetTripData();
    BOOST_CHECK(test[0] == POS_VALUE);
    BOOST_CHECK(test[1] == (POS_VALUE / POS_VALUE));
    BOOST_CHECK(test[2] == POS_VALUE);
    BOOST_CHECK(test[3] == POS_VALUE);
}

BOOST_AUTO_TEST_SUITE_END()