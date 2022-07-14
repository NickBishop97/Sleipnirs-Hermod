import sys
sys.path.insert(0, "../")
from trip_meter import TripMeter


def testStandard():
    tm = TripMeter()
    tm.startNewTrip(50000, 17)
    tm.toggleTrip()
    tm.startNewTrip(60000, 12)

    # Test mileage
    tm.toggleTrip()  # Go to trip A
    assert tm.getMileage(50223) == 223, "Miles travelled incorrect for Trip A"
    tm.toggleTrip()  # Go to trip B
    assert tm.getMileage(61345) == 1345, "Miles traveled incorrect for Trip B"
    
    # Test fuel consumed
    tm.toggleTrip()  # Go to trip A
    assert tm.getFuelConsumed(13) == 4, "Fuel Consumed incorrect for Trip A"
    tm.toggleTrip()  # Go to trip B
    assert tm.getFuelConsumed(9) == 3, "Fuel Consumed incorrect for Trip B"

    # Test time elapsed
    tm.toggleTrip()  # Go to trip A
    assert tm.getTimeElapsed(60) == 60, "Time elapsed incorrect for Trip A"
    tm.toggleTrip()  # Go to trip B
    assert tm.getTimeElapsed(45) == 45, "Time elapsed incorrect for Trip B"

    # Test average speed
    tm.toggleTrip()  # Go to trip A
    assert tm.getAvSpeed(60000, 200) == 50, "Average speed incorrect for Trip A"
    tm.toggleTrip()  # Go to trip B
    assert tm.getAvSpeed(70000, 500) == 20, "Average speed incorrect for Trip B"

    # Test average mpg
    tm.toggleTrip()  # Go to trip A
    assert tm.getAvMpg(60000, 7) == 1000, "Average MPG incorrect for Trip A"
    tm.toggleTrip()  # Go to trip B
    assert tm.getAvMpg(70000, 2) == 1000, "Average MPG incorrect for Trip B"


# def testFuelConsumed():
# 
# 
# def testTimeElapsed():
# 
# 
# def testAvMpg():
# 
# 
# def testAvSpeed():
# 
# 
# def testClear():