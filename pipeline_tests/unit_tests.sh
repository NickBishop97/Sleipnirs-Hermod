#! /bin/bash

echo "Starting unit tests for MessageBroker project..."
python -m pytest --cov-report=html --cov=src message-broker/broker/
#pytest message-broker/broker/test/
#pytest message-broker/testing-framework/test/
