# Copyright 2022 Proyectos y Sistemas de Mantenimiento SL (eProsima).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
HelloWorld Publisher
"""
from threading import Thread
from email.message import Message
from logging.config import listen
from multiprocessing.connection import Listener
from threading import Condition
import time

import fastdds

DESCRIPTION = """HelloWorld Publisher example for Fast DDS python bindings"""
USAGE = ('python3 HelloWorldPublisher.py')
class Entity : 
    
    class ReaderListener(fastdds.DataReaderListener):

        def __init__(self):
            #self.data = data
            super().__init__()


        def on_subscription_matched(self, datareader, info) :
            raise NotImplementedError(self.__class__.__name__ + " was not implemented!")

        def on_data_available(self, reader):
            raise NotImplementedError(self.__class__.__name__ + " was not implemented!")

        def getDataReturn(self):
            raise NotImplementedError(self.__class__.__name__ + " was not implemented!")

    class Reader:
        def __init__(self, 
                     myPubSubType, 
                     myPubSubType_name, 
                     myTopic_name, 
                     myListener, 
                     myControlSignal,):
            #SAVING INPUT VARIABLES
            self.MessageType      = myPubSubType
            self.MessageType_name = myPubSubType_name
            self.Topic_name       = myTopic_name
            #self.ReaderListener   = myReaderListener #PASS BY POINTER, NOT BY OBJECT
            self.controlSignal    = myControlSignal
            #self.dataOutput = myDataOutput
            
            #SAVING THE DATA TYPE OF THE MESSAGE
            
            try:
                #data = HelloWorld.HelloWorld()
                func = getattr(self.MessageType, f"{self.MessageType_name}") #inputting the idl special datatype
                self.data = func()
            except AttributeError:
                print(f"{self.MessageType_name}.{self.MessageType_name}() not found")
            
            #use factory to make participant
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.participant_qos = fastdds.DomainParticipantQos()
            factory.get_default_participant_qos(self.participant_qos)
            self.participant = factory.create_participant(0, self.participant_qos)

            #create name and initialize the data type for the topic
            #myPubSubType() is the message type being defined   
            try:
                funcOne = getattr(self.MessageType, f"{self.MessageType_name}PubSubType") #inputting the idl special datatype
                self.topic_data_type = funcOne()
                print(f"Found: {self.MessageType_name}.{self.MessageType_name}PubSubType()")
            except AttributeError:
                print(f"{self.MessageType_name}.{self.MessageType_name}PubSubType() not found")
                
            self.topic_data_type.setName(f"{self.MessageType_name}")
            self.type_support = fastdds.TypeSupport(self.topic_data_type)
            self.participant.register_type(self.type_support)


            #create the topic itself and name it 
            self.topic_qos = fastdds.TopicQos()
            self.participant.get_default_topic_qos(self.topic_qos)
            self.topic = self.participant.create_topic(f"{self.Topic_name}", self.topic_data_type.getName(), self.topic_qos)

            #create the particular subscriber
            self.subscriber_qos = fastdds.SubscriberQos()
            self.participant.get_default_subscriber_qos(self.subscriber_qos)
            self.subscriber = self.participant.create_subscriber(self.subscriber_qos)


            #create the data reader object, and listen to the topic
            
            #####################################################################################################
            
            self.listener = myListener(self.data)
            self.dataQueue = self.listener.getDataReturn()
            
            #####################################################################################################
            self.reader_qos = fastdds.DataReaderQos()
            self.subscriber.get_default_datareader_qos(self.reader_qos)
            self.reader = self.subscriber.create_datareader(self.topic, self.reader_qos, self.listener)
      
        def dataRunReturn(self):
            while True:
                if not self.dataQueue.empty():
                    return self.dataQueue
                else:
                    return None
                
      
        def run(self):
            dataThread = Thread(target=(self.dataRunReturn), daemon=True)
            dataThread.start()
            
            
        def delete(self):
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.participant.delete_contained_entities()
            factory.delete_participant(self.participant)
                    
    class WriterListener (fastdds.DataWriterListener) :
        def __init__(self, writer) :
            self._writer = writer
            super().__init__()


        def on_publication_matched(self, datawriter, info) :
            if (0 < info.current_count_change) :
                print ("Publisher matched subscriber {}".format(info.last_subscription_handle))
                self._writer._cvDiscovery.acquire()
                self._writer._matched_reader += 1
                self._writer._cvDiscovery.notify()
                self._writer._cvDiscovery.release()
            else :
                print ("Publisher unmatched subscriber {}".format(info.last_subscription_handle))
                self._writer._cvDiscovery.acquire()
                self._writer._matched_reader -= 1
                self._writer._cvDiscovery.notify()
                self._writer._cvDiscovery.release()
                exit()

    class Writer:
        
        def __init__(self, myPubSubType, myPubSubType_name, myTopic_name):
            #SAVING INPUT VARIABLES
            self.MessageType = myPubSubType
            self.MessageType_name = myPubSubType_name
            self.Topic_name = myTopic_name
            
            #SAVING THE DATA TYPE OF THE MESSAGE
            try:
                #data = HelloWorld.HelloWorld()
                func = getattr(self.MessageType, f"{self.MessageType_name}") #inputting the idl special datatype
                self.data = func()
            except AttributeError:
                print(f"{self.MessageType_name}.{self.MessageType_name}() not found")
            
            self._matched_reader = 0
            self._cvDiscovery = Condition()
            self.index = 0

            #creating a fastdds factory to generate participant.
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.participant_qos = fastdds.DomainParticipantQos()
            factory.get_default_participant_qos(self.participant_qos)
            self.participant = factory.create_participant(0, self.participant_qos)

            #myPubSubType() is the message type being defined   
            try:
                funcOne = getattr(self.MessageType, f"{self.MessageType_name}PubSubType") #inputting the idl special datatype
                self.topic_data_type = funcOne()
                print(f"Found: {self.MessageType_name}.{self.MessageType_name}PubSubType()")
            except AttributeError:
                print(f"{self.MessageType_name}.{self.MessageType_name}PubSubType() not found")
                
            self.topic_data_type.setName(f"{self.MessageType_name}") #setting name of topic to myPubSubType_name, <idl-name>
            self.type_support = fastdds.TypeSupport(self.topic_data_type)
            self.participant.register_type(self.type_support)

            #creating a topic using the topic name and idl file name
            self.topic_qos = fastdds.TopicQos()
            self.participant.get_default_topic_qos(self.topic_qos)
            self.topic = self.participant.create_topic(myTopic_name, self.topic_data_type.getName(), self.topic_qos)

            #making the participant a publisher
            self.publisher_qos = fastdds.PublisherQos()
            self.participant.get_default_publisher_qos(self.publisher_qos)
            self.publisher = self.participant.create_publisher(self.publisher_qos)

            #making a data writer
            self.listener = Entity.WriterListener(self)
            self.writer_qos = fastdds.DataWriterQos()
            self.publisher.get_default_datawriter_qos(self.writer_qos)
            self.writer = self.publisher.create_datawriter(self.topic, self.writer_qos, self.listener)

        def wait_discovery(self) :
            self._cvDiscovery.acquire()
            print (f"{self.MessageType_name}Writer is waiting discovery...")
            self._cvDiscovery.wait_for(lambda : self._matched_reader != 0)
            self._cvDiscovery.release()
            print("Writer discovery finished...")

        def delete(self):
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.participant.delete_contained_entities()
            factory.delete_participant(self.participant)
