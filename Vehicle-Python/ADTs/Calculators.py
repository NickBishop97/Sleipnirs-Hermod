"""@package docstring
This py file contains all of the calculations for publisher and subscribers

@class FuelConsump - Does calculations based on fuel consumption rate in L/Gal
@class DisTrav - Does calculations to find the distance traveled
@class LowFuelCalc - Does calculations to determine if the low fuel alert is 1/0
@class MPGCalc - Calculates the miles per gallon
@class MileRemainCalc - Calculates the miles remaining till the tank is empty
@class TripCalc - Does calculations related to tripmeter display.
"""
import time
import random

# NOTE THAT THESE ARE SELF DEFINED CLASSES, EACH TYPE OF CLASS WILL BE DIFFERENT AND WILL HAVE DIFFERENT UNITS


class FuelConsump:

    # CAPACITY IS INPUTTED AS GALLONS
    def __init__(self, capacity, currentFuel):
        """FuelConsump constructor

        @param capacity max capacity of tank
        @param currentFuel fuel level at the current moment measured in Gallons
        """
        # for better precision, use numpy dtype float64
        self.gallonToLiters = float(3.785412)

        self.capacityGallons = capacity
        self.capacityLiters = capacity * self.gallonToLiters

        self.currentFuelGallons = currentFuel
        self.currentFuelLiters = currentFuel * self.gallonToLiters

    def consumeFuel(self, stop_flag):
        """ConsumeFuel
        @brief Generates a random number between 0.5 and 1 and removed that much fuel
        from the remaining fuel. Will return a (-1, -1) if the car is stopped.

        @param stop_flag tells the function that the car is stopped or not
        """
        if stop_flag:
            return(-1, -1)

        change = self.currentFuelGallons - random.uniform(0.001, 0.01)  # random.uniform(0.5, 1)#
        self.currentFuelGallons = change
        if self.currentFuelGallons < 0:
            self.currentFuelGallons = 0
        elif change > 0:
            self.currentFuelGallons = change
        return (self.currentFuelGallons, self.capacityGallons - self.currentFuelGallons)

    def calculateFuelPercentage(self):
        """calculateFuelPercentage
        @brief calculates the fuel percentage based on the current fuel remaining

        @return 0.0 through 100.0
        """
        if self.capacityGallons <= 0:
            return 0.0
        if self.currentFuelGallons < 0:
            return 0.0
        if self.currentFuelGallons > self.capacityGallons:
            return 100.0

        return ((self.currentFuelGallons / self.capacityGallons) * 100)

    # KILL SENSOR WHEN CONDITION IS MET, THIS IS A BASIC SIGNAL

    def controlSignal(self):
        """controlSignal
        @brief will return true when called, kills the sensor when called.

        @return True
        """
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
            fuelDatum = fuelQueue.get()[1]

        if not milesQueue.empty():
            milesDatum = milesQueue.get()[1]

        if fuelDatum <= 0:
            self.mpg = float(-1)

        elif milesDatum < 0:
            self.mpg = float(-1)

        elif not fuelDatum == 0:
            self.mpg = float(milesDatum) / float(fuelDatum)

        return self.mpg


class MileRemainCalc:
    def __init__(self):
        self.mileRemain = 0

    def calculateMileRemain(self, fuelQueue, mpgQueue):
        fuelDatum = 0
        mpgDatum = 0

        if not fuelQueue.empty():
            fuelDatum = fuelQueue.get()[1]
        else:
            fuelDatum = -1

        if not mpgQueue.empty():
            mpgDatum = mpgQueue.get()[1]

        if fuelDatum < 0:
            self.mileRemain = float(0)
        elif mpgDatum < 0:
            self.mileRemain = float(-1)
        else:
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
