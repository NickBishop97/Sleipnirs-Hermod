#! /bin/bash

#Fail if any command exit with error.
set -e

LPUR='\033[1;35m'
NC='\033[0m' # No Color

echo
echo "############ Auto Formating Python Code ##############"
echo
cd ./Vehicle-Python
find . -name '*.py' -exec autopep8 --in-place --verbose --ignore=E501,F811 '{}' \;
echo
echo -e "${LPUR}AutoFormating Python Files Complete ${NC}"