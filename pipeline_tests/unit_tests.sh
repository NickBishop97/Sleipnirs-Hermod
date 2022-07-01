#! /bin/bash

set -e

echo "================================================"
echo "Starting unit tests for Vehicle-Python project..."
echo "================================================"

# Tests for Python Vehicle
pytest Vehicle-Python/Pytests/*

# Tests for testing framework
#cd message-broker/testing-framework
#python -m pytest --cov-report=html --cov=src .
#cd -

# Test for pytest/robotframework example HelloWorld
cd Examples/Python/HelloWorld
robot *.robot
cd -

#pytest message-broker/broker/test/
#pytest message-broker/testing-framework/test/
