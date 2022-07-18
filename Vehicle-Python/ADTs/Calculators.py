import time
import random
# import pytest

# NOTE THAT THESE ARE SELF DEFINED CLASSES, EACH TYPE OF CLASS WILL BE DIFFERENT AND WILL HAVE DIFFERENT UNITS


class FuelConsump:
    # CAPACITY IS INPUTTED AS GALLONS
    def __init__(self, capacity, currentFuel):
        # for better precision, use numpy dtype float64
        self.gallonToLiters = float(3.785412)

        self.capacityGallons = capacity
        self.capacityLiters = capacity * self.gallonToLiters

        self.currentFuelGallons = currentFuel
        self.currentFuelLiters = currentFuel * self.gallonToLiters

    def consumeFuel(self, stop_flag):
        if stop_flag:
            return(-1, -1)

        change = self.currentFuelGallons = self.currentFuelGallons - \
            random.uniform(0.001, 0.01)  # random.uniform(0.5, 1)#
        if change <= 0:
            self.currentFuelGallons = 0
        elif change > 0:
            self.currentFuelGallons = change
        else:
            self.currentFuelGallons = 0
        return (self.currentFuelGallons, self.capacityGallons - self.currentFuelGallons)

    def calculateFuelPercentage(self):
        if self.capacityGallons <= 0:
            return 0.0
        if self.currentFuelGallons < 0:
            return 0.0
        if self.currentFuelGallons > self.capacityGallons:
            return 100.0

        return ((self.currentFuelGallons / self.capacityGallons) * 100)

    # KILL SENSOR WHEN CONDITION IS MET, THIS IS A BASIC SIGNAL

    def controlSignal(self):
        time.sleep(50)
        return True


class DistTrav:
    def __init__(self, displacement):
        self.milesTraveled = displacement

    def addMiles(self, startStopCondition):
        # Fuel has not send data
        # if not startStopCondition.milesStarter:
        #    self.milesTraveled = -1

        if not startStopCondition.milesStopper and startStopCondition.milesStarter:
            self.milesTraveled += random.uniform(1, 2)


class LowFuelCalc:
    def __init__(self, threshold):
        self.threshold = threshold
        self.lowFuelAlertFlag = 0

    def lowFuelAlert(self, currentFuel):
        if self.threshold < 0:
            self.lowFuelAlertFlag = -1
            return self.lowFuelAlertFlag
        if currentFuel < self.threshold:
            self.lowFuelAlertFlag = 1
            return self.lowFuelAlertFlag
        else:
            self.lowFuelAlertFlag = 0
            return self.lowFuelAlertFlag


class MpGCalc:
    def __init__(self):
        self.mpg = 0

    def calculateMpG(self, fuelQueue, milesQueue):
        fuelDatum = 0
        milesDatum = 0

        if not fuelQueue.empty():
            fuelDatum = fuelQueue.get()[2]

        if not milesQueue.empty():
            milesDatum = milesQueue.get()[1]

        if not fuelDatum == 0:
            self.mpg = float(milesDatum) / float(fuelDatum)

        elif fuelDatum <= 0:
            self.mpg = float(-1)

        return self.mpg


class MileRemainCalc:
    def __init__(self):
        self.mileRemain = 0

    def calculateMpG(self, fuelQueue, mpgQueue):
        fuelDatum = 0
        mpgDatum = 0

        if not fuelQueue.empty():
            fuelDatum = fuelQueue.get()[1]
        else:
            fuelDatum = -1

        if not mpgQueue.empty():
            mpgDatum = mpgQueue.get()[1]

        self.mileRemain = float(mpgDatum) * float(fuelDatum)

        return self.mileRemain


class TripCalc:
    def __init__(self):
        self.trips = []
        self.currentTrip = 0

    # def returnTrip(self, tripNumber):

    def reset(self, button, totalMilesObj):
        if(button):
            totalMilesObj.milesTraveled = 0

    def addTrip(self, totalMilesObj):
        self.trips.append(totalMilesObj.milesTraveled)
        # receive the total miles traveled and reset them
