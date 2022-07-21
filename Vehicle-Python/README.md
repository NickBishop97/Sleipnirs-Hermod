# Sleipnir's Hermod Python Implementation

<img src= "../etc/Team_Image.png" width="100" height="100">

## Section Links

[Hermod - How to Build](#How-to-Build)

[Hermod - How to Run](#How-to-Run)

[Hermod - Documentation](#Documentation)

## How to Build

To build the .so file needed, run the `./build.sh` script in the top most directory in this git repo. This will build all the necessary .so files in order to run the Python FastDDS implementation.

## How to Run

All the python files that can be run will be located in these directories: **./PubSubs**, **./Publishers**, and **./Subscribers**. Each python file can be run with the command `python3 <name of file>.py`. Each py file should be run in its own terminal.

## Documentation

At this moment most of the python Implementation isn't documented but you are still welcome to Generate the files and look at what is documented.

- Local Generation

    There is auto-generated documentation available for Hermod, to generate it just be in this local directory and run `doxygen Doxyfile` this will generate an html Documentation in ./Build/ directory.

- Top Directory Generation

    In order to build the documentation in the top directory there is a doc.sh file provided all you have to do is run the command `./doc.sh` and it will be generated in the the ./Vehicle-Python/Build/ directory.