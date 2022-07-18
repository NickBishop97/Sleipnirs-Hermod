from TripMeter import DashBoard


# Testing for data input into trip 1
def test_trip1_case():
    d = DashBoard()
    d.TM.updateTrip(10, 10, 10, 1)
    temp = d.TM.curentTrip()
    captured = [temp.milesTraveled, temp.mpg, temp.avgspeed, temp.time,
            d.TM.currently_selected]
    assert captured == [10, 10, 10, 1, 0]


# Testing for data input into trip 2 and swtiching to trip 2
def test_trip2_case():
    d = DashBoard()
    d.TM.updateTrip(10, 10, 10, 1)
    d.BT.click()
    temp = d.TM.curentTrip()
    captured = [temp.milesTraveled, temp.mpg, temp.avgspeed, temp.time,
            d.TM.currently_selected]
    assert captured == [10, 10, 10, 1, 1]


# Testing for reseting data of trip 1 and if trip 2 still has data
def test_trip1reset_case():
    d = DashBoard()
    d.TM.updateTrip(1.0, 10, 0.0, 1.0)
    temp = d.TM.curentTrip()
    d.BT.longclick()
    captured = [temp.milesTraveled, temp.mpg, temp.avgspeed, temp.time,
            d.TM.currently_selected]
    assert captured == [0.0, 0.0, 0.0, 0.0, 0]
    d.BT.click()
    temp = d.TM.curentTrip()
    captured = [temp.milesTraveled, temp.mpg, temp.avgspeed, temp.time,
            d.TM.currently_selected]
    assert captured == [1.0, 10, 0.0, 1.0, 1]


# Testing for Trip Time Alert being on
def test_triptime2Hrs_case():
    d = DashBoard()
    d.TM.updateTrip(1.0, 10, 0.0, 2.0)
    data = d.checkTime()
    assert data == 1


# Testing for Trip Time alert being off
def test_TripTimeUnder2Hrs_case():
    d = DashBoard()
    d.TM.updateTrip(1.0, 10, 0.0, 1.0)
    data = d.checkTime()
    assert data == 0
