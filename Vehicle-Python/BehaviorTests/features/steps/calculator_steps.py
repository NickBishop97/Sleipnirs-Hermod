from behave import *

import sys
sys.path.insert(0, '../../../ADTs/')
from Calculators import LowFuelCalc # noqa E402 (linting exemption)

@given('we have fuel domain')
def step_impl():
    LowFuelCalc
    pass

@when('low fuel receives negative fuel')
def step_impl():
    LowFuelCalc.lowFuelAlert(-5)
    pass

@then('low fuel should return an error code')
def step_impl():
    assert LowFuelCalc.lowFuelAlert(-5) == -1