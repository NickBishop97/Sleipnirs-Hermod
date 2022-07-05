# from threading import Condition
import time
import random

#ADT IMPORTS
from entity import Entity  
from Calculators import *

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
class FuelWriter(Entity.Writer):
    def __init__(self, ddsDataArray, CalculationClass):

        self.CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self, test_flag):
        
        # UPDATING MESSAGE CONTENTS
        dataOutput = self.CalculationClass.consumeFuel(test_flag)
        self.data.litersRemaining(float(dataOutput[0]))
        self.data.litersSpent(float(dataOutput[1]))
        self.data.index(self.index)

        self.writer.write(self.data)
        print(f"{self.index}, {dataOutput[0]}, {dataOutput[1]} \n")
        self.index = self.index + 1

    def run(self, test_flag) -> None: 
        #self.wait_discovery()
        while True:
            self.write(test_flag)
            time.sleep(0.25)

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
class MilesWriter(Entity.Writer):
    def __init__(self, ddsDataArray, CalculationClass):
        self.CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self, startStopCondition):
        # UPDATING MESSAGE CONTENTS
        self.CalculationClass.addMiles(startStopCondition)
        self.data.milesTraveled(float(self.CalculationClass.milesTraveled))
        self.data.index(self.index)
        self.writer.write(self.data)
        
        print(f"MILES TRAVELED: {self.data.index()}, {self.data.milesTraveled()}\n")
        self.index += 1

    def run(self, startStopCondition):
        #self.wait_discovery()
        while True:
            self.write(startStopCondition)
            time.sleep(0.25)    # Report every 0.25 s
            # 25 MPH = 0.001 miles in 0.25 s
            # 85 MPH = 0.006 miles in 0.25 s

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class LowFuelWriter(Entity.Writer):
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)

    def write(self, alertStatus):
        
        # UPDATING MESSAGE CONTENTS
        self.data.message(f"{alertStatus}")
        self.data.index(self.index)

        self.writer.write(self.data)
        #print("{index}, {message}\n".format(message=self.data.message(), index=self.data.index()))
        self.index = self.index + 1

    def run(self, alertStatus):
        #self.wait_discovery()
        while True:
            self.write(alertStatus)
            time.sleep(0.25)
            
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class MpGWriter(Entity.Writer):
    def __init__(self, ddsDataArray): #, CalculationClass):

        #self.CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self, fuelQueue, milesQueue):
        fuelDatum = 0
        milesDatum = 0

        if not fuelQueue.empty():
            fuelDatum  = fuelQueue.get()[2]
            
        if not milesQueue.empty():
            milesDatum  = milesQueue.get()
        
        if not fuelDatum == 0:
            temp = float(milesDatum)/float(fuelDatum)
            
            self.data.index(self.index)
            self.data.mpg(temp)
            print(f"MpG: {self.index}, {temp} \n")
        
        elif fuelDatum == 0:
            self.data.index(self.index)
            self.data.mpg(float(-1))
            print(f"MpG: {self.index}, {-1} \n")

        self.index = self.index + 1
            
            
    def run(self, fuelQueue, milesQueue):
        #self.wait_discovery()
        while True:
            self.write(fuelQueue, milesQueue)
            time.sleep(0.3)
  