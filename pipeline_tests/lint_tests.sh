#! /bin/bash

echo "====================================="
echo "=  Starting lint on Vehicle-Python  ="
echo "====================================="
#flake8 Vehicle-Python --max-line-length 130

echo "=================================="
echo "=  Starting lint on Vehicle-C++  ="
echo "=================================="
cd Vehicle-C++/Vehicle
sh cxxlint_test.sh ./src/
doxygen Doxyfile
cd -