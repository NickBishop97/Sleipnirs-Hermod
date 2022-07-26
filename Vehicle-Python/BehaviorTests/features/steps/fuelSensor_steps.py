from behave import *


import sys
sys.path.insert(0, '../../../MessageFormats/Fuel/')
sys.path.insert(0, '../../../ADTs/')
sys.path.insert(1, "../../../Publishers")
import fuelSensor  # noqa E402 (linting exemption)

@given('the Fuel Sensor, Miles Sensor, and Low Fuel is running')
def step_impl(context):
    pass

@when('the Fuel receives negative fuel')
def step_impl(context):
    pass

@then('the Fuel will return an error code')
def step_impl(context):
    pass