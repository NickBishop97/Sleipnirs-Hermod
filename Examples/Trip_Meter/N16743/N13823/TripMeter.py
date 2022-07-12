import pytest


class TripData:
    def __init__(self, tripMileage, tripMPG, tripSpeed, tripTime):

        self.tripMileage = tripMileage
        self.tripMPG = tripMPG
        self.tripSpeed = tripSpeed
        self.tripTime = tripTime

    def setTripMileage(self, tripMileage):
        self.tripMileage = tripMileage

    def setTripMPG(self, tripMPG):
        self.tripMPG = tripMPG

    def setTripSpeed(self, tripSpeed):
        self.tripSpeed = tripSpeed

    def setTripTime(self, tripTime):
        self.tripTime = tripTime

    def reset(self):
        self.tripMileage = 0.0
        self.tripMPG = 0.0
        self.tripSpeed = 0.0
        self.tripTime = 0.0


class TripMeter:
    def __init__(self):
        self.trip1 = TripData(0.0, 0.0, 0.0, 0.0)
        self.trip2 = TripData(0.0, 0.0, 0.0, 0.0)
        self.currentTrip = 0

    def setCurrentTrip(self, tripSelected):
        self.currentTrip = tripSelected

    def reset(self, trip):
        trip.reset()

class Button:
    def __init__(self, shortPress, longPress, ):
        self.shortPress = shortPress
        self.longPress = longPress

class DashBoard:
    def __init__(self):
        self.tripMeter = TripMeter()


def main():
    d = DashBoard()
    d.TM.tripMeter.setMPG(1)
    print(d.TM.trip1.mpg)
    d.TM.trip1.resetTrip()


if __name__ == "__main__":
    main()
