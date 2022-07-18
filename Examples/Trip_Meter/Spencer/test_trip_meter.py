from TripMeter import DashBoard

CONST_INIT_VALUE = 0.0
CONST_NEW_VALUE = 25.0
CONST_DIFF_VALUE = 15.0
CONST_TIME_TRUE_VALUE = 2.0
CONST_TIME_FALSE_VALUE = 1.99

# Verify that inputed/current tripData displays properly
# for current trip
def test_trip1_input():
    dashboard = DashBoard()
    # Assign value to currentTrip, which should be trip1
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_NEW_VALUE)
    # Get value from trip1 as a temp object
    temp = dashboard.tripMeter.trip1.getTripSpeed()
    # Verify that value of trip1 was assigned to by currentTrip
    assert temp == CONST_NEW_VALUE


# Verify that tripData works when switching to trip2
# Tests basic switching from trip1 to trip2
# Tests basic input for trip2
def test_trip2_input():
    dashboard = DashBoard()
    # Assign to trip1 new value to assert it is not init compared to trip2
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_NEW_VALUE)
    # Switch current trip to trip2
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    # Assign to trip2 a different value to assert
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_DIFF_VALUE)
    # Get value from trip2 as a temp object
    temp = dashboard.tripMeter.trip2.getTripSpeed()
    # Verify that value of trip2 was assigned to by currentTrip
    assert temp == CONST_DIFF_VALUE


# Verify that switching from trip2 to trip1 works
# Asserting that trip1 data is current trip
def test_trip2_switchTo1():
    dashboard = DashBoard()
    # Assign to trip1 new value to assert it is not init compared to trip2
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_NEW_VALUE)
    # Switch current trip to trip2
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    # Assign to trip2 a different value to assert
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_DIFF_VALUE)
    # Switch current trip2 to trip1
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    # Get value from trip1 as a temp object
    temp = dashboard.tripMeter.getCurrentTrip().getTripSpeed()
    # Verify that value of currentTrip new value given to trip1
    assert temp == CONST_NEW_VALUE


# Verify that switching multiple times maintains data in trip1 versus trip2
# Asserting that final switch data is the current trip
def test_multi_switch():
    dashboard = DashBoard()
    # Assign to trip1 new value to assert it is not init compared to trip2
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_NEW_VALUE)
    # Switch current trip to trip2
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    # Assign to trip2 a different value to assert
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_DIFF_VALUE)
    # Switch current trip2 to trip1
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    # Switch current trip1 to trip2
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    # Get value from trip2 as a temp object
    temp = dashboard.tripMeter.getCurrentTrip().getTripSpeed()
    # Verify that value of currentTrip diff value given to trip2
    assert temp == CONST_DIFF_VALUE


# Verify that trip1 data resets to initial values
def test_trip1_reset():
    dashboard = DashBoard()
    # Assign current trip, trip1, new value
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_NEW_VALUE)
    # Reset current trip, resetting trip1
    dashboard.tripMeter.button.setLongPress(True)
    dashboard.tripMeter.isPressed()
    # Get value from trip1 as a temp object
    temp = dashboard.tripMeter.getCurrentTrip().getTripSpeed()
    # Verify that value of currentTrip diff value given to trip2
    assert temp == CONST_INIT_VALUE

# Verify that trip2 data resets to initial values
def test_trip2_reset():
    dashboard = DashBoard()
    # Assign current trip, trip1, new value
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_NEW_VALUE)
    # Switch from trip1 to trip2
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    # Assign current trip, trip2, different value
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_DIFF_VALUE)
    # Reset current trip, resetting trip2
    dashboard.tripMeter.button.setLongPress(True)
    dashboard.tripMeter.isPressed()
    # Switch back to trip1
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    # Get value from currentTrip, trip1, as a temp object
    temp = dashboard.tripMeter.getCurrentTrip().getTripSpeed()
    # Verify that value of currentTrip, trip1, has new value, not reset
    assert temp == CONST_NEW_VALUE


# Verify that trip2 data reset does not affect trip1 data
def test_clean_reset():
    dashboard = DashBoard()
    # Switch from trip1 to trip2
    dashboard.tripMeter.button.setLongPress(True)
    dashboard.tripMeter.isPressed()
    # Assign current trip, trip2, new value
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_NEW_VALUE)
    # Reset current trip, resetting trip2
    dashboard.tripMeter.button.setLongPress(True)
    dashboard.tripMeter.isPressed()
    # Get value from trip2 as a temp object
    temp = dashboard.tripMeter.getCurrentTrip().getTripSpeed()
    # Verify that value of currentTrip diff value given to trip2
    assert temp == CONST_INIT_VALUE


# Verify that time is true when over two
def test_time_true():
    dashboard = DashBoard()
    # Assign current trip, trip1, new time value
    dashboard.tripMeter.getCurrentTrip().setTripTime(CONST_TIME_TRUE_VALUE)
    # Get bool of isTime from currentTrip
    temp = dashboard.tripMeter.isTime(dashboard.tripMeter.getCurrentTrip())
    # Verify that Time of currentTrip returns True
    assert temp == True

# Verify that time is false when time is close but not two
def test_time_false():
    dashboard = DashBoard()
    # Assign current trip, trip1, new time value
    dashboard.tripMeter.getCurrentTrip().setTripTime(CONST_TIME_FALSE_VALUE)
    # Get bool of isTime from currentTrip
    temp = dashboard.tripMeter.isTime(dashboard.tripMeter.getCurrentTrip())
    # Verify that Time of currentTrip returns False
    assert temp == False
