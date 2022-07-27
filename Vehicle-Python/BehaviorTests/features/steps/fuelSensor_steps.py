from behave import *

# Currently, unable to import publishers as path includes another path insert,
# which behave is unable to find module
# import sys
# sys.path.insert(0, "../../../Publishers")
# import fuelSensor  # noqa E402 (linting exemption)


@given('the Fuel Sensor is running') # noqa F405 (linting exemption)
def step_impl(context):
    pass


@when('the Fuel Sensor is activated') # noqa F405 (linting exemption)
def step_impl(context):
    pass


@then('the signal will be sent') # noqa F405 (linting exemption)
def step_impl(context):
    pass
