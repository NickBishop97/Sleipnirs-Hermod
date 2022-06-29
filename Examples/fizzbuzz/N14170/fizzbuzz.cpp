// import necessary libraries
#include <iostream>
#include <string>
#include <sstream>
#include <typeinfo>
#include <vector>

// import boost framework
#define BOOST_TEST_MODULE myMain
#include <boost/test/included/unit_test.hpp>
#define BOOST_TEST_DYN_LINK

using namespace std;

/*
function that takes an int input and outputs a string output
if number is divisible by 3, return Fizz
if number is divisible by 5, return Buzz
if number is divisible by both 3 or 5, return FizzBuzz
if number is divisible by neither 3 or 5, return input as string
*/
string returnFizzBuzz(int n)
{
    // test for the four different scenarios
    bool test3 = (n % 3 == 0) && (n % 5 != 0);
    bool test5 = (n % 3 != 0) && (n % 5 == 0);
    bool test35 = (n % 3 == 0) && (n % 5 == 0);
    bool testN = (n % 3 != 0) && (n % 5 != 0);

    // use stringstream to process input
    stringstream ss;
    string num_to_str;

    // convert integer input to string variable
    ss << n;
    ss >> num_to_str;

    // test the integer and output accordingly
    if (test3 == true ) { return "Fizz"; }
    else if (test5 == true ) { return "Buzz"; }
    else if (test35 == true) { return "FizzBuzz"; }
    else if (testN == true ) { return num_to_str; }
}

BOOST_AUTO_TEST_SUITE()

BOOST_AUTO_TEST_CASE(fizzbuzz_test)
{
    cout << endl;

    // create list of cases
    vector<int> tests;
    vector<string> expected;

    tests.push_back(3);
    expected.push_back("Fizz");

    tests.push_back(5);
    expected.push_back("Buzz");

    tests.push_back(15);
    expected.push_back("FizzBuzz");

    tests.push_back(2);
    expected.push_back("2");

    tests.push_back(1);
    expected.push_back("1");

    tests.push_back(0);
    expected.push_back("FizzBuzz");

    tests.push_back(12);
    expected.push_back("Fizz");

    tests.push_back(20);
    expected.push_back("Buzz");

    tests.push_back(30);
    expected.push_back("FizzBuzz");

    // end index
    int end_index = tests.size();

    // run tests
    for (int i = 0; i < end_index; i++)
    {
        // get output values
        int test_res = tests.at(i);
        string expected_res = expected.at(i);
        string actual_res = returnFizzBuzz(test_res);

        // convert test integer to string
        stringstream processor;
        string test_out;
        processor << test_res;
        processor >> test_out;

        // print results of testing
        cout << "Now testing for input:     " + test_out << endl;
        cout << "Expected output should be: " + expected_res << endl;
        BOOST_CHECK(returnFizzBuzz(test_res) == expected_res);
        cout << "Output was:                " + actual_res << endl;
        if (actual_res == expected_res) { cout << "Test was successful!" << endl; }
        else { cout << "Test failed..." << endl; }
        cout << endl;
    }
}

BOOST_AUTO_TEST_SUITE_END()