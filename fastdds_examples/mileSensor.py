import time
import random
from entity import Entity
import sys
sys.path.insert(0, './Miles/')
import Miles as M


class Miles(Entity.Writer):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name)
        self.milesTraveled = 0.0

    def clearSensor(self):
        self.milesTraveled = 0.0

    def write(self):
        self.data.message(str(self.milesTraveled))
        self.data.index(self.index)
        self.writer.write(self.data)
        print("{index}: {message}".format(index=self.data.index(), message=self.data.message()))
        self.index += 1

    def run(self):
        self.wait_discovery()
        while 1 == 1:
            self.write()
            time.sleep(0.25)    # Report every 0.25 s
            # 25 MPH = 0.001 miles in 0.25 s
            # 85 MPH = 0.006 miles in 0.25 s
            self.milesTraveled += random.uniform(0.001, 0.006)
        self.delete()


print("\nStarting Miles Traveled Sensor\n")
mileSensor = Miles(M, "Miles", "MilesTraveled")
mileSensor.run()
exit()
