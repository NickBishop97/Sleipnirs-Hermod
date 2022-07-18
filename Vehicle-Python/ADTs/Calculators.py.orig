import time
import random
<<<<<<< HEAD
from xmlrpc.client import Boolean

# NOTE THAT THESE ARE SELF DEFINED CLASSES, EACH TYPE OF CLASS WILL BE DIFFERENT AND WILL HAVE DIFFERENT UNITS

=======
# import pytest

# NOTE THAT THESE ARE SELF DEFINED CLASSES, EACH TYPE OF CLASS WILL BE DIFFERENT AND WILL HAVE DIFFERENT UNITS


>>>>>>> master
class FuelConsump:
    # CAPACITY IS INPUTTED AS GALLONS
    def __init__(self, capacity, currentFuel):
        # for better precision, use numpy dtype float64
        self.gallonToLiters = float(3.785412)

        self.capacityGallons = capacity
        self.capacityLiters = capacity * self.gallonToLiters

        self.currentFuelGallons = currentFuel
<<<<<<< HEAD
        self.currentFuelLiters  = currentFuel * self.gallonToLiters
        
    def consumeFuel(self, stop_flag, delta = random.uniform(0.001, 0.01)):
        if stop_flag:
            return(-1, -1)
            
        change = self.currentFuelGallons = self.currentFuelGallons - delta#random.uniform(0.5, 1)#
        if change <= 0:
            self.currentFuelGallons = 0 
=======
        self.currentFuelLiters = currentFuel * self.gallonToLiters

    def consumeFuel(self, stop_flag):
        if stop_flag:
            return(-1, -1)

        change = self.currentFuelGallons = self.currentFuelGallons - random.uniform(0.001, 0.01)  # random.uniform(0.5, 1)#
        if change <= 0:
            self.currentFuelGallons = 0
>>>>>>> master
        elif change > 0:
            self.currentFuelGallons = change
        else:
            self.currentFuelGallons = 0
        return (self.currentFuelGallons, self.capacityGallons - self.currentFuelGallons)
<<<<<<< HEAD
        
    #KILL SENSOR WHEN CONDITION IS MET, THIS IS A BASIC SIGNAL
    def controlSignal(self):
        time.sleep(50)
        return True

class DistTrav:
    def __init__(self, displacement):
        self.__milesTraveled = displacement
        self.__delta         = random.uniform(1,2)
        
    def addMiles(self, fuelQueue):
        #Fuel has not send data
        #if not startStopCondition.milesStarter:
        #    self.milesTraveled = -1
        if not fuelQueue.empty():
            data = fuelQueue.get()

            #If the fuel guage is sending values <= 0, it is likely that the fuel tank is out
            #For an odometer, the state would be kept and a displacement would be calculated
            if float(data[1]) <= 0:
                print("*****NO FUEL*****")
            else:
                self.__milesTraveled +=  self.__delta
    
    def setDelta(self, delta) -> None:
        self.__delta = delta
            
=======

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


>>>>>>> master
class LowFuelCalc:
    def __init__(self, threshold):
        self.threshold = threshold
        self.lowFuelAlertFlag = 0
<<<<<<< HEAD
    
    def lowFuelAlert(self, currentFuel):
=======

    def lowFuelAlert(self, currentFuel):
        if self.threshold < 0:
            self.lowFuelAlertFlag = -1
            return self.lowFuelAlertFlag
>>>>>>> master
        if currentFuel < self.threshold:
            self.lowFuelAlertFlag = 1
            return self.lowFuelAlertFlag
        else:
            self.lowFuelAlertFlag = 0
            return self.lowFuelAlertFlag

<<<<<<< HEAD
class MpGCalc:
    def __init__(self):
        self.mpg = 0
    
=======

class MpGCalc:
    def __init__(self):
        self.mpg = 0

>>>>>>> master
    def calculateMpG(self, fuelQueue, milesQueue):
        fuelDatum = 0
        milesDatum = 0

        if not fuelQueue.empty():
<<<<<<< HEAD
            fuelDatum  = fuelQueue.get()[2]
            
        if not milesQueue.empty():
            milesDatum  = milesQueue.get()[1]
        
        if not fuelDatum == 0:
            self.mpg = float(milesDatum)/float(fuelDatum)
        
        elif fuelDatum <= 0:
            self.mpg = float(-1)
            
            
        return self.mpg
    
    
class MileRemainCalc:
    def __init__(self):
        self.mileRemain = 0
    
=======
            fuelDatum = fuelQueue.get()[2]

        if not milesQueue.empty():
            milesDatum = milesQueue.get()[1]

        if not fuelDatum == 0:
            self.mpg = float(milesDatum)/float(fuelDatum)

        elif fuelDatum <= 0:
            self.mpg = float(-1)

        return self.mpg


class MileRemainCalc:
    def __init__(self):
        self.mileRemain = 0

>>>>>>> master
    def calculateMpG(self, fuelQueue, mpgQueue):
        fuelDatum = 0
        mpgDatum = 0

        if not fuelQueue.empty():
            fuelDatum = fuelQueue.get()[1]
        else:
            fuelDatum = -1
<<<<<<< HEAD
            
        if not mpgQueue.empty():
            mpgDatum = mpgQueue.get()[1]
        
        self.mileRemain = float(mpgDatum) * float(fuelDatum)
        
        return self.mileRemain
    
class TimeCalc:
    #net time elapsed
    def timedButton(self, timeElapsed = random.randint(0,3)):
        #Implement time stuff here
        return timeElapsed    
               
class ButtonCalc:
    def timedButton(self, timePressed = random.randint(0,3)):
        #Implement button stuff here
        return timePressed
    
class AverageSpeedCalc:
    def averageSpeed(self, distance, time):
        return float(distance / time)
    
 
class TripCalc:
    def __init__(self):
        self.currentTripNum = 0
        self.trip_dict = {
            "averageSpeed"     : 0,
            "distance"         : 0,
            "time"             : 0,
            "MpG"              : 0,
            "twoHours"         : False,
            "resetCounterDist" : 0,
            "resetCounterTime" : 0
            
        }
        self.trips = [dict(self.trip_dict), dict(self.trip_dict)]
    
    def update(self, dataArray):
        data = []
        
        for i in range(len(dataArray)):
            data.append(dataArray[i].get()[1])
            
        for i in range(len(self.trips)):
            #don't update resetcounter here    
            self.trips[i]["averageSpeed"] = data[0]
            self.trips[i]["distance"]     = data[1] - self.trips[i]["resetCounterDist"]
            self.trips[i]["time"]         = data[2] - self.trips[i]["resetCounterTime"]
            self.trips[i]["MpG"]          = data[3]
            
            if self.trips[i]["time"] >= float(2):
                self.trips[i]["twoHours"] = True

    def reset(self, resetButton):
        #deep copy
        currentTrip = self.trips[self.currentTripNum]
        
        #if long reset, reset all of the values
        if resetButton >= 3:
            data = self.trip_dict
            
            #write a comment of the equation for this block
            data["resetCounterDist"] += currentTrip["distance"]
            data["resetCounterTime"] += currentTrip["time"]
            
            #making the trip dict all zeros
            self.trips[self.currentTripNum] = data
        
        #if a short reset, switch trips
        elif resetButton >=0 and resetButton < 3:
            self.currentTripNum = (self.currentTripNum + 1) % 2
        else:
            pass
         
        
    def calculateTripData(self, resetButton, dataArray):
        self.reset(resetButton)
        self.update(dataArray)
        return self.trips[self.currentTripNum]
    
    def printDashData(self):
        currentTrip = self.trips[self.currentTripNum]
        
        print(f"Current Trip Num: {self.currentTripNum}")
        for key in currentTrip:
            print(f"{str(key)}: {currentTrip[str(key)]}")
=======

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
>>>>>>> master
