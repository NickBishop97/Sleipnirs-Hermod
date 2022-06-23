from entity import Entity
import HelloWorld  # my <idl file>
# from threading import Condition
import time
import random
# import fastdds


class Fuel(Entity.Writer):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
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
writerOne = Fuel(HelloWorld, "HelloWorld", "FuelRemaining")
#writerTwo = Fuel(HelloWorld, "HelloWorld", "FuelSpent")
writerOne.run()
exit()
