from entity import Entity
import fastdds
import time
import sys

sys.path.insert(0, 'Miles/')
# import Miles as MT

#################################
#  Publisher Class Decleration  #
#################################


class DistanceDisplay(Entity.Reader):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name, myReaderListener, myControlSignal):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        self.ReaderListener = myReaderListener
        self.controlSignal = myControlSignal
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name, myReaderListener, myControlSignal)


class DistanceRL(Entity.ReaderListener):
    def __init__(self, data):
        self.data = data
        self.dataReturn = 0
        super().__init__(data)

    def on_subscription_matched(self, datareader, info):
        if (0 < info.current_count_change):
            print("Subscriber matched publisher {}".format(info.last_publication_handle))
        else:
            print("Subscriber unmatched publisher {}".format(info.last_publication_handle))
            # exit()

    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.data
        reader.take_next_sample(data, info)

        tempStr = data.message()
        dataArray = tempStr.split(", ")

        print("Fuel Left:" + dataArray[1])
        print("Percentage remaining: " + str(round(100 * (float(dataArray[1])/100.0), 1)) + "%")
        self.dataReturn = data.message()

    def getDataReturn(self):
        return self.dataReturn

#############################
#  Control Pulbisher Class  #
#############################


def controlSignal():
    time.sleep(30)
    return True


readerDistance = DistanceDisplay(MT, "Miles", "Miles Traveled", DistanceRL, controlSignal)

# code to display distance to sashboard
