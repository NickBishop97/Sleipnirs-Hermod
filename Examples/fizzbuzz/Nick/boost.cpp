#include <iostream>
#include <string>
#include <sstream>
#include "fizz.h"
#include <boost/lexical_cast.hpp>

BOOST_AUTO_TEST_CASE(FIZZBUZZ_NotDivby3or5)
{
    for(int i = 1; i <= 100; ++i){
        if(i%3 != 0 && i%5 != 0){
            std::string str1 = boost::lexical_cast<std::string>(i);
            BOOST_CHECK(fizzbuzz(i) == str1);
            BOOST_REQUIRE_MESSAGE(current_test_passing(), "FAILED i=" <<i);
        }
    }
}

BOOST_AUTO_TEST_CASE(FIZZBUZZ_Divby3)
{
    
    for(int i = 1; i <= 100; ++i){
        if(i%3 == 0 && i%5 != 0){
            BOOST_CHECK(fizzbuzz(i) == "fizz");
            BOOST_REQUIRE_MESSAGE(current_test_passing(), "FAILED i=" <<i);
        }
    }
}

BOOST_AUTO_TEST_CASE(FIZZBUZZ_Divby5)
{
    for(int i = 1; i <= 100; ++i){
        if(i%5 == 0 && i%3 != 0){
            BOOST_CHECK(fizzbuzz(i) == "buzz");
            BOOST_REQUIRE_MESSAGE(current_test_passing(), "FAILED i=" <<i);
        }
    }
}

BOOST_AUTO_TEST_CASE(FIZZBUZZ_Divby3and5)
{
    for(int i = 1; i <= 100; ++i){
        if(i%3 == 0 && i%5 == 0){
            BOOST_CHECK(fizzbuzz(i) == "fizzbuzz");
            BOOST_REQUIRE_MESSAGE(current_test_passing(), "FAILED i=" <<i);
        }
    }
}
