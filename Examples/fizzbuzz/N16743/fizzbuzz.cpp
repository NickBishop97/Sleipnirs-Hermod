#include <boost/lexical_cast.hpp>

using namespace std;
using namespace boost;

string fizzbuzz(int input)
{
    if(input%3 == 0 && input%5 == 0)
    {
        return "fizzbuzz";
    }
    else if(input%3 == 0)
    {
        return "fizz";
    }
    else if(input%5 == 0)
    {
        return "buzz";
    }
    else
    {
        //converts from a int to a string
        string str = lexical_cast<string>(input);
        return str;
    }
}
