from behave import *

from hamcrest import assert_that, equal_to # Provides explict results of what was expected
import sys
from queue import Queue
sys.path.insert(0, "../../../ADTs")
from Calculators import LowFuelCalc  # noqa E402 (linting exemption)

# Given that this is a unit test, everything will actually occur in the last step.
# This behave test is a proof of concept before using behave with integration testing.
@given('fuel domain is running')
def step_impl(context):
    pass


@when('low fuel receives negative fuel')
def step_impl(context):
    pass


@then('low fuel should return an error code')
def step_assert(context):
    context = LowFuelCalc(5)
    lowfuel = Queue()
    lowfuel.put([1, -1])
    assert_that(context.lowFuelAlert(lowfuel), equal_to(-1))
