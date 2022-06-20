from threading import Thread
from entity import Entity
import fastdds
import signal

import sys
sys.path.insert(0, '/home/n13853/n13853/dev/sleipnir/fastdds_examples/HelloWorld/')
import HelloWorld

sys.path.insert(1, '/home/n13853/n13853/dev/sleipnir/fastdds_examples/Fuel/')
import Fuel

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class FuelGauge(Entity.Reader):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name, myReaderListener):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        self.ReaderListener = myReaderListener
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name, myReaderListener)

class FuelRL(Entity.ReaderListener):
    def __init__(self, data):
            self.data = data
            super().__init__(data)


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

        print("Fuel Left:" + dataArray[1])
        print("Percentage remaining: " + str(round(100 * (float(dataArray[1])/100.0), 1)) + "%")

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
class Hello(Entity.Reader):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name, myReaderListener):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        self.ReaderListener = myReaderListener
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name, myReaderListener)

class HelloRL(fastdds.DataReaderListener):

    def __init__(self, data):
        self.data = data
        super().__init__()


    def on_subscription_matched(self, datareader, info) :
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

readerFuel  = FuelGauge(Fuel, "Fuel", "FuelRemaining", FuelRL)
readerHello = Hello(HelloWorld, "HelloWorld", "HelloWorldTopic1846", HelloRL)

threadFuel  = Thread(target=(readerFuel.run()))
threadHello = Thread(target=(readerHello.run()))

threadHello.start()
threadFuel.start()


exit()
