from sleipnir.Examples.Trip_Meter.N16743.N13823.TripMeter import DashBoard

# Verify that inputed/current tripData displays properly
# for trip #1
def test_trip1_input():
    dashboard = DashBoard()
    dashboard.TM.setTripMileage(1.0)
    dashboard.TM.setTripSpeed(1.0)
    dashboard.TM.setTripMPG(1.0)
    dashboard.TM.setTripTime(1.0)


# Verify that inputed/current tripData displays properly
# for trip #2
def test_trip2_input():
    dashboard = DashBoard()

# Verify that switching from trip1 to trip2 works
def test_trip1_switchTo2():
    dashboard = DashBoard()

# Verify that switching from trip2 to trip1 works
def test_trip2_switchTo1():
    dashboard = DashBoard()
# Verify that trip1 data resets to initial values
def test_trip1_reset():
    dashboard = DashBoard()

# Verify that trip2 data resets to initial values
def test_trip2_reset():
    dashboard = DashBoard()