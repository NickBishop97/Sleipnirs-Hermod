import time
import random
from queue import Queue
from xmlrpc.client import Boolean


#NOTE THAT THESE ARE SELF DEFINED CLASSES, 
#EACH TYPE OF CLASS WILL BE DIFFERENT AND WILL HAVE DIFFERENT UNITS

class clkClac:
    def __init__(self):
        pass
    
    def edgeIsHigh(self, clkQueue):
        timeOut   = 0
        breakTime = 1000
        # do nothing until the queue is populated
        while clkQueue.empty():
            timeOut +=1
            if(timeOut == breakTime):
                break
        
        edge = clkQueue.get() 
        if edge == 1:
            return True
        else:
            return False

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class FuelConsump:
    #CAPACITY IS INPUTTED AS GALLONS
    def __init__(self, 
                 capacity : float, 
                 currentFuel : float,
                 delta : float):
        #for better precision, use numpy dtype float64
        self.__delta = float(delta)
        
        #self.__gallonToLiters     = float(3.785412) 
        
        self.__capacityGallons    = float(capacity)
        #self.__capacityLiters     = capacity * self.__gallonToLiters
        
        self.__currentFuelGallons = float(currentFuel)
        #self.__currentFuelLiters  = currentFuel * self.__gallonToLiters
        
    def consumeFuel(self, 
                    stop_flag : int) -> None:
        if stop_flag:
            return(-1, -1)
            
        change = self.__currentFuelGallons - self.__delta 
        if change <= 0:
            self.__currentFuelGallons = 0 
        elif change > 0:
            self.__currentFuelGallons = change
        else:
            self.__currentFuelGallons = 0
        return (self.__currentFuelGallons, 
                self.__capacityGallons - self.__currentFuelGallons)

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class DistTrav:
    def __init__(self, 
                 displacement : float,
                 delta : float):
        
        self.__milesTraveled = float(displacement)
        self.__delta         = float(delta)
        
    def addMiles(self, 
                 fuelQueue : Queue) -> float:
        #Fuel has not send data
        #if not startStopCondition.milesStarter:
        #    self.__milesTraveled = -1
        if not fuelQueue.empty():
            data = fuelQueue.get()
            #If the fuel guage is sending values <= 0, it is likely that the fuel tank is out
            #For an odometer, the state would be kept and a displacement would be calculated
            if float(data[1]) <= 0:
                return self.__milesTraveled
            else:
                self.__milesTraveled +=  self.__delta
                return self.__milesTraveled
        
        else:
            return self.__milesTraveled
    
    def setDelta(self, 
                 delta : float) -> None:
        self.__delta = delta
 
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
           
class LowFuelCalc:
    def __init__(self, 
                 threshold : float):
        self.__threshold = float(threshold)
        
        #__lowFuelAlertFlag acts as a bool in this case
        self.__lowFuelAlertFlag = 0
    
    #return __lowFuelAlertFlag acts as a bool
    def lowFuelAlert(self, 
                     fuelQueue : float) -> int:
        currentFuel = fuelQueue.get()[1]
        
        if currentFuel < self.__threshold:
            self.__lowFuelAlertFlag = 1
            return self.__lowFuelAlertFlag
        else:
            self.__lowFuelAlertFlag = 0
            return self.__lowFuelAlertFlag

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class MpGCalc:
    def __init__(self):
        self.__mpg = 0
    
    def calculateMpG(self, 
                     fuelQueue : Queue, 
                     milesQueue : Queue) -> float:
        fuelDatum = 0.0
        milesDatum = 0.0
        
        if not fuelQueue.empty():
            fuelDatum  = fuelQueue.get()[1]
            
        if not milesQueue.empty():
            milesDatum  = milesQueue.get()[1]
        
        if not fuelDatum == 0:
            self.__mpg = float(milesDatum / fuelDatum )
        
        elif fuelDatum <= 0:
            self.__mpg = float(-1)
            
        return self.__mpg
    
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
    
class MileRemainCalc:
    def __init__(self):
        self.__mileRemain = 0
    
    def calculateMpG(self, 
                     fuelQueue : Queue,
                     mpgQueue : Queue):
        fuelDatum = 0
        mpgDatum = 0

        if not fuelQueue.empty():
            fuelDatum = fuelQueue.get()[2]
            
        if not mpgQueue.empty():
            mpgDatum = mpgQueue.get()[1]
        
        self.__mileRemain = float(mpgDatum) * float(fuelDatum)
        
        return self.__mileRemain

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################    

class TripCalc:
    def __init__(self):
        self.__currentTripNum = 0
        self.__trip_dict = {
            "distance"         : 0,
            "fuel"             : 0,
            "time"             : 0,
            
            "averageSpeed"     : 0,
            "MpG"              : 0,
            
            "twoHours"         : False,
            "resetCounterDist" : 0,
            "resetCounterFuel" : 0,
            "resetCounterTime" : 0
        }
        self.__trips = [dict(self.__trip_dict), dict(self.__trip_dict)]
    
    def update(self, 
               queueArray : list) -> None:
        
        #using a for loop makes the code harder to read
        distance = queueArray[0].get()[1] 
        fuel     = queueArray[1].get()[1] #fuel spent
        time     = queueArray[2].get()[1] 
            
        for i in range(len(self.__trips)): 
            self.__trips[i]["distance"]  = distance - self.__trips[i]["resetCounterDist"]
            self.__trips[i]["fuel"]      = fuel     - self.__trips[i]["resetCounterFuel"]
            self.__trips[i]["time"]      = time     - self.__trips[i]["resetCounterTime"]
            
            #AVOID DIVISION BY TIME = 0
            if(time != 0):
                self.__trips[i]["averageSpeed"] = float(distance / time)
            else: 
                self.__trips[i]["averageSpeed"] = -1
            
            #AVOID DIVISION BY FUEL = 0
            if(fuel != 0):
                self.__trips[i]["MpG"] = float(distance / fuel)
            else: 
                self.__trips[i]["MpG"] = -1
            
            #TWO HOURS HAVE PASSED 
            if self.__trips[i]["time"] >= float(2):
                self.__trips[i]["twoHours"] = True

    def reset(self, 
              resetButton : bool) -> None:
        #deep copy
        currentTrip = self.__trips[self.__currentTripNum]
        
        #if long reset, reset all of the values
        if resetButton >= 3:
            blankDict = self.__trip_dict 
            
            #write a comment of the equation for this block
            blankDict["resetCounterDist"] += currentTrip["distance"]
            blankDict["resetCounterFuel"] += currentTrip["fuel"]
            blankDict["resetCounterTime"] += currentTrip["time"]
            
            #making the trip dict all zeros
            self.__trips[self.__currentTripNum] = blankDict
        
        #if a short reset, switch trips
        elif resetButton >=0 and resetButton < 3:
            self.__currentTripNum = (self.__currentTripNum + 1) % 2
        else:
            pass
         
        
