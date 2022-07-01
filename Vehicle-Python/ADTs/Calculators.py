import time
import random
import pytest

# NOTE THAT THESE ARE SELF DEFINED CLASSES, EACH TYPE OF CLASS WILL BE DIFFERENT AND WILL HAVE DIFFERENT UNITS

class FuelConsump:
    #CAPACITY IS INPUTTED AS GALLONS
    def __init__(self, capacity, currentFuel):
        #for better precision, use numpy dtype float64
        self.gallonToLiters     = float(3.785412) 
        
        self.capacityGallons    = capacity
        self.capacityLiters     = capacity * self.gallonToLiters
        
        self.currentFuelGallons = currentFuel
        self.currentFuelLiters  = currentFuel * self.gallonToLiters
        
    def consumeFuel(self, test_flag):
        if test_flag:
            return(-1, -1)
            
        change = self.currentFuelGallons = self.currentFuelGallons - random.uniform(0.01, 0.1)
        if change <= 0:
            self.currentFuelGallons = 0 
        elif change > 0:
            self.currentFuelGallons = change
        else:
            self.currentFuelGallons = 0
        return (self.currentFuelGallons, self.capacityGallons - self.currentFuelGallons)
        
        
        
        
        
        
    
    #KILL SENSOR WHEN CONDITION IS MET, THIS IS A BASIC SIGNAL
    def controlSignal(self):
        time.sleep(50)
        return True

class DistTrav:
    def __init__(self, displacement):
        self.milesTraveled = displacement
        
    def addMiles(self, startStopCondition):
        #Fuel has not send data
        #if not startStopCondition.milesStarter:
        #    self.milesTraveled = -1
        
        if not startStopCondition.milesStopper and startStopCondition.milesStarter:
            self.milesTraveled += random.uniform(1,2)
            
class LowFuel:
    def __init__(self, threshold):
        self.threshold = threshold
        self.lowFuelAlertFlag = "Fuel Status: Good"
    
    def lowFuelAlert(self, currentFuel):
        if currentFuel < self.threshold:
            self.lowFuelAlertFlag = "Fuel Status: Low"
        else:
            self.lowFuelAlertFlag = "Fuel Status: Good"
