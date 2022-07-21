#include "fizzbizz.h"
#include <iostream>
#include <sstream>
#include <string>

#include <boost/lexical_cast.hpp>

void fizzbuzz(
    unsigned int lowerLimit, 
    unsigned int upperLimit,
    std::ostream& os){

    assert(lowerLimit > 0 && upperLimit > 0);
    for(unsigned int num = lowerLimit; num <= upperLimit; num++){
        if(num % 15 == 0)
            os << "fizzbuzz";
        else if(num % 3 == 0)
            os << "fizz";
        else if(num % 5 == 0)
            os << "buzz";
        else
            os << num;
    }
    
}
