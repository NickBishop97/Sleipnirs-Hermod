#!/opt/rh/rh-python38/root/usr/bin/python3

import pytest 


class TripData:
    def __init__(self, tripMileage, tripMPG, tripSpeed, tripTime):

        self.tripMileage = tripMileage
        self.tripMPG = tripMPG
        self.tripSpeed = tripSpeed
        self.tripTime = tripTime

    def setTripMileage(self, tripMileage):
        # Update only if the value is non-negative
        if (tripMileage >= 0):
            self.tripMileage = tripMileage

    def setTripMPG(self, tripMPG):
        if (tripMPG >= 0):
            self.tripMPG = tripMPG

    def setTripSpeed(self, tripSpeed):
        if (tripSpeed >= 0):
            self.tripSpeed = tripSpeed

    def setTripTime(self, tripTime):
        if (tripTime >= 0):
            self.tripTime = tripTime

    def getTripMileage(self):
        return self.tripMileage

    def getTripMPG(self):
        return self.tripMPG

    def getTripSpeed(self):
        return self.tripSpeed

    def getTripTime(self):
        return self.tripTime

    def reset(self):
        self.tripMileage = 0.0
        self.tripMPG = 0.0
        self.tripSpeed = 0.0
        self.tripTime = 0.0


class TripMeter:
    def __init__(self):
        self.trip1 = TripData(0.0, 0.0, 0.0, 0.0)
        self.trip2 = TripData(0.0, 0.0, 0.0, 0.0)
        self.currentTrip = 1
        self.button = Button(False, False)

    def getCurrentTrip(self):
        if (self.currentTrip == 1):
            return self.trip1   
        elif (self.currentTrip == 2):
            return self.trip2   

    def isPressed(self):
        if (self.button.shortPress == True):
            # Reset button after pressing
            self.button.setShortPress(False)
            if (self.currentTrip == 1):
                self.currentTrip = 2
            elif (self.currentTrip == 2):
                self.currentTrip = 1    
        elif (self.button.longPress == True):
            # Reset button after pressing
            self.button.setLongPress(False)
            self.reset()

    def isTime(self, trip):
        if (trip.getTripTime() < 2.0):
            return False
        else:
            return True

    def reset(self):
        self.getCurrentTrip().reset()


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
        self.tripMeter = TripMeter()


def main():
    d = DashBoard()


if __name__ == "__main__":
    main()
