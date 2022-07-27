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
cmake Fuel/.
cd ./Fuel/ && make
cd ..
echo
echo -e "${LPUR}Building LowFuelAlert .so Files ${NC}"
cmake LowFuelAlert/.
cd ./LowFuelAlert/ && make
cd ..
echo
echo -e "${LPUR}Building Miles .so Files ${NC}"
cmake Miles/.
cd ./Miles/ && make
cd ..
echo
echo -e "${LPUR}Building MilesToRefuel .so Files ${NC}"
cmake MilesToRefuel/.
cd ./MilesToRefuel/ && make
cd ..
echo
echo -e "${LPUR}Building MpG .so Files ${NC}"
cmake MpG/.
cd ./MpG/ && make
cd ..
echo
echo -e "${LPUR}Building of Python Files is Complete ${NC}"
echo -e "${LPUR}Binary Files For C++ can be found in ./Vehicle-C++/Vehicle/Build/ ${NC}"
echo