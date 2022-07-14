from TripMeterLemuel import Dashboard, Button, TripMeter, TripData

testTD1 = TripData(25.0, 100.0, 0.0, 35.0)
testTD2 = TripData(30.0, 90.0, 0.0, 20.0)
testTM = TripMeter(testTD1, testTD2)
testDash = Dashboard(testTM)

def test_base_case():
    assert testDash.button.tm.display_miles_traveled() == 25.0