import sys

sys.path.insert(0, "../ADTs")
from Calculators import LowFuelCalc  # noqa E402 (linting exemption)


# There is enough fuel
def test_enough_fuel():
    f = LowFuelCalc(5)
    f.lowFuelAlert(10)
    assert f.lowFuelAlertFlag == 0


# Fuel is low
def test_low_fuel():
    f = LowFuelCalc(5)
    f.lowFuelAlert(2)
    assert f.lowFuelAlertFlag == 1


# Fuel is at threshold but not low
def test_on_mark_fuel():
    f = LowFuelCalc(5)
    f.lowFuelAlert(5)
    assert f.lowFuelAlertFlag == 0


# Fuel is empty
def test_zero_fuel():
    f = LowFuelCalc(5)
    f.lowFuelAlert(0)
    assert f.lowFuelAlertFlag == 1


# Fuel is negative should result in low fuel alert
def test_negative_fuel():
    f = LowFuelCalc(5)
    f.lowFuelAlert(-1.0)
    assert f.lowFuelAlertFlag == 1


# Fuel capacity is negative, then send an error
def test_negative_capacity():
    f = LowFuelCalc(-6)
    f.lowFuelAlert(20)
    assert f.lowFuelAlertFlag == -1
