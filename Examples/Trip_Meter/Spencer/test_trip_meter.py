from TripMeter import DashBoard


# Verify that inputed/current tripData displays properly
# for current trip
def test_trip1_input():
    dashboard = DashBoard()
    dashboard.tripMeter.currentTrip.setTripMileage(1.0)
    assert dashboard.tripMeter.currentTrip.getTripMileage() == 1.0


# Verify that inputed/current tripData displays properly
# for trip #2 is inital when current trip is #1
def test_trip2_input():
    dashboard = DashBoard()
    dashboard.tripMeter.trip2.setTripMileage(2.0)
    dashboard.tripMeter.currentTrip.setTripMileage(1.0)
    assert dashboard.tripMeter.trip2.getTripMileage() == 2.0


# Verify that switching from trip1 to trip2 works
# Asserting that trip2 data is current trip
def test_trip1_switchTo2():
    dashboard = DashBoard()
    dashboard.tripMeter.trip2.setTripMPG(1.0)
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    assert dashboard.tripMeter.currentTrip.getTripMPG() == 1.0


# Verify that switching from trip2 to trip1 works
# Asserting that trip1 data is current trip
def test_trip2_switchTo1():
    dashboard = DashBoard()
    dashboard.tripMeter.trip2.setTripMPG(1.0)
    dashboard.tripMeter.trip1.setTripMPG(5.0)
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    assert dashboard.tripMeter.currentTrip.getTripMPG() == 5.0

# Verify that switching multiple times maintains data in trip1 versus trip2
# Asserting that final switch data is the current trip
def test_multi_switch():
    dashboard = DashBoard()
    dashboard.tripMeter.trip2.setTripMPG(1.0)
    dashboard.tripMeter.trip1.setTripMPG(5.0)
    dashboard.tripMeter.button.setShortPress(True)
    # Switch to trip 2
    dashboard.tripMeter.isPressed()
    dashboard.tripMeter.button.setShortPress(True)
    # Switch to trip 1
    dashboard.tripMeter.isPressed()
    dashboard.tripMeter.button.setShortPress(True)
    # Switch to trip 2
    dashboard.tripMeter.isPressed()
    dashboard.tripMeter.button.setShortPress(True)
    # Switch to trip 1 and end switching
    dashboard.tripMeter.isPressed()
    # Value should be equal to trip 1 data
    assert dashboard.tripMeter.currentTrip.getTripMPG() == 5.0

# Verify that trip1 data resets to initial values
def test_trip1_reset():
    dashboard = DashBoard()
    dashboard.tripMeter.trip1.setTripMileage(1.0)
    dashboard.tripMeter.button.setLongPress(True)
    dashboard.tripMeter.isPressed()
    assert dashboard.tripMeter.trip1.getTripMileage() == 0.0


# Verify that trip2 data resets to initial values
def test_trip2_reset():
    dashboard = DashBoard()
    dashboard.tripMeter.trip1.setTripMileage(1.0)
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    dashboard.tripMeter.current.setTripMileage(2.0)
    dashboard.tripMeter.button.setLongPress(True)
    dashboard.tripMeter.isPressed()
    assert dashboard.tripMeter.currentTrip.getTripMileage() == 0.0


# Verify that trip2 data reset does not affect trip1 data
def test_clean_reset():
    dashboard = DashBoard()
    dashboard.tripMeter.trip1.setTripMileage(2.0)
    dashboard.tripMeter.button.setShortPress(True)
    dashboard.tripMeter.isPressed()
    dashboard.tripMeter.currentTrip.setTripMileage(3.0)
    dashboard.tripMeter.button.setLongPress(True)
    dashboard.tripMeter.isPressed()
    assert dashboard.tripMeter.trip1.getTripMileage() == 2.0
    assert dashboard.tripMeter.currentTrip.getTripMileage == 0.0

# Verify that time is true when over two
def test_time_true():
    dashboard = DashBoard()
    dashboard.tripMeter.currentTrip.setTripTime(2.0)
    assert dashboard.tripMeter.isTime(dashboard.tripMeter.currentTrip) == True

# Verify that time is false when time is close but not two
def test_time_false():
    dashboard = DashBoard()
    dashboard.tripMeter.currentTrip.setTripTime(1.99)
    assert dashboard.tripMeter.isTime(dashboard.tripMeter.currentTrip) == False