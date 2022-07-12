#! /bin/bash

echo ""
echo "====================================="
echo "=  Starting lint on Vehicle-Python  ="
echo "====================================="
echo ""
#flake8 Vehicle-Python --max-line-length 130

echo ""
echo "====================================="
echo "=  Starting lint on Lemuel Example  ="
echo "====================================="
echo ""
flake8 Examples/Trip_Meter/N14170 --max-line-length 150

echo ""
echo "======================================"
echo "=  Starting lint on Spencer Example  ="
echo "======================================"
echo ""
flake8 Examples/Trip_Meter/N13823 --max-line-length 150

echo ""
echo "==================================="
echo "=  Starting lint on Nick Example  ="
echo "==================================="
echo ""
flake8 Examples/Trip_Meter/N16743 --max-line-length 150

echo ""
echo "==================================="
echo "=  Starting lint on Cole Example  ="
echo "==================================="
echo ""
flake8 Examples/Trip_Meter/N08066 --max-line-length 150

echo ""
echo "======================================"
echo "=  Starting lint on Maxwell Example  ="
echo "======================================"
echo ""
flake8 Examples/Trip_Meter/N13853 --max-line-length 150

echo ""
echo "=================================="
echo "=  Starting lint on Vehicle-C++  ="
echo "=================================="
echo ""
cd Vehicle-C++/Vehicle
sh cxxlint_test.sh ./src/
doxygen Doxyfile
cd -