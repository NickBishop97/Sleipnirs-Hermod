#! /bin/bash

set -e

echo ""
echo "================================================"
echo "Starting unit tests for Vehicle-Python project..."
echo "================================================"
echo ""
cp Vehicle-Python/Pytests/* Vehicle-Python/ADTs
cd Vehicle-Python/ADTs
mkdir coverage
pytest ./
pytest --cov=./ > coverage/ADT_cov_report.txt
cd -

# echo ""
# echo "========================================="
# echo "Starting unit tests for Lemuel Example..."
# echo "========================================="
# echo ""
# cd Examples/Trip_Meter/lemuel
# pytest
# cd -

echo ""
echo "==========================================="
echo "Starting unit tests for Spencer Example..."
echo "==========================================="
echo ""
cd Examples/Trip_Meter/Spencer
pytest
cd -

echo ""
echo "========================================"
echo "Starting unit tests for Nick Example..."
echo "========================================"
echo ""
cd Examples/Trip_Meter/Nick
pytest
cd -

# echo ""
# echo "========================================"
# echo "Starting unit tests for Cole Example..."
# echo "========================================"
# echo ""
# cd Examples/Trip_Meter/Cole
# pytest
# cd -

echo ""
echo "==========================================="
echo "Starting unit tests for Maxwell Example..."
echo "==========================================="
echo ""
# cd Examples/Trip_Meter/N13853
# pytest
# cd -

# Test for pytest/robotframework example HelloWorld
#cd Examples/Python/HelloWorld
#robot *.robot
#cd -
