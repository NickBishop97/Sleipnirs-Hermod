# Sleipnir

## Purpose
Summer 2022 Internship Project

Project Hermod is a DDS (Distributed Data Service) that models a DDS that would be used for a car system. It utilizes fastDDS framework to create publishers and subscribers to transmit data via topics in real time. Some of the specific component domain being written for the car system are the following:
    - Fuel Domain (Fuel spent, Fuel remaining, Low fuel alert, Miles per gallon, etc..)
    - Miles Domain (Miles traveled, Miles remaining, Miles per gallon, etc..)
    - Trip Domain (Current trip, Trip time, Avg speed, Avg miles per gallon, etc..)

## Important Info

**Runable Scripts**

- Build.sh (Buids both C++ and Python version of the Code)
- Lint.sh (Will lint both C++ and Python code for any syntax errors) **Requires that cppcheck and flake8 are installed**
- Doc.sh (Will create an HTML Doc of the code for both C++ and Python) **Requires that Doxygen is installed**
- FormatCode.sh (Will auto format the Python Code to Pep8 standards) **Requires that autopep8 is installed**

## FastDDS Setup

1. Getting dependencies
    - **TinyXml2 v9.0.0**
        - Go to a directory that you want to place all of these download files preferably in the "/home/<userID>/<folder>/" location
            - Run these commands in order.
## 

![alt text](https://gitlab.sde.sp.gc1.myngc.com/lts/sleipnir/-/blob/master/ect/Gradle.gif)
