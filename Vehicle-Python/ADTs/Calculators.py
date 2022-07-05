import time
import random
import pytest

# NOTE THAT THESE ARE SELF DEFINED CLASSES, EACH TYPE OF CLASS WILL BE DIFFERENT AND WILL HAVE DIFFERENT UNITS

class LowFuel:
    def __init__(self, threshold):
        self.threshold = threshold
        self.lowFuelAlertFlag = "Fuel Status: Good"
    
    def lowFuelAlert(self, currentFuel):
        if currentFuel < self.threshold:
            self.lowFuelAlertFlag = "Fuel Status: Low"
        else:
            self.lowFuelAlertFlag = "Fuel Status: Good"

class FuelConsump:
    #CAPACITY IS INPUTTED AS GALLONS
    def __init__(self, capacity, currentFuel):
        #for better precision, use numpy dtype float64
        self.gallonToLiters     = float(3.785412) 
        
        self.capacityGallons    = capacity
        self.capacityLiters     = capacity * self.gallonToLiters
        
        self.currentFuelGallons = currentFuel
        self.currentFuelLiters  = currentFuel * self.gallonToLiters
        
    def consumeFuel(self, delta):
        change = self.currentFuelGallons = self.currentFuelGallons - delta
        if change <= 0:
            self.currentFuelGallons = 0
            
        elif change > 0:
            self.currentFuelGallons = change
        else:
            self.currentFuelGallons = 0
        
        return self.currentFuelGallons
    
    #KILL SENSOR WHEN CONDITION IS MET, THIS IS A BASIC SIGNAL
    def controlSignal(self):
        time.sleep(50)
        return True
    

class DistTrav:
    def __init__(self, displacement):
        self.milesTraveled = displacement
        
    def addMiles(self, stopState):
        if stopState.milesStopper:
            self.milesTraveled += 0
        else:
            self.milesTraveled += random.uniform(1, 2)


class MPG:
    def __init__(self, fuel, dist, capacity):
        self.fuelSpent = capacity - float(fuel)
        self.distance = float(dist)
        self.mpg = 0.0

    def getMPG(self):
        if self.fuelSpent <= 0:
            self.mpg = -1
        else:
            self.mpg = self.distance / self.fuelSpent
        return self.mpg

    def setFuel(self, fuel):
        self.fuelSpent = float(fuel)

    def setDist(self, dist):
        self.distance = float(dist)


class FuelGauge:
    def __init__(self, fuel_remaining, max_capacity):
        self.fuel_remaining = fuel_remaining
        self.max_capacity = max_capacity
    
    def getRemainingFuel(self):

        if self.max_capacity <= 0.0 or self.fuel_remaining <= 0.0:
            return 0.0
        elif self.fuel_remaining > self.max_capacity:
            return 100.0
        return (self.fuel_remaining/self.max_capacity) * 100
        