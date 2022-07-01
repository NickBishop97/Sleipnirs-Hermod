// import necessary libraries
#include <iostream>
#include <string>
#include <vector>

// import boost framework
#define BOOST_TEST_MODULE myMain
#include <boost/test/included/unit_test.hpp>
#define BOOST_TEST_DYN_LINK

using namespace std;


class CalculatorClass
{     
    public:
      double milesTraveled;
      double fuelSpent;
      double fuelRemaining;
      //void addEmptySpaces(int method);
      //double roundThis(double target);
      //void titlefy(string message, char border, char corner);
      static double returnMilesPerGallon(double miles_traveled, double fuel_spent);
      static double returnMilesRemaining(double fuel_remaining, double mpg);
};



/***********************************
Add a certain amount of empty spaces
***********************************/
//void addEmptySpaces(int amount)
//{
//    for (int i = 0; i < amount; i++) {cout << endl;}
//}

/*****************************
Present string in a flashy way
*****************************/
//void titlefy(string message, char border, char corner)
//{
    // get size of line
//    int line_length = message.size();
    // Upper Left Corner
//    cout << corner << border;
    // Upper Border
//    for (int i = 0; i < line_length; i++) {cout << border;}
    // Upper Right Corner
//    cout << border << corner;
//    cout << endl;
    // Message With Side Borders
//    cout << "| " << message << " |" << endl;
    // Lower Left Corner
//    cout << corner << border;
    // Lower Border
//    for (int i = 0; i < line_length; i++) {cout << border;}
    // Lower Right Corner
//    cout << border << corner;
//    cout << endl;
//}

/***********************************
Round a double to two decimal places
***********************************/
double roundThis(double target)
{
    double value = (int)(target * 100 + .5);
    return (float)value / 100;
}



/*************************************************************
Return miles per gallon using the amount of fuel spent and the
miles that were traveled.
*************************************************************/
double CalculatorClass::returnMilesPerGallon(double miles_traveled, double fuel_spent)
{
    if (fuel_spent <= 0) {return 0.0;}
    else
    {
        double fuel_spent_gal = fuel_spent * 0.264172;
        return miles_traveled / fuel_spent_gal;
    }
}


/************************************************************
Return the miles that remain until refuel is needed using the
miles per gallon and the fuel that is remaining
************************************************************/
double CalculatorClass::returnMilesRemaining(double fuel_remaining, double mpg)
{
    double fuel_remaining_gal = fuel_remaining * 0.264172;
    return fuel_remaining_gal * mpg;
}



/******************************
Test Suite for Calculator Class
******************************/
BOOST_AUTO_TEST_SUITE()

// Test the Miles Per Gallon function
BOOST_AUTO_TEST_CASE(retunMilesPerGallon_test)
{

    CalculatorClass test1;

    cout << "TEST #1" << endl;
    double actual = roundThis(test1.returnMilesPerGallon(70.0, 0.0));
    cout << "---------------------" << endl;
    cout << "Miles Traveled : 70.0" << endl;
    cout << "Fuel Spent     : 0.0" << endl;
    cout << "Expected       : 0.0" << endl;
    BOOST_CHECK_CLOSE(actual, 0.0, 0.0001f);
    cout << "Results        : " + std::to_string(actual) << endl;
    cout << "---------------------" << endl;
    // print if the test succeeded or failed
    if (roundThis(0.0) == roundThis(actual)) {cout << "Test was successful!" << endl;}
    else {cout << "Test failed..." << endl;}
    cout << endl;
    cout << endl;
    
    cout << "TEST #2" << endl;
    actual = roundThis(test1.returnMilesPerGallon(0.0, 50.0));
    cout << "---------------------" << endl;
    cout << "Miles Traveled : 0.0" << endl;
    cout << "Fuel Spent     : 50.0" << endl;
    cout << "Expected       : 0.0" << endl;
    BOOST_CHECK_CLOSE(actual, 0.0, 0.0001f);
    cout << "Results        : " + std::to_string(actual) << endl;
    cout << "---------------------" << endl;
    // print if the test succeeded or failed
    if (roundThis(0.0) == roundThis(actual)) {cout << "Test was successful!" << endl;}
    else {cout << "Test failed..." << endl;}
    cout << endl;
    cout << endl;
    /*
    // test data list
    vector<double> given_miles_traveled;
    vector<double> given_fuel_spent;
    vector<double> expected;

    // test 1
    given_miles_traveled.push_back(70.0);
    given_fuel_spent.push_back(50.0);
    expected.push_back(5.30);

    // test 2
    given_miles_traveled.push_back(0.0);
    given_fuel_spent.push_back(50.0);
    expected.push_back(0.0);

    // test 3
    given_miles_traveled.push_back(70.0);
    given_fuel_spent.push_back(0.0);
    expected.push_back(0.0);

    // test 4
    given_miles_traveled.push_back(50.0);
    given_fuel_spent.push_back(50.0);
    expected.push_back(3.790000);

    // test 5
    given_miles_traveled.push_back(50.0);
    given_fuel_spent.push_back(70.0);
    expected.push_back(2.700000);

    titlefy("Now Running Tests for Miles Per Gallon", '=', '#');
    cout << endl;

    // run tests
    for (int i = 0; i < expected.size(); i++)
    {
        // get actual result
        double actual = roundThis(returnMilesPerGallon(given_miles_traveled.at(i), given_fuel_spent.at(i)));

        // get output value table
        cout << "TEST #" + std::to_string(i + 1) << endl;
        cout << "---------------------" << endl;
        cout << "Miles Traveled : " + std::to_string(given_miles_traveled.at(i)) << setprecision(2) << endl;
        cout << "Fuel Spent     : " + std::to_string(given_fuel_spent.at(i)) << setprecision(2) << endl;
        cout << "Expected       : " + std::to_string(expected.at(i)) << setprecision(2) << endl;
        BOOST_CHECK_CLOSE(actual, expected.at(i), 0.0001f);
        cout << "Results        : " + std::to_string(actual) << endl;
        cout << "---------------------" << endl;

        // print if the test succeeded or failed
        if (roundThis(expected.at(i)) == roundThis(actual)) {cout << "Test was successful!" << endl;}
        else {cout << "Test failed..." << endl;}
        addEmptySpaces(2);
        
    }
    */
    
}

BOOST_AUTO_TEST_SUITE_END()