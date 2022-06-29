#define BOOST_TEST_MODULE FizzbuzzTest
#include <boost/test/included/unit_test.hpp>

#include "fizzbuzz.hpp"
#include <sstream>


/**
 * Reads integers from a given file and stores them in a vector
 * This function is used for the single number test
 *
 * @param inFile	File to be scanned for integers
 * @return		Vetor containing all test integers in file
 */
std::vector<int> readTestCase(std::string inFile){
    std::vector<int> vals;	// Vector to store test ints

    std::ifstream fin(inFile.c_str());		// Open file
    if(!fin.is_open()){				// If file did not open, abort program
        std::cout << "Failed to open " << inFile << ". Exiting..." << std::endl;
        exit(1);
    }

    int testNum;
    while(fin >> testNum){		// Read each int and push onto vector
        vals.push_back(testNum);
    }

    fin.close();	// Close file and return complete test vector
    return vals;
}


/**
 * Boost unit tests for single, random fizzbuzz numbers
 * Verifies FizzBuzz returns the correct value for any input
 */
BOOST_AUTO_TEST_CASE( singleNumTest ){
    // Read text files to get expected valuces for each test
    std::vector<int> fizzTest = readTestCase("fizzTest.txt");		// Contains values expected to be FIZZ
    std::vector<int> buzzTest = readTestCase("buzzTest.txt");		// Contains values expected to be BUZZ
    std::vector<int> fizzBuzzTest = readTestCase("fizzBuzzTest.txt");	// Contains values expected to be FIZZBUZZ
    std::vector<int> noneTest = readTestCase("noneTest.txt");		// Contains values not expected to hit in FizzBuzz

    for(int i=0; i<fizzTest.size(); i++){	// Loop through divisible by 3 numbers and verify Fizz returned
        BOOST_CHECK(fizzbuzz(fizzTest[i]) == "Fizz");
    }
    for(int i=0; i<buzzTest.size(); i++){	// Loop through divisible by 5 numbers and verify Buzz returned
        BOOST_CHECK(fizzbuzz(buzzTest[i]) == "Buzz");
    }
    for(int i=0; i<fizzBuzzTest.size(); i++){	// Loop through divisible by 3 and 5 numbers and verify FizzBuzz returned
        BOOST_CHECK(fizzbuzz(fizzBuzzTest[i]) == "FizzBuzz");
    }
    for(int i=0; i<noneTest.size(); i++){	// Loop through non-value numbers and verify same number returned
        std::stringstream expected;
        expected << noneTest[i];
        BOOST_CHECK(fizzbuzz(noneTest[i]) == expected.str());
    }
}


/**
 * Boost unit tests for a run of numbers
 * Verify correct sequence of Fizz, Buzz, and FizzBuzz is returned
 */
BOOST_AUTO_TEST_CASE(fullRunTest){
    std::vector<std::string> testList = startFizz(1, 100);	// Run FizzBuzz from 1 to 100

    std::ifstream fin("runTest_1-100.txt");	// Read expected values from file
    std::string expected;
    std::vector<std::string> expectList;
    while(fin >> expected){
        expectList.push_back(expected);		// Store expected value
    }
    fin.close();
    
    for(int i=0; i<expectList.size(); i++){		// Compare what FizzBuzz returned to expected vals
        BOOST_CHECK(testList[i] == expectList[i]);
    }
}
