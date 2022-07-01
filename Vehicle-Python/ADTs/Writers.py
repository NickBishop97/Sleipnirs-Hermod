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
    #def __init__(self, ddsDataArray, FuelConsump):

        self.total_fuel = 100.0
        self.fuel_change_rate = 0
        super().__init__(ddsDataArray)
        self.CalculationClass = CalculationClass

    def write(self):
        dataOutput = self.CalculationClass.consumeFuel(random.uniform(0.01, 0.2))
        #dataOutput = self.FuelConsump.consumeFuel(random.uniform(0.01, 0.2))
        # UPDATING MESSAGE CONTENTS
        self.data.message(f"{dataOutput}")
        self.data.index(self.index)

        self.writer.write(self.data)
        print("{index}, {message}\n".format(message=self.data.message(), index=self.data.index()))
        self.index = self.index + 1

    def run(self):
        self.wait_discovery()
        while True:
            self.write()
            time.sleep(0.25)

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class MilesWriter(Entity.Writer):
    def __init__(self, ddsDataArray, CalculationClass):
        super().__init__(ddsDataArray)
        self.CalculationClass = CalculationClass

    def write(self, stopMoving):
        # UPDATING MESSAGE CONTENTS
        self.data.message(str(self.CalculationClass.milesTraveled))
        self.data.index(self.index)
        self.writer.write(self.data)
        print("{index}: {message}\n".format(index=self.data.index(), message=self.data.message()))
        self.index += 1

        # WRITE STATE UPDATE
        if stopMoving.milesStopper:
            self.CalculationClass.milesTraveled += 0
        else:
            self.CalculationClass.milesTraveled += random.uniform(1, 2)

    def run(self, stopMoving):
        self.wait_discovery()
        while True:
            self.write(stopMoving)
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
        print("{index}, {message}\n".format(message=self.data.message(), index=self.data.index()))
        self.index = self.index + 1

    def run(self, alertStatus):
        self.wait_discovery()
        while True:
            self.write(alertStatus)
            time.sleep(0.25)