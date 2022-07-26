#!/bin/bash
cd /opt/Fast-DDS-Python/install/fastdds_python_examples/share/fastdds_python_examples/HelloWorld
python3 HelloWorldExample.py  -p publisher & sleep 2; python3 HelloWorldExample.py -p subscriber