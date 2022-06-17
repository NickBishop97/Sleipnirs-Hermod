from entity import Entity
import HelloWorld #my <idl file>
import fastdds

class Fuel(Entity.Reader):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name)
        
class RL(Entity.ReaderListener):
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
        data = self.data
        #data = HelloWorld.HelloWorld()
        reader.take_next_sample(data, info)
        print("Received {message} : {index}".format(message=data.message(), index=data.index()))

print('\nStarting publisher.')
rl_parm = RL()
readerOne = Fuel(HelloWorld, "HelloWorld", "HelloWorldTopic", rl_parm)
readerTwo = Fuel(HelloWorld, "HelloWorld", "HelloWorldTopicTwo")

readerOne.run()
readerTwo.run()
#exit()


exit()
