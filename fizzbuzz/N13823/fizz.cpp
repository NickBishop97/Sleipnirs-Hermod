#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE


#include <iostream>
#include <string>
#include <vector>
#include <boost/test/unit_test.hpp>

using namespace std;

// Unsigned for postive values only
string fizzBuzz(unsigned int number)
{

    if (number % 15 == 0) 
    {
        return "fizzbuzz";
    }
    else if (number % 3 == 0) 
    {
        return "fizz";
    }
    else if (number % 5 == 0) 
    {
        return "buzz";
    }
    else
    {
        // For later versions, use to_string
        stringstream ss;
        ss << number;
        string str = ss.str();
        return str;
    }

}
// Cases that should produce buzz
BOOST_AUTO_TEST_CASE(buzzTest)
{
    for (int i = 5; i <= 100; i += 5)
    {
        if (i % 3 != 0)
        {
            BOOST_CHECK(fizzBuzz(i) == "buzz");
        }   
    }
   
}

// Cases that should produce fizz
BOOST_AUTO_TEST_CASE(fizzTest)
{
    for (int i = 3; i <= 100; i += 3)
    {
        if (i % 5 != 0)
        {
            BOOST_CHECK(fizzBuzz(i) == "fizz");
        }    
    }
}

// Cases that should produce fizzbuzz
BOOST_AUTO_TEST_CASE(fizzbuzzTest)
{
    for (int i = 15; i <= 100; i += 15)
    {
         BOOST_CHECK(fizzBuzz(i) == "fizzbuzz");
    }  
}

// Cases that should produce none of the above
BOOST_AUTO_TEST_CASE(noneTest)
{
    BOOST_CHECK(fizzBuzz(1) == "1");
    BOOST_CHECK(fizzBuzz(2) == "2");
    BOOST_CHECK(fizzBuzz(4) == "4");
    BOOST_CHECK(fizzBuzz(31) == "31");
    BOOST_CHECK(fizzBuzz(77) == "77");
}
