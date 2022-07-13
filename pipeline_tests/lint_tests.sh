#! /bin/bash

echo "====================================="
echo "=  Starting lint on Vehicle-Python  ="
echo "====================================="
flake8 Vehicle-Python/ADTs --max-line-length 130
flake8 Vehicle-Python/Publishers --max-line-length 130
flake8 Vehicle-Python/PubSubs --max-line-length 130
flake8 Vehicle-Python/Pytests --max-line-length 130
flake8 Vehicle-Python/Subscribers --max-line-length 130

echo "=================================="
echo "=  Starting lint on Vehicle-C++  ="
echo "=================================="
cd Vehicle-C++/Vehicle
sh cxxlint_test.sh ./src/
doxygen Doxyfile
cd -