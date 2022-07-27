# from threading import Condition
import time
import random
from queue import Queue

# ADT IMPORTS
from entity import Entity
from Calculators import *

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
# This CLK represents: @always(posedge)
# ___---___---___---___ sync clock


class CLKWriter(Entity.Writer):
    def __init__(self,
                 ddsDataArray: list,
                 clockPeriod: float):

        self.__clockPeriod = clockPeriod
        self.__stopFlag = False
        super().__init__(ddsDataArray)

    def write(self) -> None:
        index = self.getIndex()
        data = self.getData()
        writer = self.getWriter()

        if self.__stopFlag:
            clk = 2
            print(f"Stop signal sent : {clk}\n")
        else:
            # makes this a boolean value that alternates
            clk = int(index % 2)

        # UPDATING MESSAGE CONTENTS
        data.clk(clk)
        data.index(index)
        writer.write(data)
        self.setIndex()

    def printData(self) -> None:
        data = self.getData()
        index = data.index()
        clk = data.clk()

        print(f"[index, clk] : {index}, {clk}\n")

    def run(self) -> None:
        while True:
            self.write()
            self.printData()
            time.sleep(self.__clockPeriod)

    def setStopSignal(self, value: bool) -> None:
        self.__stopFlag = value
        self.write()
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class FuelWriter(Entity.Writer):
    def __init__(self,
                 ddsDataArray: list,
                 CalculationClass: type):

        self.__CalculationClass = CalculationClass
        self.__stopFlag = False
        super().__init__(ddsDataArray)

    def write(self) -> None:
        index = self.getIndex()
        data = self.getData()
        writer = self.getWriter()

        fuelRemain, fuelSpent = self.__CalculationClass.consumeFuel(self.__stopFlag)

        if self.__stopFlag:
            print(f"Stop signal sent : {fuelRemain}, {fuelSpent}\n")

        # UPDATING MESSAGE CONTENTS
        data.litersRemaining(float(fuelRemain))
        data.litersSpent(float(fuelSpent))
        data.index(index)

        writer.write(data)
        self.setIndex()

    def printData(self) -> None:
        data = self.getData()
        index = data.index()
        fuelRemain = data.litersRemaining()
        fuelSpent = data.litersSpent()
        print(f"[index, spent, remain] : {index}, {fuelSpent:.2f}, {fuelRemain:.2f}\n")

    def run(self,
            edge: Queue) -> None:
        while True:
            currentEdge = edge.get()[1]
            if currentEdge:
                self.write()
                self.printData()
            else:
                pass

    def setStopSignal(self, value: bool) -> None:
        self.__stopFlag = value
        self.write()

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class MilesWriter(Entity.Writer):
    def __init__(self,
                 ddsDataArray: list,
                 CalculationClass: type):

        self.__CalculationClass = CalculationClass

        super().__init__(ddsDataArray)

    def write(self,
              fuelQueue: Queue) -> None:
        index = self.getIndex()
        data = self.getData()
        writer = self.getWriter()

        milesTraveled = self.__CalculationClass.addMiles(fuelQueue)

        # UPDATING MESSAGE CONTENTS
        data.index(index)
        data.milesTraveled(milesTraveled)

        writer.write(data)
        self.setIndex()

    def printData(self) -> None:
        data = self.getData()
        index = data.index()
        milesTraveled = data.milesTraveled()
        print(f"[index, milesTraveled] : {index}, {milesTraveled:.2f}\n")

    def run(self,
            fuelQueue: Queue,
            edge: Queue) -> None:
        while True:
            if edge.get()[1]:
                self.write(fuelQueue)
                self.printData()
            else:
                pass

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class LowFuelWriter(Entity.Writer):
    def __init__(self,
                 ddsDataArray: list,
                 CalculationClass: type):

        self.__CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self,
              fuelQueue: Queue) -> None:
        index = self.getIndex()
        data = self.getData()
        writer = self.getWriter()

        lowFuelFlag = self.__CalculationClass.lowFuelAlert(fuelQueue)

        # UPDATING MESSAGE CONTENTS
        data.isFuelLow(lowFuelFlag)
        data.index(index)
        writer.write(data)

        self.setIndex()

    def printData(self) -> None:
        data = self.getData()
        index = data.index()
        isFuelLow = bool(data.isFuelLow())
        print(f"[index, isFuelLow]: {index}, {isFuelLow}\n")

    def run(self,
            fuelQueue: Queue,
            edge: Queue) -> None:
        while True:
            if edge.get()[1]:
                self.write(fuelQueue)
                self.printData()
            else:
                pass

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class MpGWriter(Entity.Writer):
    def __init__(self,
                 ddsDataArray: list,
                 CalculationClass: type):

        self.__CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self,
              fuelQueue: Queue,
              milesQueue: Queue) -> None:
        index = self.getIndex()
        data = self.getData()
        writer = self.getWriter()

        mpgData = self.__CalculationClass.calculateMpG(fuelQueue, milesQueue)
        data.mpg(mpgData)
        data.index(index)
        writer.write(data)

        self.setIndex()

    def printData(self):
        data = self.getData()
        index = data.index()
        mpg = data.mpg()
        print(f"[index, MpG] : {index}, {mpg} \n")

    def run(self,
            fuelQueue: Queue,
            milesQueue: Queue,
            edge: Queue) -> None:

        while True:
            if edge.get()[1]:
                self.write(fuelQueue, milesQueue)
                self.printData()
            else:
                pass


############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class MilesRemaining(Entity.Writer):
    def __init__(self,
                 ddsDataArray: list,
                 CalculationClass: type):

        self.__CalculationClass = CalculationClass
        super().__init__(ddsDataArray)

    def write(self,
              fuelQueue: Queue,
              mpgQueue: Queue) -> None:
        index = self.getIndex()
        data = self.getData()
        writer = self.getWriter()

        milesRemaining = self.__CalculationClass.calculateMpG(fuelQueue, mpgQueue)

        data.index(index)
        data.milesToRefuel(milesRemaining)
        writer.write(data)

        self.setIndex()

    def printData(self) -> None:
        data = self.getData()
        index = data.index()
        milesToRefuel = data.milesToRefuel()
        print(f"[index, milesToRefuel] : {index}, {milesToRefuel} \n")

    def run(self,
            fuelQueue: Queue,
            mpgQueue: Queue,
            edge: Queue) -> None:
        while True:
            if edge.get()[1]:
                self.write(fuelQueue, mpgQueue)
                self.printData()
            else:
                pass
