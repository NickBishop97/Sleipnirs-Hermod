#! /bin/sh

#Fail if any command exit with error.
set -e

LPUR='\033[1;35m'
NC='\033[0m' # No Color

# Builds and Makes the C++ files
echo
echo "############ Buiding Vehicle C++ ##############"
echo
cd ./Vehicle-C++/Vehicle
cmake .
echo
echo "############ Making Vehicle C++ ##############"
echo
make
cd ..
cd ..
echo

# Builds and Makes the Python files
echo
echo "############ Buiding/Making Vehicle Python ##############"
echo
cd Vehicle-Python/MessageFormats/
echo -e "${LPUR}Building Fuel .so Files ${NC}"
cd ./Fuel
cmake .
make
cd ..
echo
echo -e "${LPUR}Building CLK .so Files ${NC}"
cd ./CLK
cmake .
make
cd ..
echo
echo -e "${LPUR}Building LowFuelAlert .so Files ${NC}"
cd ./LowFuelAlert
cmake .
make
cd ..
echo
echo -e "${LPUR}Building Miles .so Files ${NC}"
cd ./Miles
cmake .
make
cd ..
echo
echo -e "${LPUR}Building MilesToRefuel .so Files ${NC}"
cd ./MilesToRefuel
cmake .
make
cd ..
echo
echo -e "${LPUR}Building MpG .so Files ${NC}"
cd ./MpG
cmake .
make
cd ..
echo
echo -e "${LPUR}Building of Python Files is Complete ${NC}"
echo -e "${LPUR}Binary Files For C++ can be found in ./Vehicle-C++/Vehicle/Build/ ${NC}"
echo