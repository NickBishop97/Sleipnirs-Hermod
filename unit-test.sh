#! /bin/bash

#Fail if any command exit with error.
set -e

LPUR='\033[1;35m'
NC='\033[0m' # No Color

# Runs pytest to unit test code in directory
echo
echo "############ Running Pytest ##############"
echo
cd ./Vehicle-Python/Pytests
pytest --cov-report term-missing --cov=Calculators
echo
echo "############ Running C++ Unit Tests ##############"
cd ../..
cd ./Vehicle-C++/Vehicle/src/Unit_Testing
# Compiling Unit tests
g++ -Wall -fprofile-arcs -ftest-coverage -c ../Calculations.cpp
g++ -Wall -fprofile-arcs -ftest-coverage -c Testing_Main.cpp
g++ -Wall -fprofile-arcs -ftest-coverage *.o -o Main -lboost_unit_test_framework-mt
./Main #--log_level=test_suite
# creating coverage info
lcov -c -d . -o coverage.info 1> /dev/null
# Generating Html coverage report
genhtml coverage.info -o ../../Build/Coverage 1> /dev/null
echo
printf ${LPUR}
gcov Calculations.cpp | head -n 2
echo
echo "Coverage html has been generated in Vehicle-C++/Vehicle/Build/Coverage"
printf ${NC}
rm *.o *.gcda *.gcno *.gcov Main *.info
echo
echo -e "${LPUR}C++ UNIT TESTING COMPLETE${NC}"