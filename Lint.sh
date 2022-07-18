#! /bin/bash

#Fail if any command exit with error.
#set -e

#exits if no directory is given as an arg
#string=$1
# if ((${#string} <= 0));
#if [ -z $string ] ;
#then
#    echo No dir arg given
#    exit 1
#fi

LPUR='\033[1;35m'
NC='\033[0m' # No Color

# Runs cppcheck on all files within this files structure
echo
echo "############ Linting C++ Dir ##############"
echo
cppcheck --quiet --enable=all --language=c++ --suppress=missingIncludeSystem --suppress=unusedFunction ./Vehicle-C++/Vehicle/src/
echo -e "${LPUR}C++ LINTING COMPLETE${NC}"
echo
echo "############ Linting Python Dir ##############"
echo
flake8 --ignore=E501,F401,E402,F403,F811 ./Vehicle-Python/
echo -e "${LPUR}Python LINTING COMPLETE${NC}"