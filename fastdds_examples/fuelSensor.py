from threading import Condition
import time
import random

from entity import Entity
import sys
sys.path.insert(0, './Fuel/')
import Fuel as F

sys.path.insert(0, './HelloWorld/')
import HelloWorld

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

        self.data.message(str(round(self.total_spent, 1)) + ", " + str(round(self.total_fuel, 1)))
        self.data.index(self.index)
        self.writer.write(self.data)
        print("{index}, {message}".format(message=self.data.message(), index=self.data.index()))
        self.index = self.index + 1

        self.total_fuel -= self.fuel_change_rate
        self.total_spent = self.fuel_change_rate
        self.fuel_change_rate = random.randrange(5.0, 10.0)


    def run(self):
        self.wait_discovery()
        for x in range(10) :
            time.sleep(1)
            self.write()
        self.delete()



print('\nStarting publisher.')
writerOne = Fuel(F, "Fuel", "FuelRemaining")
writerOne.run()
exit()
