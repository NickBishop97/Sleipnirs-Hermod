import time
import random

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