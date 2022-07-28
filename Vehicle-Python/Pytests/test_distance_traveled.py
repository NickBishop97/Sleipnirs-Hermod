"""@package docstring
File used to unit test the distance traveled functionality

@author Nicholas Bishop
@version 0.1
@date 2022-07-21
@copyright Copyright (c) 2022
"""
import sys
from queue import Queue
sys.path.insert(0, "../ADTs")
from Calculators import DistTrav  # noqa E402 (linting exemption)


def test_normal_value():
    """Test distance traveled addmiles

    Tests that the distance given and delta value is added to the total
    """
    d = DistTrav(10, 0)
    d.setDelta(0.5)
    distance = Queue()
    distance.put([1, 10])
    assert d.addMiles(distance) == 10.5


def test_neg_value():
    """Test distance traveled when negative values are inputted

    Tests that the distance traveled is not affected when the distance
    traveled is negative
    """
    d = DistTrav(10, 0)
    d.setDelta(-0.5)
    distance = Queue()
    distance.put([1, 10])
    assert d.addMiles(distance) == 10


def test_init_neg_value():
    """Test distance traveled when initial negative values are inputted

    Tests that the distance traveled is not affected when the distance
    traveled is negative
    """
    d = DistTrav(-1, -0.5)
    distance = Queue()
    distance.put([1, 10])
    assert d.addMiles(distance) == 0


def test_fuelQueue_zerovalue():
    """Test distance traveled when zero are inputted in the fuel Queue

    Tests that the fuel Queue has a value that is greater than zero, if its zero or less
    it will output the same distance traveled as the inputted value.
    """
    d = DistTrav(10, 0)
    d.setDelta(5)
    distance = Queue()
    distance.put([1, 0])
    assert d.addMiles(distance) == 10


def test_fuelQueue_negvalue():
    """Test distance traveled when negative values are inputted in the fuel Queue

    Tests that the fuel Queue has a value that is greater than zero, if its zero or less
    it will output the same distance traveled as the inputted value.
    """
    d = DistTrav(10, 0)
    d.setDelta(5)
    distance = Queue()
    distance.put([1, -1])
    assert d.addMiles(distance) == 10


def test_fuelQueue_empty():
    """Test distance traveled fuel Queue is empty

    Tests that the fuel Queue is empty and outputs current distance.
    """
    d = DistTrav(10, 0)
    d.setDelta(5)
    distance = Queue()
    assert d.addMiles(distance) == 10
