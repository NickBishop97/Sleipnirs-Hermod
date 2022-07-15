# from threading import Condition
import time
import random
from queue import Queue

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
        self.__stopFlag = False
        self.__CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self, stop_flag):
        
        # UPDATING MESSAGE CONTENTS
        dataOutput = self.__CalculationClass.consumeFuel(self.__stopFlag)
        self.__data.litersRemaining(float(dataOutput[0]))
        self.__data.litersSpent(float(dataOutput[1]))
        self.__data.index(self.__index)

        self.writer.write(self.__data)
        print(f"{self.__index}, {dataOutput[0]}, {dataOutput[1]} \n")
        self.__index = self.__index + 1

    def run(self, stop_flag : bool) -> None: 
        #self.wait_discovery()
        while True:
            self.write(stop_flag)
            time.sleep(global_sleep_time)
            
    def stopSignalReceived(self, value : bool):
        self.__stopFlag = value

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
class MilesWriter(Entity.Writer):
    def __init__(self, ddsDataArray, CalculationClass):
        self.__CalculationClass   = CalculationClass
        super().__init__(ddsDataArray)

    def write(self, fuelQueue : Queue)  -> None:
        # UPDATING MESSAGE CONTENTS
        self.__CalculationClass.addMiles(fuelQueue)
        self.__data.milesTraveled(float(self.__CalculationClass.milesTraveled))
        self.__data.index(self.__index)
        self.writer.write(self.__data)
        
        print(f"MILES TRAVELED: {self.__data.index()}, {self.__data.milesTraveled()}\n")
        self.__index += 1

    def run(self, fuelQueue : Queue) -> None:
        #self.wait_discovery()
        while True:
            self.write(fuelQueue)
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
        self.__data.isFuelLow(alert)
        self.__data.index(self.__index)
        self.writer.write(self.__data)
        print(f"Low Fuel: {self.__data.index()}, {bool(self.__data.isFuelLow())}\n")
            
        self.__index = self.__index + 1

    def run(self, fuelQueue) -> None:
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

        #self.__CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self, fuelQueue, milesQueue) -> None:
        mpgCalc = MpGCalc()

        self.__data.index(self.__index)
        self.__data.mpg(mpgCalc.calculateMpG(fuelQueue, milesQueue))
        
        self.writer.write(self.__data)
        
        print(f"MpG: {self.__data.index()}, {self.__data.mpg()} \n")
        self.__index = self.__index + 1
            
            
    def run(self, fuelQueue, milesQueue) -> None:
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

        #self.__CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self, fuelQueue, mpgQueue) -> None:

        milesRemainCalc = MileRemainCalc()
        
        self.__data.index(self.__index)
        self.__data.milesToRefuel(milesRemainCalc.calculateMpG(fuelQueue, mpgQueue))
        self.writer.write(self.__data)
        
        if not fuelQueue.empty() or not mpgQueue.empty():
            print(f"MilesToRefuel: {self.__data.index()}, {self.__data.milesToRefuel()} \n")
        else:
            print("MilesToRefuel:")
            
        self.__index = self.__index + 1
            
            
    def run(self, fuelQueue, mpgQueue) -> None:
        #self.wait_discovery()
        while True:
            self.write(fuelQueue, mpgQueue)
            time.sleep(global_sleep_time_buffered)
            
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
class ButtonWriter(Entity.Writer):
    def __init__(self, ddsDataArray, CalculationClass): #, CalculationClass):

        self.__CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self) -> None:
        buttonCalc = self.__CalculationClass

        self.__data.index(self.__index)
        self.__data.button(buttonCalc.timedButton())
        
        self.writer.write(self.__data)
        
        print(f"Button: {self.__data.index()}, {self.__data.button()} \n")
        self.__index = self.__index + 1
            
            
    def run(self) -> None:
        #self.wait_discovery()
        while True:
            self.write()
            time.sleep(global_sleep_time_buffered)
    
""""            
class AvgSpeedWriter(Entity.Writer):
    def __init__(self, ddsDataArray): #, CalculationClass):

        #self.__CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self, timeQueue, milesQueue):
        speedCalc = SpeedCalc()

        self.__data.index(self.__index)
        self.__data.speed(SpeedCalc.calculateSpeed(timeQueue, milesQueue))
        
        self.writer.write(self.__data)
        
        print(f"MpG: {self.__data.index()}, {self.__data.speed()} \n")
        self.__index = self.__index + 1
            
            
    def run(self, fuelQueue, milesQueue):
        #self.wait_discovery()
        while True:
            self.write(fuelQueue, milesQueue)
            time.sleep(global_sleep_time_buffered)
"""