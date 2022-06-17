from entity import Entity
import HelloWorld #my <idl file>
from threading import Condition
import time

class Fuel(Entity.Writer):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name)
        
    def write(self):
       # print("hello wrold")
        
        self.data.message("Hello World")
        self.data.index(self.index)
        self.writer.write(self.data)
        print("Sending {message} : {index}".format(message=self.data.message(), index=self.data.index()))
        self.index = self.index + 1

    def run(self):
        self.wait_discovery()
        for x in range(10) :
            time.sleep(1)
            self.write()
        self.delete()

print('\nStarting publisher.')
writerOne = Fuel(HelloWorld, "HelloWorld", "HelloWorldTopic")
writerTwo = Fuel(HelloWorld, "HelloWorld", "HelloWorldTopicTwo")
writerOne.run()
writerTwo.run()
#exit()


exit()
