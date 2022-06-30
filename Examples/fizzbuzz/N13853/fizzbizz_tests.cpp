
/*
//Test 1: Returns string fizz when num_in % 3 == 0
BOOST_AUTO_TEST_CASE(fizz_test){
    std::string actual;
    std::ostringstream ss_output;
    std::string expected = "fizz";
    std::vector<int> pos_cases;
    pos_cases.push_back(3);
    pos_cases.push_back(9);
    pos_cases.push_back(33);
    pos_cases.push_back(999999);

    for (unsigned int i = 0; i < pos_cases.size(); i++) {
      fizzbuzz(pos_cases[i], ss_output);
      BOOST_CHECK( ss_output.str() == expected );   
      ss_output.str("");
    }
}
*/
#define BOOST_TEST_MODULE MyTest
#include <boost/test/included/unit_test.hpp>
#include <boost/lexical_cast.hpp>

#include "fizzbizz.h"
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
//stuff gets more complex when adding more classes, data types, etc

//Test 1: Returns string fizz when num_in % 3 == 0
BOOST_AUTO_TEST_CASE(fizz_test){
    std::string expected = "fizz";
    std::vector<int> pos_cases;
    pos_cases.push_back(3);
    pos_cases.push_back(9);
    pos_cases.push_back(33);
    pos_cases.push_back(999999);


    std::ostringstream ss_output;
    for (unsigned int i = 0; i < pos_cases.size(); i++) {
      fizzbuzz(pos_cases[i], pos_cases[i], ss_output);
      BOOST_CHECK( ss_output.str() == expected );   
      ss_output.str("");
    }
}
//Test 2: Returns string buzz when num_in % 5 == 0
BOOST_AUTO_TEST_CASE(buzz_test){
    std::string expected = "buzz";
    std::vector<int> pos_cases;
    pos_cases.push_back(5);
    pos_cases.push_back(10);
    pos_cases.push_back(100);
    pos_cases.push_back(1000000000);

    std::ostringstream ss_output;
    for (unsigned int i = 0; i < pos_cases.size(); i++) {
      fizzbuzz(pos_cases[i], pos_cases[i], ss_output);
      BOOST_CHECK( ss_output.str() == expected );   
      ss_output.str("");
    }
}
//Test 3: Returns string fizzbuzz when num_in % 3 == 0 && num_in % 5 == 0
BOOST_AUTO_TEST_CASE(fizzbuzz_test){
    std::string expected = "fizzbuzz";

    std::vector<int> pos_cases;
    pos_cases.push_back(15);
    pos_cases.push_back(30);
    pos_cases.push_back(60);
    pos_cases.push_back(600000000);

    std::ostringstream ss_output;
    for (unsigned int i = 0; i < pos_cases.size(); i++) {
      fizzbuzz(pos_cases[i], pos_cases[i], ss_output);
      BOOST_CHECK( ss_output.str() == expected );   
      ss_output.str("");
    }
}


//Test 4: Returns the num_in if !(num_in % 5 == 0 || num_in % 3 == 0)
BOOST_AUTO_TEST_CASE(integer_return_test){
    std::vector<int> pos_cases;
    pos_cases.push_back(2);
    pos_cases.push_back(7);
    pos_cases.push_back(11);
    pos_cases.push_back(7919);
  
    std::ostringstream ss_output;
    for (unsigned int i = 0; i < pos_cases.size(); i++) {
      fizzbuzz(pos_cases[i], pos_cases[i], ss_output);
      BOOST_CHECK(  
        ss_output.str() == boost::lexical_cast<std::string>(pos_cases[i]));   
      ss_output.str("");
    }
}
