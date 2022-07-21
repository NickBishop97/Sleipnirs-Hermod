# Sleipnir's Hermod C++ Implementation

<img src= "../../etc/Team_Image.png" width="100" height="100">

## Section Links

[Hermod - How to Build](#How-to-Build)

[Hermod - How to Run](#How-to-Run)

[Hermod - Documentation](#Documentation)

## How to Build

There are two way of building the C++ Implementation
1. First be in the Vehicle-C++/Vehicle/ directory and run `cmake . && make` command while in this directory to build the binary files, they will be located in the ./Vehicle-C++/Vehicle/Build/ directory.
2. The second automated way is to run the `./build.sh` script in the top most directory in this git repo, the files will also be located in ./Vehicle-C++/Vehicle/Build/ directory.

## How to Run

There are eight different binary files that you can run, the Big one being TripMeter.
In order to run TripMeter you will need to start four different binaries first, each one will need to be started in its own terminal: **DDSFuelSensor**, **DDSMoving**, **DDSMPG**, **DDSMilesTraveled**. After those have been started in different terminals then you can start up **DDSTripMeter**.

## Documentation

There is auto-generated documentation available for Hermod, to generate it just be in this local directory and run `doxygen Doxyfile` this will generate an html Documentation in ./Build/ directory.