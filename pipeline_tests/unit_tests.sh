#! /bin/bash

echo "Starting unit tests for MessageBroker project..."
pytest ../message-broker/broker/test/
pytest ../message-broker/testing-framework/test/
