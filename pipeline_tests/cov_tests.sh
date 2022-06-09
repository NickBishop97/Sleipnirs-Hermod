#! /bin/bash

echo "Starting coverage tests for MessageBroker project..."
coverage run ../message-broker/broker/test/
coverage report -m
coverage run ../message-broker/testing-framework/test/
coverage report -m
