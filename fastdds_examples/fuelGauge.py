from entity import Entity
import HelloWorld #my <idl file>

class Fuel(Entity.Reader):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name)
        

print('\nStarting publisher.')
readerOne = Fuel(HelloWorld, "HelloWorld", "HelloWorldTopic")
readerTwo = Fuel(HelloWorld, "HelloWorld", "HelloWorldTopicTwo")

readerOne.run()
readerTwo.run()
#exit()


exit()
