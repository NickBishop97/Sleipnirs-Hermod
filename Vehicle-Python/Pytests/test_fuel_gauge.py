"""@package docstring
File used to unit test the fuel gauge functionality
"""
import sys
sys.path.insert(0, "../ADTs")
from Calculators import FuelConsump  # noqa E402 (linting exemption)


def test_base_case():
    """Test fuel gauge with base data values

    The expected value should be 50.0 since we feed the maximum amount
    of fuel to be 30.0 and the remaining amount of fuel to be 15.0
    """
    test_gauge = FuelConsump(30.0, 15.0)
    print("Expected: 50.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 50.0


def test_zero_over_full():
    """Test fuel gauge with zero fuel remaining

    The expected value should be 0.0 since we feed the maximum amount
    of fuel to be 30.0 and the remaining amount of fuel to be 0.0
    """
    test_gauge = FuelConsump(30.0, 0)
    print("Expected: 0.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 0.0


def test_zero_over_zero():
    """Test fuel gauge with zero fuel remaining and a maximum capacity of zero

    The expected value should be 0.0 since we feed the maximum amount
    of fuel to be 0.0 and the remaining amount of fuel to be 0.0
    """
    test_gauge = FuelConsump(0.0, 0.0)
    print("Expected: 0.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 0.0


def test_negative_over_full():
    """Test fuel gauge with a negative amount of fuel

    The expected value should be 0.0 since we feed the maximum amount
    of fuel to be 30.0 and the remaining amount of fuel is negative.
    The program automatically sets the fuel remaining to be zero.
    """
    test_gauge = FuelConsump(30.0, -15.0)
    print("Expected: 0.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 0.0


def test_side_case():
    """Test fuel gauge with secondary values

    The expected value should be 86.0 since we feed the maximum amount
    of fuel to be 30.0 and the remaining amount of fuel to be 25.8
    """
    test_gauge = FuelConsump(30.0, 25.8)
    print("Expected: 86.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 86.0


def test_half_over_zero():
    """Test fuel gauge with zero maximum fuel capacity

    The expected value should be 0.0 since we feed the maximum amount
    of fuel to be 0.0
    """
    test_gauge = FuelConsump(0.0, 30.0)
    print("Expected: 0.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 0.0


def test_extra_over_full():
    """Test fuel gauge with fuel remaining over the maximum

    The expected value should be 100.0 since the amount of fuel remaining
    is larger than the maximum amount of fuel
    """
    test_gauge = FuelConsump(30.0, 45.0)
    print("Expected: 100.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 100.0


def test_full_over_full():
    """Test fuel gauge with a fuel tank

    The expected value should be 100.0 since the value of teh maximum amount of
    fuel and the fuel remaining are the same.
    """
    test_gauge = FuelConsump(30.0, 30.0)
    print("Expected: 100.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 100.0


def test_full_over_negative():
    """Test fuel gauge with negative maximum capacity of fuel

    The expected value should be 0.0 since the maximum capacity of fuel is set to zero.
    The maximum capacity would be set to 0.0
    """
    test_gauge = FuelConsump(-15.0, 30.0)
    print("Expected: 0.0")
    print("Actual Result: " + str(test_gauge.calculateFuelPercentage()))
    assert test_gauge.calculateFuelPercentage() == 0.0


test_base_case()
print('')
test_zero_over_full()
print('')
test_zero_over_zero()
print('')
test_negative_over_full()
print('')
test_side_case()
print('')
test_half_over_zero()
print('')
test_extra_over_full()
print('')
test_full_over_full()
print('')
test_full_over_negative()
