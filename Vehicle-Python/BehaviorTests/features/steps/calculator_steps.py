from behave import *


import sys
sys.path.insert(0, '../../../ADTs/')
from Calculators import LowFuelCalc # noqa E402 (linting exemption)

@given('the Fuel Sensor, Miles Sensor, and MPG is running')
def step_impl():
    # The idea for intergration testing is to have this running 
    # For now, pass in the values into the function to test behave
    pass

@when('the MPG receives negative miles')
def step_impl():
    pass

@then('the MPG will return an error code')
def step_impl():
    assert LowFuelCalc.lowFuelAlert(-1)