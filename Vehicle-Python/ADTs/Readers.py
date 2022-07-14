from threading import Thread
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

        super().__init__()

    def on_subscription_matched(self, datareader, info):
        if (0 < info.current_count_change):
            print("Subscriber matched publisher {}".format(info.last_publication_handle))
        else:
            print("Subscriber unmatched publisher {}".format(info.last_publication_handle))

    def on_data_available(self, reader):

        self.connectionStatus.connected = True

        info = fastdds.SampleInfo()
        data = self.data
        reader.take_next_sample(data, info)
        # print(f"[FUEL: REMAINING, SPENT]: {data.index()}, {data.litersRemaining()}, {data.litersSpent()}")
        self.dataQueue.put([data.index(),
                            data.litersRemaining(),
                            data.litersSpent()])

    def getConnectionStatus(self):
        return self.connectionStatus

    def getDataReturn(self):
        return self.dataQueue

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
            if not self.dataQueue.empty():
                self.dataQueue = self.listener.getDataReturn()
            else:
                return None

    def run(self):
        dataThread = Thread(target=(self.dataRunReturn), daemon=True)
        dataThread.start()


class DistanceRL(Entity.ReaderListener):
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
                            data.milesToRefuel()])

    def getDataReturn(self):
        return self.dataQueue
