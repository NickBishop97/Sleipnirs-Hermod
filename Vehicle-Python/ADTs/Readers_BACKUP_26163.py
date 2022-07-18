<<<<<<< HEAD
from threading import Thread    
=======
from threading import Thread
>>>>>>> master
from entity import Entity
import fastdds
from queue import Queue

# import sys
# sys.path.insert(1, './Fuel')
# import Fuel
# sys.path.insert(1, './Miles/')
# import Miles as M

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class FuelGauge(Entity.Reader):
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)

<<<<<<< HEAD
class FuelRL(Entity.ReaderListener):
    def __init__(self, data):
        self.__data = data
        self.__dataQueue = Queue()
        
=======
        self.connected = self.listener.getConnectionStatus()

    def dataRunReturn(self):
        while True:
            if not self.dataQueue.empty():
                self.dataQueue = self.listener.getDataReturn()
                self.connected = self.listener.getConnectionStatus()
                # return (self.dataQueue, self.connected)
            else:
                return None

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()


class FuelRL(Entity.ReaderListener):
    def __init__(self, data):
        self.data = data
        self.dataQueue = Queue()

        class ConnectionStatus:
            def __init__(self):
                self.connected = False

        self.connectionStatus = ConnectionStatus()

>>>>>>> master
        super().__init__()

    def on_subscription_matched(self, datareader, info):
        if (0 < info.current_count_change):
            print("Subscriber matched publisher {}".format(info.last_publication_handle))
        else:
            print("Subscriber unmatched publisher {}".format(info.last_publication_handle))

    def on_data_available(self, reader):
<<<<<<< HEAD
        
=======

        self.connectionStatus.connected = True

>>>>>>> master
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)
<<<<<<< HEAD
        #print(f"[FUEL: REMAINING, SPENT]: {__data.index()}, {__data.litersRemaining()}, {__data.litersSpent()}")
        self.__dataQueue.put([data.index(), 
                            data.litersRemaining(),
                            data.litersSpent()])
    
    def getDataReturn(self):
        return self.__dataQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class DistanceDisplay(Entity.Reader):
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)
    
    def dataRunReturn(self):
        while True:
            if not self.__dataQueue.empty():
                self.__dataQueue = self.listener.getDataReturn()
            else:
                return None

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()

class DistanceRL(Entity.ReaderListener):
    def __init__(self, data):
        self.__data = data
        self.__dataQueue = Queue()
        super().__init__()

    def on_subscription_matched(self, datareader, info):
        if(0 < info.current_count_change):
            print("Subscriber matched publisher {}".format(info.last_publication_handle))
        else:
            print("Subscriber unmatched publisher {}".format(info.last_publication_handle))
            # exit()

    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)

        #print(f"[DISTANCE TRAVELED]: {__data.index()}, {data.milesTraveled()}")
        self.__dataQueue.put([data.index(),
                            data.milesTraveled()])
=======
        # print(f"[FUEL: REMAINING, SPENT]: {data.index()}, {data.litersRemaining()}, {data.litersSpent()}")
        self.dataQueue.put([data.index(),
                            data.litersRemaining(),
                            data.litersSpent()])

    def getConnectionStatus(self):
        return self.connectionStatus
>>>>>>> master

    def getDataReturn(self):
        return self.__dataQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

<<<<<<< HEAD
class MpGDisplay(Entity.Reader):
=======

class DistanceDisplay(Entity.Reader):
>>>>>>> master
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)
    
    def dataRunReturn(self):
        while True:
            if not self.__dataQueue.empty():
                self.__dataQueue = self.listener.getDataReturn()
            else:
                return None

<<<<<<< HEAD
    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()
=======
    def dataRunReturn(self):
        while True:
            if not self.dataQueue.empty():
                self.dataQueue = self.listener.getDataReturn()
            else:
                return None

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()

>>>>>>> master

class MpGRL(Entity.ReaderListener):
    def __init__(self, data):
        self.__data = data
        self.__dataQueue = Queue()
        super().__init__()

    def on_subscription_matched(self, datareader, info):
        if(0 < info.current_count_change):
            print("Subscriber matched publisher {}".format(info.last_publication_handle))
        else:
            print("Subscriber unmatched publisher {}".format(info.last_publication_handle))
            # exit()

    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)
        #print(f"[MPG]: {__data.index()}, {float(__data.mpg())}")
        self.__dataQueue.put([data.index(),
                            float(data.mpg())])

    def getDataReturn(self):
        return self.__dataQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class LowFuelAlertDisplay(Entity.Reader):
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)
    
    def dataRunReturn(self):
        while True:
            if not self.__dataQueue.empty():
                self.__dataQueue = self.listener.getDataReturn()
            else:
                return None

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()

class LowFuelAlertRL(Entity.ReaderListener):
    def __init__(self, data):
<<<<<<< HEAD
        self.__data = data
        self.__dataQueue = Queue()
=======
        self.data = data
        self.dataQueue = Queue()
>>>>>>> master
        super().__init__()

    def on_subscription_matched(self, datareader, info):
        if(0 < info.current_count_change):
            print("Subscriber matched publisher {}".format(info.last_publication_handle))
        else:
            print("Subscriber unmatched publisher {}".format(info.last_publication_handle))
            # exit()

    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)
        
        #print(f"[LOW FUEL]: {__data.index()}, {bool(__data.isFuelLow())}")
        self.__dataQueue.put([data.index(),
                            bool(data.isFuelLow())])

    def getDataReturn(self):
        return self.__dataQueue
    
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
class MilesRemainDisplay(Entity.Reader):
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)
    
    def dataRunReturn(self):
        while True:
            if not self.__dataQueue.empty():
                self.__dataQueue = self.listener.getDataReturn()
            else:
                return None

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()

class MilesRemainRL(Entity.ReaderListener):
    def __init__(self, data):
        self.__data = data
        self.__dataQueue = Queue()
        super().__init__()

    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)
        
        #print(f"[MILES REMAIN]: {__data.index()}, {__data.milesToRefuel()}")
        self.__dataQueue.put([data.index(),
                            data.milesToRefuel()])

    def getDataReturn(self):
        return self.__dataQueue
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
class MilesRemainDisplay(Entity.Reader):
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)
    
    def dataRunReturn(self):
        while True:
            if not self.__dataQueue.empty():
                self.__dataQueue = self.listener.getDataReturn()
            else:
                return None

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()

class MilesRemainRL(Entity.ReaderListener):
    def __init__(self, data):
        self.__data = data
        self.__dataQueue = Queue()
        super().__init__()

    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.__data
        reader.take_next_sample(data, info)
<<<<<<< HEAD
        
        #print(f"[MILES REMAIN]: {__data.index()}, {__data.milesToRefuel()}")
        self.__dataQueue.put([data.index(),
=======
        # milesTraveled = float(data.milesTraveled())
        # print(f"[DISTANCE TRAVELED]: {data.index()}, {milesTraveled}")
        self.dataQueue.put([data.index(),
                            data.milesTraveled()])

    def getDataReturn(self):
        return self.dataQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class MpGDisplay(Entity.Reader):
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)

    def dataRunReturn(self):
        while True:
            if not self.dataQueue.empty():
                self.dataQueue = self.listener.getDataReturn()
            else:
                return None

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()


class MpGRL(Entity.ReaderListener):
    def __init__(self, data):
        self.data = data
        self.dataQueue = Queue()
        super().__init__()

    def on_subscription_matched(self, datareader, info):
        if(0 < info.current_count_change):
            print("Subscriber matched publisher {}".format(info.last_publication_handle))
        else:
            print("Subscriber unmatched publisher {}".format(info.last_publication_handle))
            # exit()

    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.data
        reader.take_next_sample(data, info)
        # print(f"[MPG]: {data.index()}, {float(data.mpg())}")
        self.dataQueue.put([data.index(),
                            float(data.mpg())])

    def getDataReturn(self):
        return self.dataQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class LowFuelAlertDisplay(Entity.Reader):
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)

    def dataRunReturn(self):
        while True:
            if not self.dataQueue.empty():
                self.dataQueue = self.listener.getDataReturn()
            else:
                return None

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()


class LowFuelAlertRL(Entity.ReaderListener):
    def __init__(self, data):
        self.data = data
        self.dataQueue = Queue()
        super().__init__()

    def on_subscription_matched(self, datareader, info):
        if(0 < info.current_count_change):
            print("Subscriber matched publisher {}".format(info.last_publication_handle))
        else:
            print("Subscriber unmatched publisher {}".format(info.last_publication_handle))
            # exit()

    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.data
        reader.take_next_sample(data, info)

        # print(f"[LOW FUEL]: {data.index()}, {bool(data.isFuelLow())}")
        self.dataQueue.put([data.index(),
                            bool(data.isFuelLow())])

    def getDataReturn(self):
        return self.dataQueue

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class MilesRemainDisplay(Entity.Reader):
    def __init__(self, ddsDataArray):
        super().__init__(ddsDataArray)

    def dataRunReturn(self):
        while True:
            if not self.dataQueue.empty():
                self.dataQueue = self.listener.getDataReturn()
            else:
                return None

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()


class MilesRemainRL(Entity.ReaderListener):
    def __init__(self, data):
        self.data = data
        self.dataQueue = Queue()
        super().__init__()

    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.data
        reader.take_next_sample(data, info)

        # print(f"[MILES REMAIN]: {data.index()}, {data.milesToRefuel()}")
        self.dataQueue.put([data.index(),
>>>>>>> master
                            data.milesToRefuel()])

    def getDataReturn(self):
        return self.__dataQueue