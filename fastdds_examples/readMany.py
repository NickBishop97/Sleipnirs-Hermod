#from msilib.schema import Class
#from pkgutil import get_data
from threading import Thread
from entity import Entity
import fastdds
import signal
import time

import sys
sys.path.insert(0, 'HelloWorld/')
import HelloWorld

sys.path.insert(1, 'Fuel')
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
            
    def run(self):
        signal.signal(signal.SIGINT, 
                        lambda sig, frame : (
                            print("\nInterrupted!\n"),
                            exit(),
                        )
                    )

        print('Press Ctrl+C to stop')

        if self.controlSignal():
            self.delete()
            exit()
            
        signal.pause()
        self.delete()
        
class FuelRL(Entity.ReaderListener):
    def __init__(self, data, realTimeInput):
            self.data          = data
            self.dataReturn    = 0 
            self.realTimeInput = realTimeInput
            super().__init__(data)
         
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
        #dataArray = tempStr.split(", ")

        #print("Fuel Left:" + dataArray[1])
        #print("Percentage remaining: " + str(round(100 * (float(dataArray[1])/100.0), 1)) + "%")
        self.realTimeWrite.counter1 = data.message()

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
def controlSignal():
    time.sleep(30)
    return True

#1) CREATE THE RUN FUNCTIONS TO ACCUMULATE DATA ON SHARED MEMORY

shared_helloData = 0
shared_fuelData  = 0

#2) CREATE A FUNCTION THAT IS CALLED TO DO THE CALCULATION IN A SEPARATE THREAD

def calculateInThread(counter1, counter2, rate):
    time.sleep(rate)
    if counter1 != 0:
        print(f"{counter2 / counter2}\n")
    else: 
        print("0\n")
    
    #After calculating over the interval specified, reset
    #This is in shared memory so the data is actually by reference
    
class counter1:    
    counter1 = 0
class counter2:
    counter2 = 0

#3) CREATE THE THREADS AND ADD THE ARGS

#Needs to feed .run() and give run args

readerFuel  = FuelGauge(Fuel, "Fuel", "FuelRemaining", FuelRL(Fuel, counter1), controlSignal)
#readerHello = Hello(HelloWorld, "HelloWorld", "HelloWorldTopic1846", HelloRL)

threadFuel  = Thread(target=(readerFuel.run), args=())
#threadHello = Thread(target=(readerHello.run), args=(shared_helloData))
#threadCalculate = Thread

threadFuel.start()
#threadHello.start()


print(counter1.counter1)
exit()
