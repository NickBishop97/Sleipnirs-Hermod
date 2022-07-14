from TripMeterLemuel import *

def test_data_switch():
    testTD1 = TripData(25.0, 100.0, 0.0, 35.0)
    testTD2 = TripData(30.0, 90.0, 0.0, 20.0)
    testTM = TripMeter(testTD1, testTD2)
    testDash = Dashboard(testTM)

    assert testDash.button.tm.display_miles_traveled() == 25.0
    assert testDash.button.tm.display_mpg() == 100.0
    assert testDash.button.tm.display_time() == 3600
    assert testDash.button.tm.display_avg_speed() == 0.01
    testDash.button.short_press()

    assert testDash.button.tm.display_miles_traveled() == 30.0
    assert testDash.button.tm.display_mpg() == 90.0
    assert testDash.button.tm.display_time() == 3600
    assert testDash.button.tm.display_avg_speed() == 0.01
    testDash.button.short_press()
    
    testDash.button.long_press()
    assert testDash.button.tm.display_miles_traveled() == 0.0
    assert testDash.button.tm.display_mpg() == 0.0
    assert testDash.button.tm.display_time() == 3600
    assert testDash.button.tm.display_avg_speed() == 0.0


def test_data_reset():
    testTD1 = TripData(25.0, 100.0, 0.0, 35.0)
    testTD2 = TripData(30.0, 90.0, 0.0, 20.0)
    testTM = TripMeter(testTD1, testTD2)
    testDash = Dashboard(testTM)

    testDash.button.long_press()
    assert testDash.button.tm.display_miles_traveled() == 0.0
    assert testDash.button.tm.display_mpg() == 0.0
    assert testDash.button.tm.display_time() == 3600
    assert testDash.button.tm.display_avg_speed() == 0.0

    testDash.button.short_press()
    assert testDash.button.tm.display_miles_traveled() == 30.0
    assert testDash.button.tm.display_mpg() == 90.0
    assert testDash.button.tm.display_time() == 3600
    assert testDash.button.tm.display_avg_speed() == 0.01

    testDash.button.long_press()
    assert testDash.button.tm.display_miles_traveled() == 0.0
    assert testDash.button.tm.display_mpg() == 0.0
    assert testDash.button.tm.display_time() == 3600
    assert testDash.button.tm.display_avg_speed() == 0.0

def test_alarm():
    testTD1 = TripData(25.0, 100.0, 0.0, 35.0)
    testTD2 = TripData(30.0, 90.0, 0.0, 20.0)
    testTM = TripMeter(testTD1, testTD2)
    testDash = Dashboard(testTM)

    assert testDash.button.tm.check_for_alarm_for_current_trip() == 'Everything good.'
    testDash.button.tm.trip_data_list[0].current_time = 7199
    assert testDash.button.tm.check_for_alarm_for_current_trip() == 'Everything good.'
    testDash.button.tm.trip_data_list[0].current_time = 7200
    assert testDash.button.tm.check_for_alarm_for_current_trip() == 'Alert! Alert!'
    testDash.button.short_press()
    assert testDash.button.tm.check_for_alarm_for_current_trip() == 'Everything good.'



test_data_switch()
test_data_reset()
test_alarm()