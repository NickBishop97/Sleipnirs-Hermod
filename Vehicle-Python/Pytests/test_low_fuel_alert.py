"""@package docstring
File used to unit test the low fuel alert of the vehicle. If the amount of current fuel
is less than or equal to the established threshold, then the alarm is triggered. Else
if the amount of current fuel is greater than the threshold, then the alarm is not
triggered.
"""
from queue import Queue
import sys
sys.path.insert(0, "../ADTs")
from Calculators import LowFuelCalc  # noqa E402 (linting exemption)


# There is enough fuel
def test_enough_fuel():
    """Test to see if the system indicates that there is enough fuel

    The expected value should be 0 since the threshold is set to 5 and the amount of
    current fuel is set to 10, thus not triggering the alarm.
    """
    f = LowFuelCalc(5)
    lowfuel = Queue()
    lowfuel.put([1, 10])
    f.lowFuelAlert(lowfuel)
    assert f.getlowFuelAlertFlag() == 0


# Fuel is low
def test_low_fuel():
    """Test to see if the system indicates that the amount of fuel is low

    The expected value should be 1 since the threshh hold is set to 5 and the amount of
    current fuel is set to 2, thus triggering the alarm.
    """
    f = LowFuelCalc(5)
    f.lowFuelAlert(2)
    assert f.lowFuelAlertFlag == 1


# Fuel is at threshold but not low
def test_on_mark_fuel():
    """Test to see if the system indicates that the amount of fuel remaining is right on
    the threshold

    The expected value should be 0 since the threshold is set to 5 and the amount of fuel
    remaining is set to 10, thus not triggering the alarm.
    """
    f = LowFuelCalc(5)
    f.lowFuelAlert(5)
    assert f.lowFuelAlertFlag == 0


# Fuel is empty
def test_zero_fuel():
    """Test to see if the system indicates that there is no fuel

    The expected value should be 1 since the threshold is set to 5 and the amount of fuel
    remaining is set to 0, thus triggering the alarm.
    """
    f = LowFuelCalc(5)
    f.lowFuelAlert(0)
    assert f.lowFuelAlertFlag == 1


# Fuel is negative should result in low fuel alert
def test_negative_fuel():
    """Test to see if the system indicates that there is negative fuel

    The expected value should be 1 since the threshold is set to 5 and the amount of fuel
    remaining is set to -1, thus triggering the alarm.
    """
    f = LowFuelCalc(5)
    f.lowFuelAlert(-1.0)
    assert f.lowFuelAlertFlag == 1


# Fuel capacity is negative, then send an error
def test_negative_capacity():
    """Test to see if the system indicates that the capacity amount if negative

    The expected value should be 1 since the threshold is set to -6 and the amount of fuel
    remaining is set to 20, thus triggering the amount.
    """
    f = LowFuelCalc(-6)
    f.lowFuelAlert(20)
    assert f.lowFuelAlertFlag == -1
