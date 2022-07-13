class TripData:
    def __init__(self, initialMiles, initialFuel, initialTime):
        self.initialMiles = initialMiles
        self.initialFuel = initialFuel
        self.initialTime = initialTime

    def setInitialMiles(self, miles):
        self.initialMiles = miles

    def setInitialFuel(self, fuel):
        self.initialFuel = fuel

    def setInitialTime(self, time):
        self.initialTime = time

    def getMileage(self, newMiles):
        return newMiles - self.initialMiles

    def getFuelConsumed(self, newFuel):
        return self.initialFuel - newFuel

    def getTimeElapsed(self, newTime):
        return newTime - self.initialTime

    def getAvSpeed(self, newMiles, newTime):
        return (self.getMileage(newMiles) / self.getTimeElapsed(newTime))

    def getAvMpg(self, newMiles, newFuel):
        return (self.getMileage(newMiles) / self.getFuelConsumed(newFuel))

    def clear(self):
        self.initialMiles = 0
        self.initialFuel = 0
        self.initialTime = 0
