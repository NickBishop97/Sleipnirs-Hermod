#! /bin/bash

echo "Starting lint on Python section of Vehicle Project..."
flake8 Vehicle-Python --max-line-length 130
