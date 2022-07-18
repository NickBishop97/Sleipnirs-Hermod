cmake_minimum_required(VERSION 3.12.4)

if(NOT CMAKE_VERSION VERSION_LESS 3.0)
    cmake_policy(SET CMP0048 NEW)
endif()

project(DDSVehicle)
SET(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${DDSVehicle_SOURCE_DIR}/Build)

# Find requirements
if(NOT fastcdr_FOUND)
    find_package(fastcdr REQUIRED)
endif()

if(NOT fastrtps_FOUND)
    find_package(fastrtps REQUIRED)
endif()

# Set C++11
include(CheckCXXCompilerFlag)
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_COMPILER_IS_CLANG OR
        CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    check_cxx_compiler_flag(-std=c++11 SUPPORTS_CXX11)
    if(SUPPORTS_CXX11)
        add_compile_options(-std=c++11)
    else()
        message(FATAL_ERROR "Compiler doesn't support C++11")
    endif()
endif()
message(STATUS "Configuring Fuel publisher/subscriber...")
file(GLOB DDS_FUEL_SOURCES_CXX "src/Fuel/*.cxx")
add_executable(DDSFuelSensor src/Pubs/FuelSensor.cpp ${DDS_FUEL_SOURCES_CXX})
target_link_libraries(DDSFuelSensor fastrtps fastcdr)
add_executable(DDSFuelGauge src/Subs/FuelGauge.cpp ${DDS_FUEL_SOURCES_CXX})
target_link_libraries(DDSFuelGauge fastrtps fastcdr)

message(STATUS "Configuring Moving publisher/subscriber...")
file(GLOB DDS_MOVE_SOURCES_CXX "src/Moving/*.cxx")
add_executable(DDSMoving src/PubSub/Moving.cpp ${DDS_MOVE_SOURCES_CXX})
target_link_libraries(DDSMoving fastrtps fastcdr)

message(STATUS "Configuring Miles publisher/subscriber...")
file(GLOB DDS_MILES_SOURCES_CXX "src/Miles/*.cxx")
add_executable(DDSMilesTraveled src/PubSub/MilesTraveled.cpp ${DDS_MILES_SOURCES_CXX})
target_link_libraries(DDSMilesTraveled fastrtps fastcdr)
add_executable(DDSDistanceDisplay src/Subs/DisDisplay.cpp ${DDS_MILES_SOURCES_CXX})
target_link_libraries(DDSDistanceDisplay fastrtps fastcdr)

message(STATUS "Configuring MPG publisher/subscriber...")
file(GLOB DDS_MPG_SOURCES_CXX "src/MPG/*.cxx")
add_executable(DDSMPG src/PubSub/MpG.cpp ${DDS_MPG_SOURCES_CXX})
target_link_libraries(DDSMPG fastrtps fastcdr)

message(STATUS "Configuring MilesLeft publisher/subscriber...")
file(GLOB DDS_ML_SOURCES_CXX "src/MilesLeft/*.cxx")
add_executable(DDSMilesLeft src/PubSub/MilesLeft.cpp ${DDS_ML_SOURCES_CXX})
target_link_libraries(DDSMilesLeft fastrtps fastcdr)

message(STATUS "Configuring TripMeter publisher/subscriber...")
file(GLOB DDS_TM_SOURCES_CXX "src/TripMeter/*.cxx")
add_executable(DDSTrip src/PubSub/TripMeter.cpp ${DDS_TM_SOURCES_CXX})
target_link_libraries(DDSTrip fastrtps fastcdr)