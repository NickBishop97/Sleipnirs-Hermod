#! /bin/bash

echo "================================================"
echo "Starting unit tests for MessageBroker project..."
echo "================================================"

# Tests for message broker
cd message-broker/broker
python -m pytest --cov-report=html --cov=src .
cd -

# Tests for testing framework
cd message-broker/testing-framework
python -m pytest --cov-report=html --cov=src .
cd -

#pytest message-broker/broker/test/
#pytest message-broker/testing-framework/test/
