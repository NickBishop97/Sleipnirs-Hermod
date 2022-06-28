# from threading import Condition
import time
import random

from entity import Entity

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class FuelWriter(Entity.Writer):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name

        self.total_fuel = 100.0
        self.fuel_change_rate = 0
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name)

    def write(self):
        if self.total_fuel <= 0:
            self.fuel_change_rate = 0
            self.total_fuel = 0

        # UPDATING MESSAGE CONTENTS
        self.data.message(str(round(self.fuel_change_rate, 1)) + ", " + str(round(self.total_fuel, 1)))
        self.data.index(self.index)

        self.writer.write(self.data)
        print("{index}, {message}\n".format(message=self.data.message(), index=self.data.index()))
        self.index = self.index + 1

        # WRITE STATE UPDATE
        if self.total_fuel > 0:
            self.fuel_change_rate = random.uniform(0.01, 0.2)
            self.total_fuel -= self.fuel_change_rate

    def run(self):
        self.wait_discovery()
        while True:
            self.write()
            time.sleep(0.25)

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


class MilesWriter(Entity.Writer):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name

        self.milesTraveled = 0.0
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name)

    def write(self, stopMoving):
        # UPDATING MESSAGE CONTENTS
        self.data.message(str(self.milesTraveled))
        self.data.index(self.index)
        self.writer.write(self.data)
        print("{index}: {message}\n".format(index=self.data.index(), message=self.data.message()))
        self.index += 1

        # WRITE STATE UPDATE
        if stopMoving.milesStopper:
            self.milesTraveled += 0
        else:
            self.milesTraveled += random.uniform(1, 2)

    def run(self, stopMoving):
        self.wait_discovery()
        while True:
            self.write(stopMoving)
            time.sleep(0.25)    # Report every 0.25 s
            # 25 MPH = 0.001 miles in 0.25 s
            # 85 MPH = 0.006 miles in 0.25 s

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
