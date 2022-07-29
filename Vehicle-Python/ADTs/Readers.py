from threading import Thread
from entity import Entity
import fastdds
from queue import Queue


class CLKDisplay(Entity.Reader):
    def __init__(self,
                 ddsDataArray: list):
        super().__init__(ddsDataArray)


class CLKRL(Entity.ReaderListener):
    def __init__(self,
                 data: type):
        self.__data = data
        self.__listenerQueue = Queue()
        super().__init__()

    def printData(self) -> None:
        data = self.__data
        index = data.index()
        clk = data.clk()
        print(f"[index, clk] {index}, {clk}\n")

    def on_data_available(self,
                          reader: type) -> None:
        data = self.__data
        info = fastdds.SampleInfo()
        reader.take_next_sample(data, info)

        # self.printData()
        self.__listenerQueue.put([data.index(), data.clk()])

    # The integer acts as a bool
    def getDataReturn(self) -> Queue:
        return self.__listenerQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class FuelGauge(Entity.Reader):
    def __init__(self,
                 ddsDataArray: list):
        super().__init__(ddsDataArray)


class FuelRL(Entity.ReaderListener):
    def __init__(self,
                 data: type):
        self.__data = data
        self.__listenerQueue = Queue()

        super().__init__()

    def printData(self) -> None:
        data = self.__data
        index = data.index()
        spent = data.litersSpent()
        remain = data.litersRemaining()
        print(f"[index, spent, remain] : {index}, {spent}, {remain}\n")

    def on_data_available(self,
                          reader: type) -> None:
        data = self.__data
        info = fastdds.SampleInfo()
        reader.take_next_sample(data, info)

        self.__listenerQueue.put([data.index(),
                                  data.litersSpent(),
                                  data.litersRemaining()])

    def getDataReturn(self) -> Queue:
        return self.__listenerQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class DistanceDisplay(Entity.Reader):
    def __init__(self,
                 ddsDataArray: list):
        super().__init__(ddsDataArray)


class DistanceRL(Entity.ReaderListener):
    def __init__(self, data):
        self.__data = data
        self.__listenerQueue = Queue()
        super().__init__()

    def printData(self) -> None:
        index = self.__data.index()
        milesTraveled = self.__data.milesTraveled()
        print(f"[index, spent, remain] : {index}, {milesTraveled}")

    def on_data_available(self,
                          reader: type) -> None:
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)

        self.printData()
        self.__listenerQueue.put([data.index(),
                                  data.milesTraveled()])

    def getDataReturn(self) -> Queue:
        return self.__listenerQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class MpGDisplay(Entity.Reader):
    def __init__(self, ddsDataArray: list):
        super().__init__(ddsDataArray)


class MpGRL(Entity.ReaderListener):
    def __init__(self, data):
        self.__data = data
        self.__listenerQueue = Queue()
        super().__init__()

    def printData(self) -> None:
        index = self.__data.index()
        mpg = self.__data.mpg()
        print(f"[index, mpg] : {index}, {mpg}")

    def on_data_available(self,
                          reader: type) -> None:
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)

        self.printData()
        self.__listenerQueue.put([data.index(),
                                  float(data.mpg())])

    def getDataReturn(self):
        return self.__listenerQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class LowFuelAlertDisplay(Entity.Reader):
    def __init__(self, ddsDataArray: list):
        super().__init__(ddsDataArray)


class LowFuelAlertRL(Entity.ReaderListener):
    def __init__(self, data):
        self.__data = data
        self.__listenerQueue = Queue()
        super().__init__()

    def printData(self) -> None:
        index = self.__data.index()
        isFuelLow = self.__data.isFuelLow()
        print(f"[index, mpg] : {index}, {isFuelLow}")

    def on_data_available(self,
                          reader: type) -> None:
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)

        self.printData()
        self.__listenerQueue.put([data.index(),
                                  bool(data.isFuelLow())])

    def getDataReturn(self) -> Queue:
        return self.__listenerQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class MilesRemainDisplay(Entity.Reader):
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()


class MilesRemainRL(Entity.ReaderListener):
    def __init__(self, data):
        self.__data = data
        self.__listenerQueue = Queue()
        super().__init__()

    def printData(self) -> None:
        index = self.__data.index()
        milesToRefuel = self.__data.milesToRefuel()
        print(f"[index, mpg] : {index}, {milesToRefuel}")

    def on_data_available(self,
                          reader: type) -> None:
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)

        self.printData()
        self.__listenerQueue.put([data.index(),
                                  data.milesToRefuel()])

    def getDataReturn(self) -> Queue:
        return self.__listenerQueue
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class MilesRemainDisplay(Entity.Reader):
    def __init__(self, ddsDataArray: list):
        super().__init__(ddsDataArray)


class MilesRemainRL(Entity.ReaderListener):
    def __init__(self, data):
        self.__data = data
        self.__listenerQueue = Queue()
        super().__init__()

    def printData(self) -> None:
        index = self.__data.index()
        milesToRefuel = self.__data.milesToRefuel()
        print(f"[index, mpg] : {index}, {milesToRefuel}")

    def on_data_available(self, reader: type):
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)

        self.printData()
        self.__listenerQueue.put([data.index(),
                                  data.milesToRefuel()])

    def getDataReturn(self) -> Queue:
        return self.__listenerQueue
