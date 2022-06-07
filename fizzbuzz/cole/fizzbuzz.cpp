#include <iostream>
#include <sstream>
#include "fizzbuzz.hpp"


/**
 * Performs FizzBuzz challenge on a given number by testing its divisibility
 *
 * @param num		Current number to have divisibility tested
 * @return 		String containing correct FizzBuzz output for given number
 */
std::string fizzbuzz(int num){
    std::string line = "";
    if(num%3 == 0){	// If num divisible by 3 then add Fizz to output
        line = line + "Fizz";
    }
    if(num%5 == 0){	// If num divisible by 5 then add Buzz to output
        line = line + "Buzz";
    }
    if(num%3 != 0 && num%5 != 0){	// If num not divisible by either then add num to output
        std::stringstream numString;
        numString << num;
        line = line + numString.str();
    }

    return line;
}


/**
 * Does a run of FizzBuzz for consecutive numbers within a given range
 *
 * @param start		First number in range of FizzBuzz numbers
 * @param end		Last number in range of FizzBuzz numbers
 * @return 		Vector containing all output strings from FizzBuzz run
 */
std::vector<std::string> startFizz(int start, int end){
    std::vector<std::string> fizzOut;
    for(int i=start; i<=end; i++){	// loop through each value in range
        fizzOut.push_back(fizzbuzz(i));		// Place received string in vector
    }
    return fizzOut;
}
