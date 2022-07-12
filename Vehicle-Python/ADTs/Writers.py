# from threading import Condition
import time
import random

#ADT IMPORTS
from entity import Entity  
from Calculators import *

global_sleep_time          = float(0.25)
global_sleep_time_buffered = global_sleep_time + float(0.03)
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
class FuelWriter(Entity.Writer):
    def __init__(self, ddsDataArray, CalculationClass):

        self.CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self, stop_flag):
        
        # UPDATING MESSAGE CONTENTS
        dataOutput = self.CalculationClass.consumeFuel(stop_flag)
        self.data.litersRemaining(float(dataOutput[0]))
        self.data.litersSpent(float(dataOutput[1]))
        self.data.index(self.index)

        self.writer.write(self.data)
        print(f"{self.index}, {dataOutput[0]}, {dataOutput[1]} \n")
        self.index = self.index + 1

    def run(self, stop_flag) -> None: 
        #self.wait_discovery()
        while True:
            self.write(stop_flag)
            time.sleep(global_sleep_time)

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
            time.sleep(global_sleep_time)    # Report every 0.25 s
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

    def write(self, fuelQueue):
        lowFuel = LowFuelCalc(50)
        alert = lowFuel.lowFuelAlert(fuelQueue.get()[1])
        # UPDATING MESSAGE CONTENTS
        self.data.isFuelLow(alert)
        self.data.index(self.index)
        self.writer.write(self.data)
        print(f"Low Fuel: {self.data.index()}, {bool(self.data.isFuelLow())}\n")
            
        self.index = self.index + 1

    def run(self, fuelQueue):
        #self.wait_discovery()
        while True:
            self.write(fuelQueue)
            time.sleep(global_sleep_time)
            
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
        mpgCalc = MpGCalc()

        self.data.index(self.index)
        self.data.mpg(mpgCalc.calculateMpG(fuelQueue, milesQueue))
        
        self.writer.write(self.data)
        
        print(f"MpG: {self.data.index()}, {self.data.mpg()} \n")
        self.index = self.index + 1
            
            
    def run(self, fuelQueue, milesQueue):
        #self.wait_discovery()
        while True:
            self.write(fuelQueue, milesQueue)
            time.sleep(global_sleep_time_buffered)
  
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class MilesRemaining(Entity.Writer):
    def __init__(self, ddsDataArray): #, CalculationClass):

        #self.CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self, fuelQueue, mpgQueue):

        milesRemainCalc = MileRemainCalc()
        
        self.data.index(self.index)
        self.data.milesToRefuel(milesRemainCalc.calculateMpG(fuelQueue, mpgQueue))
        self.writer.write(self.data)
        
        if not fuelQueue.empty() or not mpgQueue.empty():
            print(f"MilesToRefuel: {self.data.index()}, {self.data.milesToRefuel()} \n")
        else:
            print("MilesToRefuel:")
            
        self.index = self.index + 1
            
            
    def run(self, fuelQueue, mpgQueue):
        #self.wait_discovery()
        while True:
            self.write(fuelQueue, mpgQueue)
            time.sleep(global_sleep_time_buffered)

