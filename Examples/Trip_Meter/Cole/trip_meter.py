from trip_data import TripData

class TripMeter:
    def __init__(self):
        self.tripA = TripData(0, 0, 0)
        self.tripB = TripData(0, 0, 0)
        self.tripPtr = self.tripA

    def toggleTrip(self):
        self.tripPtr = self.tripB if self.tripPtr == self.tripA else self.tripA

    def getMileage(self, newMiles):
        return self.tripPtr.getMileage(newMiles)

    def getFuelConsumed(self, newFuel):
        return self.tripPtr.getFuelConsumed(newFuel)

    def getTimeElapsed(self, newTime):
        return self.tripPtr.getTimeElapsed(newTime)

    def getAvSpeed(self, newMiles, newTime):
        return self.tripPtr.getAvSpeed(newMiles, newTime)

    def getAvMpg(self, newMiles, newFuel):
        return self.tripPtr.getAvMpg(newMiles, newFuel)

    def startNewTrip(self, miles, fuel):
        self.tripPtr.setInitialMiles(miles)
        self.tripPtr.setInitialFuel(fuel)
        self.tripPtr.setInitialTime(0)

    def clearMiles(self, newInitialMiles):
        self.tripPtr.setInitialMiles(newInitialMiles)

    def clearAll(self):
        self.tripPtr.clear()