#! /bin/bash

#Fail if any command exit with error.
set -e

LPUR='\033[1;35m'
NC='\033[0m' # No Color

# Builds and Makes the C++ files
echo
echo "############ Generating Vehicle C++ Docs ##############"
echo
cd Vehicle-C++/Vehicle
doxygen Doxyfile
cd ..
cd ..
echo -e "${LPUR}Doc Files For C++ have been created in ./Vehicle-C++/Vehicle/Build/html/index.html ${NC}"

echo
echo "############ Generating Vehicle Python Docs ##############"
echo
cd Vehicle-Python
doxygen Doxyfile
echo -e "${LPUR}Doc Files For Python have been created in ./Vehicle-Python/Build/html/index.html ${NC}"