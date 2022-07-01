#include "Calculations.cpp"
#include <iomanip>

int main()
{
    Calculations MPG;
    MPG.mpg(0.45, 0.34);
    MPG.mpg(0.70, 0);
    MPG.mpg(0, 0.23);
    MPG.mpg(-0.45, 0);
    MPG.mpg(0, -0.50);
    MPG.mpg(0,0);

    for(int i = 0; i < 6; ++i)
    {
        std::cout << std::fixed << std::setprecision(2) << MPG.get_MPG(i) << std::endl;
    }
}