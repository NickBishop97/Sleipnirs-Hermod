#include <boost/lexical_cast.hpp>
#include "boost.h"

BOOST_AUTO_TEST_CASE(Calculations_Test_1)
{
    Calculations MPG;
    MPG.mpg(0.45, 0.34);
    BOOST_CHECK(MPG.get_MPG(0) == (0.45/(0.34 * 0.264172)));
}

BOOST_AUTO_TEST_CASE(Calculations_Test_2)
{
    Calculations MPG;
    MPG.mpg(0.70, 0);
    BOOST_CHECK(MPG.get_MPG(0) == 99.99);
}

BOOST_AUTO_TEST_CASE(Calculations_Test_3)
{
    Calculations MPG;
    MPG.mpg(0, 0.23);
    BOOST_CHECK(MPG.get_MPG(0) == -1);
}

BOOST_AUTO_TEST_CASE(Calculations_Test_4)
{
    Calculations MPG;
    MPG.mpg(-0.45, 0);
    BOOST_CHECK(MPG.get_MPG(0) == 0);
}

BOOST_AUTO_TEST_CASE(Calculations_Test_5)
{
    Calculations MPG;
    MPG.mpg(0, -0.50);
    BOOST_CHECK(MPG.get_MPG(0) == 0);
}

BOOST_AUTO_TEST_CASE(Calculations_Test_6)
{
    Calculations MPG;
    MPG.mpg(0, 0);
    BOOST_CHECK(MPG.get_MPG(0) == -1);
}