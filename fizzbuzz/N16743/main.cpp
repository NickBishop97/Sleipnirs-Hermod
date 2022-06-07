#include <iostream>
#include "fizzbuzz.cpp"

using namespace std;

int main()
{
    for(int i = 1; i <= 100; ++i){
        cout << fizzbuzz(i) << endl;
    }
}