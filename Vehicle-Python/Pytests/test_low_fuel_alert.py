import sys

sys.path.insert(0, "../ADTs")

from Calculators import LowFuel

# There is enough fuel
def test_enough_fuel(): 
    f = LowFuel(5)
    f.lowFuelAlert(10)
    assert f.lowFuelAlertFlag == 0

# Fuel is low
def test_low_fuel(): 
    f = LowFuel(5)
    f.lowFuelAlert(2)
    assert f.lowFuelAlertFlag == 1

# Fuel is at threshold but not low
def test_on_mark_fuel(): 
    f = LowFuel(5)
    f.lowFuelAlert(5)
    assert f.lowFuelAlertFlag == 0

# Fuel is empty
def test_zero_fuel(): 
    f = LowFuel(5)
    f.lowFuelAlert(0)
    assert f.lowFuelAlertFlag == 1

# Fuel is negative should result an error code of -1
def test_negative_fuel(): 
    f = LowFuel(5)
    f.lowFuelAlert(-1.0)
    assert f.lowFuelAlertFlag == -1