#! /bin/bash

echo "Starting lint on MessageBroker Project..."
flake8 message-broker
flake8 fastdds_examples
