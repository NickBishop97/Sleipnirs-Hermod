#! /bin/bash

echo "Starting lint on MessageBroker Project..."
flake8 --max-line-length 99 message-broker
flake8 --max-line-length 99 fastdds_examples
