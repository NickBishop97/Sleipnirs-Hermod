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

    def getTripMileage(self):
        return self.tripMileage

    def getTripMPG(self):
        return self.tripMPG

    def getTripSpeed(self):
        return self.tripSpeed

    def getTripTime(self):
        return self.trip

    def reset(self):
        self.tripMileage = 0.0
        self.tripMPG = 0.0
        self.tripSpeed = 0.0
        self.tripTime = 0.0


class TripMeter:
    def __init__(self, currentTrip):
        self.trip1 = TripData(0.0, 0.0, 0.0, 0.0)
        self.trip2 = TripData(0.0, 0.0, 0.0, 0.0)
        self.currentTrip = currentTrip
        self.tripNumber = 1
        currentTrip = self.trip1
        self.button = Button(False, False)

    def getTripNumber(self):
        return self.tripNumber

    def setTripNumber(self, tripNumber):
        self.tripNumber = tripNumber

    def setCurrentTrip(self):
        if (self.getTripNumber() == 1):
            self.setTripNumber(2)
            self.currentTrip = self.trip2
        elif (self.getTripNumber() == 2):
            self.setTripNumber(1)
            self.currentTrip = self.trip1

    def isPressed(self, button):
        if (button.shortPress == True):
            self.setCurrentTrip()
        elif (button.longPress == True):
            self.reset()

    def isTime(self, currentTrip):
        if (currentTrip.tripTime < 2.0):
            return False
        else:
            return True


    def reset(self, trip):
        trip.reset()


class Button:
    def __init__(self, shortPress, longPress):
        self.shortPress = shortPress
        self.longPress = longPress

    def getShortPress(self):
            return self.shortPress

    def getLongPress(self):
            return self.longPress

    def setShortPress(self, shortPress):
        self.shortPress = shortPress

    def setLongPress(self, longPress):
        self.longPress = longPress

class DashBoard:
    def __init__(self):
        self.tripMeter = TripMeter(TripData(0.0, 0.0, 0.0, 0.0))



def main():
    d = DashBoard()
    d.tripMeter.currentTrip.setTripMPG(1)
    print(d.tripMeter.currentTrip.getTripMPG())
    d.tripMeter.currentTrip.reset()
    print(d.tripMeter.currentTrip.getTripMPG())



if __name__ == "__main__":
    main()
