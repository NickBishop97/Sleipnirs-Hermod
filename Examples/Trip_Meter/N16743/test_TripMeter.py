from TripMeter import DashBoard


def test_trip1_case():
    d = DashBoard()
    d.TM.updateTrip(0.0, 10, 0.0, 0.0)
    temp = d.TM.curentTrip()
    list = [temp.milesTraveled, temp.mpg, temp.avgspeed, temp.time,
            d.TM.currently_selected]
    assert list == [0.0, 10, 0.0, 0.0, 0]


def test_trip2_case():
    d = DashBoard()
    d.TM.updateTrip(0.0, 10, 0.0, 0.0)
    d.BT.click()
    temp = d.TM.curentTrip()
    list = [temp.milesTraveled, temp.mpg, temp.avgspeed, temp.time,
            d.TM.currently_selected]
    assert list == [0.0, 10, 0.0, 0.0, 1]


def test_trip1reset_case():
    d = DashBoard()
    d.TM.updateTrip(1.0, 10, 0.0, 1.0)
    temp = d.TM.curentTrip()
    d.BT.longclick()
    list = [temp.milesTraveled, temp.mpg, temp.avgspeed, temp.time,
            d.TM.currently_selected]
    assert list == [0.0, 0.0, 0.0, 0.0, 0]
    d.BT.click()
    temp = d.TM.curentTrip()
    list = [temp.milesTraveled, temp.mpg, temp.avgspeed, temp.time,
            d.TM.currently_selected]
    assert list == [1.0, 10, 0.0, 1.0, 1]


def test_triptime2Hrs_case():
    d = DashBoard()
    d.TM.updateTrip(1.0, 10, 0.0, 2.0)
    data = d.checkTime()
    assert data == 1


def test_TripTimeUnder2Hrs_case():
    d = DashBoard()
    d.TM.updateTrip(1.0, 10, 0.0, 1.0)
    data = d.checkTime()
    assert data == 0
