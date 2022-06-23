from entity import Entity
import fastdds
import signal
import time
from queue import Queue

import sys
sys.path.insert(0, '/home/n13853/n13853/dev/sleipnir/fastdds_examples/HelloWorld/')
import HelloWorld

sys.path.insert(1, '/home/n13853/n13853/dev/sleipnir/fastdds_examples/Fuel')
import Fuel

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class FuelGauge(Entity.Reader):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name, myReaderListener, myControlSignal):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        self.ReaderListener = myReaderListener
        self.controlSignal = myControlSignal
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name, myReaderListener, myControlSignal)
            

        
class FuelRL(Entity.ReaderListener):
    def __init__(self, data):
            self.data = data
            self.dataReturn    = 0 
            self.dataQueue = Queue()
            super().__init__()
         
    def getDataReturn(self):
        return self.dataReturn
       
    def on_subscription_matched(self, datareader, info) :
        if (0 < info.current_count_change) :
            print ("Subscriber matched publisher {}".format(info.last_publication_handle))
        else :
            print ("Subscriber unmatched publisher {}".format(info.last_publication_handle))
            #exit()
            
    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.data
        reader.take_next_sample(data, info)
        
        tempStr= data.message()
        dataArray = tempStr.split(", ")

        #print("Fuel Left:" + dataArray[1])
        #print("Percentage remaining: " + str(round(100 * (float(dataArray[1])/100.0), 1)) + "%")
        self.dataQueue.put(dataArray[1])
        
    def getDataReturn(self):
        return self.dataQueue
        
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
class Hello(Entity.Reader):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name, myReaderListener, myControlSignal):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        self.ReaderListener = myReaderListener
        self.controlSignal = myControlSignal
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name, myReaderListener, myControlSignal)

class HelloRL(fastdds.DataReaderListener):

    def __init__(self, data):
        self.data = data
        super().__init__()


    def on_subscription_matched(self, info) :
        if (0 < info.current_count_change) :
            print ("Subscriber matched publisher {}".format(info.last_publication_handle))
        else :
            print ("Subscriber unmatched publisher {}".format(info.last_publication_handle))


    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = HelloWorld.HelloWorld()
        reader.take_next_sample(data, info)

        print("\n\nReceived {message} : {index} \n\n".format(message=data.message(), index=data.index()))
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
