"""@package docstring
File used to unit test the fuel gauge functionality

@author Matthew Hendrickson, Nicholas Bishop
@version 0.1
@date 2022-07-21
@copyright Copyright (c) 2022
"""
import sys
sys.path.insert(0, "../ADTs")
from Calculators import FuelConsump  # noqa E402 (linting exemption)


def test_stopflag():
    """Test Consume fuel stop flag

    Test that the stop_flag returns a negative value if the stop flag is raised
    """
    test_gauge = FuelConsump(10, 8, 0.5)
    assert test_gauge.consumeFuel(1) == (-1, -1)


def test_consumeFuel():
    """Test Consume fuel returning empty tank

    Test that will check if consumeFuel returns zero if tank is empty
    """
    test_gauge = FuelConsump(10, 0, 0.5)
    assert test_gauge.consumeFuel(0) == (0, 10)


def test_NormalValue():
    """Test Consume fuel returning smaller amount of fuel

    Test that will check to see if the consumeFuel is consuming fuel after
    the functions runs.
    """
    test_gauge = FuelConsump(10, 1.5, 0.5)
    assert test_gauge.consumeFuel(0) == (1.0, 9.0)


def test_NegValue():
    """Test Consume fuel negative input values

    Test that will check to see if the consumeFuel will return a
    error code when negative values are inputted
    """
    test_gauge = FuelConsump(-10, -1.5, 0.5)
    assert test_gauge.consumeFuel(0) == (-1, -1)


def test_NoneValue():
    """Test Consume fuel Null values

    Test that will check to see if the consumeFuel can handle None/Null
    values as an input and return an error code
    """
    test_gauge = FuelConsump(None, None, None)
    assert test_gauge.consumeFuel(0) == (-1, -1)
