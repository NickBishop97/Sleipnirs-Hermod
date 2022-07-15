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
    # Assign value to currentTrip, which such be trip1
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_NEW_VALUE)
    # Get value from trip1 as a temp object  
    temp = dashboard.tripMeter.trip1.getTripSpeed()
    # Verify that value of trip1 was assigned to by currentTrip
    assert temp == CONST_NEW_VALUE



# Verify that inputed/current tripData displays properly
# for trip #2 is inital when current trip is #1
def test_trip2_input():
    dashboard = DashBoard()
    # Switch currentTrip from trip1 to trip2
    dashboard.tripMeter.getCurrentTrip().setTripSpeed(CONST_NEW_VALUE)
    # Get value from trip2 as a temp object  
    temp = dashboard.tripMeter.trip1.getTripSpeed()
    # Verify that value of trip2 was assigned to by currentTrip
    assert temp == CONST_NEW_VALUE
    


# Verify that switching from trip1 to trip2 works
# Asserting that trip2 data is current trip
def test_trip1_switchTo2():
    dashboard = DashBoard()
    


# Verify that switching from trip2 to trip1 works
# Asserting that trip1 data is current trip
def test_trip2_switchTo1():
    dashboard = DashBoard()
    

# Verify that switching multiple times maintains data in trip1 versus trip2
# Asserting that final switch data is the current trip
def test_multi_switch():
    dashboard = DashBoard()
    

# Verify that trip1 data resets to initial values
def test_trip1_reset():
    dashboard = DashBoard()
    


# Verify that trip2 data resets to initial values
def test_trip2_reset():
    dashboard = DashBoard()
    


# Verify that trip2 data reset does not affect trip1 data
def test_clean_reset():
    dashboard = DashBoard()
    

# Verify that time is true when over two
def test_time_true():
    dashboard = DashBoard()
    

# Verify that time is false when time is close but not two
def test_time_false():
    dashboard = DashBoard()
    