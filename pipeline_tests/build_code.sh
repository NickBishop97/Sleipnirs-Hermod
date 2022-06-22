#! /bin/bash

echo ""
echo "=========================="
echo "Building Fuel Level Sensor"
echo "=========================="
echo ""

cd fastdds_examples/Fuel
cmake .
make
cd -

echo ""
echo "==============================="
echo "Building Miles Travelled Sensor"
echo "==============================="
echo ""

cd fastdds_examples/Miles
cmake .
make
cd -
