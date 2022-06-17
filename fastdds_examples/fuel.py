from entity import Entity
import HelloWorld #my <idl file>

class Fuel(Entity.Writer):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name)
        
    def write(self):
        print("hello wrold")
        
        self.data.message("Hello World")
        self.data.index(self.index)
        self.writer.write(self.data)
        print("Sending {message} : {index}".format(message=self.data.message(), index=self.data.index()))
        self.index = self.index + 1
    
        
        
#print('Starting publisher.')
#writer = Fuel(HelloWorld, "HelloWorld", "HelloWorldTopic")
#writer.write()
#exit()

print('Creating subscriber.')
reader = Entity.Reader(HelloWorld, "HelloWorld", "HelloWorldTopic")
reader.run()
exit()
