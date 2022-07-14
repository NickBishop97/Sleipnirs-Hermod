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
    dashboard.tripMeter.currentTrip.setTripMileage(1.0)
    assert dashboard.tripMeter.trip2.getTripMileage() == 0.0


# Verify that switching from trip1 to trip2 works
def test_trip1_switchTo2():
    dashboard = DashBoard()
    dashboard.tripMeter.currentTrip.setTripMileage(1.0)
    dashboard.tripMeter.currentTrip.setTripMileage(1.0)
    assert dashboard.tripMeter.trip2.getTripMileage() == 0.0


# Verify that switching from trip2 to trip1 works
def test_trip2_switchTo1():
    dashboard = DashBoard()
    dashboard.tripMeter.currentTrip.setTripMileage(1.0)
    assert dashboard.tripMeter.trip2.getTripMileage() == 0.0

# Verify that switching multiple times maintains data in trip1 versus trip2
def test_multi_switch():
    dashboard = DashBoard()
    dashboard.tripMeter.currentTrip.setTripMileage(1.0)
    assert dashboard.tripMeter.trip2.getTripMileage() == 0.0

# Verify that trip1 data resets to initial values
def test_trip1_reset():
    dashboard = DashBoard()
    dashboard.tripMeter.currentTrip.setTripMileage(1.0)
    assert dashboard.tripMeter.trip2.getTripMileage() == 0.0


# Verify that trip2 data resets to initial values
def test_trip2_reset():
    dashboard = DashBoard()
    dashboard.tripMeter.currentTrip.setTripMileage(1.0)
    assert dashboard.tripMeter.trip2.getTripMileage() == 0.0
