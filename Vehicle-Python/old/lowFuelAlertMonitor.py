from entity import Entity
import HelloWorld  # my <idl file>
import fastdds
# import signal


class Fuel(Entity.Reader):
    def __init__(self, myPubSubType, myPubSubType_name, myTopic_name, myReaderListener):
        self.MessageType = myPubSubType
        self.MessageType_name = myPubSubType_name
        self.Topic_name = myTopic_name
        self.ReaderListener = myReaderListener
        super().__init__(myPubSubType, myPubSubType_name, myTopic_name, myReaderListener)

    # def run(self):
    #     signal.signal(signal.SIGINT, lambda sig, frame : print('\nInterrupted!'))
    #     print('Press Ctrl+C to stop')
    #     signal.pause()
    #     self.delete()


class RL(Entity.ReaderListener):
    def __init__(self, data):
        self.data = data
        super().__init__(data)

    def on_subscription_matched(self, datareader, info):
        if (0 < info.current_count_change):
            print("Subscriber matched publisher {}".format(info.last_publication_handle))
        else:
            print("Subscriber unmatched publisher {}".format(info.last_publication_handle))
            # exit()

    def on_data_available(self, reader):
        info = fastdds.SampleInfo()
        data = self.data
        reader.take_next_sample(data, info)
        tempStr = data.message()
        dataArray = tempStr.split(", ")

        if float(dataArray[1]) > 50:
            print("Enough Fuel")
        else:
            print("Low Fuel Alert")


print('\nStarting publisher.')


rl_parm = RL
readerOne = Fuel(HelloWorld, "HelloWorld", "FuelRemaining", rl_parm)
readerOne.run()
exit()
