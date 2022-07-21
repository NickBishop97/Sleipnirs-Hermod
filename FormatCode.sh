#! /bin/bash

#Fail if any command exit with error.
set -e

LPUR='\033[1;35m'
NC='\033[0m' # No Color

echo
echo "############ Auto Formating Python Code ##############"
echo
cd ./Vehicle-Python
# requires autopep8 through pip3 inorder to run
find . -name '*.py' -exec autopep8 --in-place --ignore=E501,F811 '{}' \;
echo
echo -e "${LPUR}AutoFormating Python Files Complete ${NC}"
echo "############ Auto Formating C++ Code ##############"
echo
cd ../Vehicle-C++/Vehicle/src
find . -name '*.cpp' -exec clang-format -i -style=WebKit '{}' \;
find . -name '*.h' -exec clang-format -i -style=WebKit '{}' \;
echo
echo -e "${LPUR}AutoFormating C++ Files Complete ${NC}"
