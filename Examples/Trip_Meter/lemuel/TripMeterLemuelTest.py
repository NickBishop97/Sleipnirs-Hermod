# Testing file to make sure that the Trip Meter program works as intended
# =======================================================================



# import file to test
from TripMeterLemuel import *


def test_to_display_stuff(inputDash, parm1, parm2, parm3, parm4):
    assert inputDash.button.tm.display_miles_traveled() == parm1
    assert inputDash.button.tm.display_mpg() == parm2
    assert inputDash.button.tm.display_time() == parm3
    assert inputDash.button.tm.display_avg_speed() == parm4

# Testing for switching between displaying trip data objects
# ----------------------------------------------------------
def test_data_switch():

    # initialize the test objects
    testTD1 = TripData(25.0, 100.0, 0.0, 35.0)
    testTD2 = TripData(30.0, 90.0, 0.0, 20.0)
    testTM = TripMeter(testTD1, testTD2)
    testDash = Dashboard(testTM)

    # test to make sure that the function calls return the correct data
    test_to_display_stuff(testDash, 25.0, 100.0, 3600.0, 0.01)
    #assert testDash.button.tm.display_miles_traveled() == 25.0
    #assert testDash.button.tm.display_mpg() == 100.0
    #assert testDash.button.tm.display_time() == 3600
    #assert testDash.button.tm.display_avg_speed() == 0.01

    # simulate short button press to change current trip data
    testDash.button.short_press()

    # test to make sure that the function calls return the correct data
    assert testDash.button.tm.display_miles_traveled() == 30.0
    assert testDash.button.tm.display_mpg() == 90.0
    assert testDash.button.tm.display_time() == 3600
    assert testDash.button.tm.display_avg_speed() == 0.01
    testDash.button.short_press()



# Test that data resetting functions work
# ---------------------------------------
def test_data_reset():

    # initialize the test objects
    testTD1 = TripData(25.0, 100.0, 0.0, 35.0)
    testTD2 = TripData(30.0, 90.0, 0.0, 20.0)
    testTM = TripMeter(testTD1, testTD2)
    testDash = Dashboard(testTM)

    # test the simulated long press to make sure that the data has been reset to zero
    testDash.button.long_press()
    assert testDash.button.tm.display_miles_traveled() == 0.0
    assert testDash.button.tm.display_mpg() == 0.0
    assert testDash.button.tm.display_time() == 3600
    assert testDash.button.tm.display_avg_speed() == 0.0

    # change between trip data objects to prepare to reset
    testDash.button.short_press()
    assert testDash.button.tm.display_miles_traveled() == 30.0
    assert testDash.button.tm.display_mpg() == 90.0
    assert testDash.button.tm.display_time() == 3600
    assert testDash.button.tm.display_avg_speed() == 0.01

    # simulate long press to test the reset of data
    testDash.button.long_press()
    assert testDash.button.tm.display_miles_traveled() == 0.0
    assert testDash.button.tm.display_mpg() == 0.0
    assert testDash.button.tm.display_time() == 3600
    assert testDash.button.tm.display_avg_speed() == 0.0



# Testing function to determine if an alarm will go off
# -----------------------------------------------------
def test_alarm():

    # initialize the test objects
    testTD1 = TripData(25.0, 100.0, 0.0, 35.0)
    testTD2 = TripData(30.0, 90.0, 0.0, 20.0)
    testTM = TripMeter(testTD1, testTD2)
    testDash = Dashboard(testTM)

    # test alarm function when the amount of time is one hour
    assert testDash.button.tm.check_for_alarm_for_current_trip() == 'Everything good.'
    
    # set the time to the very boundary of the alarm threshold to test
    testDash.button.tm.trip_data_list[0].current_time = 7199
    assert testDash.button.tm.check_for_alarm_for_current_trip() == 'Everything good.'

    # set time to exactly two hours to trigger the alarm
    testDash.button.tm.trip_data_list[0].current_time = 7200
    assert testDash.button.tm.check_for_alarm_for_current_trip() == 'Alert! Alert!'

    # change from one trip data object to another to test if the time changed as well
    testDash.button.short_press()
    assert testDash.button.tm.check_for_alarm_for_current_trip() == 'Everything good.'



# Test to see if we can add another trip data object
# --------------------------------------------------
def test_add_trip_data():
    
    # initialize the test objects
    testTD1 = TripData(25.0, 100.0, 0.0, 35.0)
    testTD2 = TripData(30.0, 90.0, 0.0, 20.0)
    testTM = TripMeter(testTD1, testTD2)
    testDash = Dashboard(testTM)

    testTD3 = TripData(10.0, 50.0, 60.0, 60.0)
    testDash.button.tm.add_trip(testTD3)

    testDash.button.short_press()
    testDash.button.short_press()



test_data_switch()
test_data_reset()
test_alarm()