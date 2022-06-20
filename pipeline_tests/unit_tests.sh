#! /bin/bash

echo "Starting unit tests for MessageBroker project..."
cd message-broker/broker
python -m pytest --cov-report=html --cov=src .
cd -
#pytest message-broker/broker/test/
#pytest message-broker/testing-framework/test/
