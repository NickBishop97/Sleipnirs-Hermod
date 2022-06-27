from threading import Condition
import time
import random

from entity import Entity

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class Fuel(Entity.Writer):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        
        self.total_fuel = 100.0
        self.fuel_change_rate = 2.4
        self.total_spent = 0.0
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name)
        
    def write(self):
        #print("hello wrold")

        #UPDATING MESSAGE CONTENTS
        self.data.message(str(round(self.total_spent, 1)) + ", " + str(round(self.total_fuel, 1)))
        self.data.index(self.index)
        
        self.writer.write(self.data)
        print("{index}, {message}\n".format(message=self.data.message(), index=self.data.index()))
        self.index = self.index + 1

        #WRITE STATE UPDATE
        self.total_fuel -= self.fuel_change_rate
        self.total_spent = self.fuel_change_rate
        self.fuel_change_rate = random.randrange(5.0, 10.0)


    def run(self):
        self.wait_discovery()
        while self.total_fuel > 0:
            self.write()
            time.sleep(0.25)
        self.delete()
        
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

class Miles(Entity.Writer):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        
        self.milesTraveled = 0.0
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name)

    def write(self):
        #UPDATING MESSAGE CONTENTS
        self.data.message(str(self.milesTraveled))
        self.data.index(self.index)
        self.writer.write(self.data)
        print("{index}: {message}\n".format(index=self.data.index(), message=self.data.message()))
        self.index += 1
        
        #WRITE STATE UPDATE
        self.milesTraveled += random.uniform(0.001, 0.006)
        
    def run(self):
        self.wait_discovery()
        while True:
            self.write()
            time.sleep(0.25)    # Report every 0.25 s
            # 25 MPH = 0.001 miles in 0.25 s
            # 85 MPH = 0.006 miles in 0.25 s

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################

