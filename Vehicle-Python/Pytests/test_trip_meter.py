"""@package docstring
File used to unit test the distance traveled functionality

@author Maxwell Rosales
@version 0.1
@date 2022-07-21
@copyright Copyright (c) 2022
"""
import sys
from queue import Queue

sys.path.insert(0, "../ADTs")
from Calculators import TripCalc  # noqa E402,F403 (linting exemptions)


# ENSURE CONSTRUCTOR MAKES BLANK MEMBER VARIABLES
def test_init():
    """Test for initial conditions

    ENSURE CONSTRUCTOR MAKES BLANK MEMBER VARIABLES
    """

    tripCalc = TripCalc()

    expectedDict = {
        "distance": 0,
        "fuel": 0,
        "time": 0,

        "averageSpeed": 0,
        "MpG": 0,

        "twoHours": False,
        "resetCounterDist": 0,
        "resetCounterFuel": 0,
        "resetCounterTime": 0
    }

    assert tripCalc.getCurrentTripNum() == 0
    assert tripCalc.getTrips()[0] == expectedDict
    assert tripCalc.getTrips()[1] == expectedDict

# ENSURE THAT TIMES LESS THAN 2 HOURS FLIP bool twoHours


def test_update_less_than_2_hours():
    """Test less than two hours of travel

    ENSURE THAT TIMES LESS THAN 2 HOURS FLIP bool twoHours
    """
    tripCalc = TripCalc()

    expectedDict = {
        "distance": 1,
        "fuel": 1,
        "time": 1,

        "averageSpeed": 1,
        "MpG": 1,

        "twoHours": False,
        "resetCounterDist": 0,
        "resetCounterFuel": 0,
        "resetCounterTime": 0
    }
    fuelQueue = Queue()
    fuelQueue.put([1, 1, 1])
    milesQueue = Queue()
    milesQueue.put([1, 1])
    timeQueue = Queue()
    timeQueue.put([1, 1])

    tripCalc.update([milesQueue,
                    fuelQueue,
                    timeQueue
                     ])

    assert tripCalc.getTrips()[0] == expectedDict
    assert tripCalc.getTrips()[1] == expectedDict


# TESTING FOR DIVISION BY ZERO
def test_update_div_by_zero():
    """Test divsion by zero

    TESTING FOR DIVISION BY ZERO in tripcalc
    """
    tripCalc = TripCalc()

    expectedDict = {
        "distance": 0,
        "fuel": 0,
        "time": 0,

        "averageSpeed": -1,
        "MpG": -1,

        "twoHours": False,
        "resetCounterDist": 0,
        "resetCounterFuel": 0,
        "resetCounterTime": 0
    }
    fuelQueue = Queue()
    fuelQueue.put([1, 0, 0])
    milesQueue = Queue()
    milesQueue.put([1, 0])

    timeQueue = Queue()
    timeQueue.put([1, 0])

    tripCalc.update([milesQueue,
                    fuelQueue,
                    timeQueue
                     ])

    assert tripCalc.getTrips()[0] == expectedDict
    assert tripCalc.getTrips()[1] == expectedDict


# ENSURE THAT TIMES EQUAL TO 2 HOURS FLIP bool twoHours
def test_update_equal_to_2_hours():
    """Test for time value equal to 2 hours of travel time

    ENSURE THAT TIMES EQUAL TO 2 HOURS FLIP bool twoHours
    """
    tripCalc = TripCalc()

    expectedDict = {
        "distance": 1,
        "fuel": 1,
        "time": 2,

        "averageSpeed": 0.5,
        "MpG": 1,

        "twoHours": True,
        "resetCounterDist": 0,
        "resetCounterFuel": 0,
        "resetCounterTime": 0
    }
    fuelQueue = Queue()
    fuelQueue.put([1, 1, 1])
    milesQueue = Queue()
    milesQueue.put([1, 1])

    timeQueue = Queue()
    timeQueue.put([1, 2])

    tripCalc.update([milesQueue,
                    fuelQueue,
                    timeQueue
                     ])

    assert tripCalc.getTrips()[0] == expectedDict
    assert tripCalc.getTrips()[1] == expectedDict

# ENSURE THAT TIMES OVER 2 HOURS FLIP bool twoHours


def test_update_greater_than_2_hours():
    """Test for time value equal to 2 hours of travel time

    ENSURE THAT TIMES OVER 2 HOURS FLIP bool twoHours
    """
    tripCalc = TripCalc()

    expectedDict = {
        "distance": 1,
        "fuel": 1,
        "time": 4,

        "averageSpeed": 0.25,
        "MpG": 1,

        "twoHours": True,
        "resetCounterDist": 0,
        "resetCounterFuel": 0,
        "resetCounterTime": 0
    }

    fuelQueue = Queue()
    fuelQueue.put([1, 1, 1])
    milesQueue = Queue()
    milesQueue.put([1, 1])

    timeQueue = Queue()
    timeQueue.put([1, 4])

    tripCalc.update([milesQueue,
                    fuelQueue,
                    timeQueue
                     ])

    assert tripCalc.getTrips()[0] == expectedDict
    assert tripCalc.getTrips()[1] == expectedDict

# WHEN RESETTING A TRIP, ENSURE THAT ONLY ONE TRIP GETS RESET


def test_reset_a_trip():
    """Testing the reset trip

    WHEN RESETTING A TRIP, ENSURE THAT ONLY ONE TRIP GETS RESET
    """
    tripCalc = TripCalc()

    expectedTripOne = {
        "distance": 0,
        "fuel": 0,
        "time": 0,

        "averageSpeed": 0,
        "MpG": 0,

        "twoHours": False,
        "resetCounterDist": 1,
        "resetCounterFuel": 1,
        "resetCounterTime": 4
    }

    expectedTripTwo = {
        "distance": 1,
        "fuel": 1,
        "time": 4,

        "averageSpeed": 0.25,
        "MpG": 1,

        "twoHours": True,
        "resetCounterDist": 0,
        "resetCounterFuel": 0,
        "resetCounterTime": 0
    }

    fuelQueue = Queue()
    fuelQueue.put([1, 1, 1])
    milesQueue = Queue()
    milesQueue.put([1, 1])

    timeQueue = Queue()
    timeQueue.put([1, 4])

    tripCalc.update([milesQueue,
                    fuelQueue,
                    timeQueue
                     ])

    tripCalc.reset(3)

    assert tripCalc.getTrips()[0] == expectedTripOne
    assert tripCalc.getTrips()[1] == expectedTripTwo

# ENSURE THAT THE TRIP NUMBER SWITCHES


def test_reset_switch_trips():
    """Testing the reset switch for the trip counter

    ENSURE THAT THE TRIP NUMBER SWITCHES
    """
    tripCalc = TripCalc()

    assert tripCalc.getCurrentTripNum() == 0
    tripCalc.reset(2)
    assert tripCalc.getCurrentTripNum() == 1

# ENSURES THAT THE RESET COUNTERS WORK AFTER AN UPDATE


def test_reset_counter_offset():
    """Testing rest counter offset

    ENSURES THAT THE RESET COUNTERS WORK AFTER AN UPDATE
    """
    tripCalc = TripCalc()
    previousDist = 1
    previousFuel = 1
    previousTime = 4

    expectedTripOne = {
        "distance": 2 - previousDist,
        "fuel": 2 - previousFuel,
        "time": 5 - previousTime,

        "averageSpeed": (1 / 1),
        "MpG": (1 / 1),

        "twoHours": False,
        "resetCounterDist": previousDist,
        "resetCounterFuel": previousFuel,
        "resetCounterTime": previousTime
    }

    expectedTripTwo = {
        "distance": 2,
        "fuel": 2,
        "time": 5,

        "averageSpeed": (2 / 5),
        "MpG": (2 / 2),

        "twoHours": True,
        "resetCounterDist": 0,
        "resetCounterFuel": 0,
        "resetCounterTime": 0
    }

    fuelQueue = Queue()
    fuelQueue.put([1, 1, 1])
    milesQueue = Queue()
    milesQueue.put([1, 1])

    timeQueue = Queue()
    timeQueue.put([1, 4])

    tripCalc.update([milesQueue,
                    fuelQueue,
                    timeQueue
                     ])

    tripCalc.reset(3)

    fuelQueue.put([2, 2, 0.5])
    milesQueue.put([2, 2])
    timeQueue.put([2, 5])

    tripCalc.update([milesQueue,
                    fuelQueue,
                    timeQueue
                     ])

    assert tripCalc.getTrips()[0] == expectedTripOne
    assert tripCalc.getTrips()[1] == expectedTripTwo
