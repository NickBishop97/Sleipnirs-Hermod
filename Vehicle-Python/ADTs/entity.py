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
entity.py
"""
from threading import Thread
from threading import Condition
from queue import Queue

import fastdds

DESCRIPTION = """Writer and Reader ADTs for use"""
USAGE = """TO BE INHERITED BY A USER DEFINED CLASS"""


class Entity:

    class ReaderListener(fastdds.DataReaderListener):

        def __init__(self):
            super().__init__()

        def on_subscription_matched(self, datareader: type, info: type) -> None:
            if(0 < info.current_count_change):
                print("Subscriber matched publisher {}".format(info.last_publication_handle))
            else:
                print("Subscriber unmatched publisher {}".format(info.last_publication_handle))

        def on_data_available(self, reader: type) -> None:
            raise NotImplementedError(self.__class__.__name__ + " was not implemented!")

        def getDataReturn(self):
            raise NotImplementedError(self.__class__.__name__ + " was not implemented!")

    class Reader:
        def __init__(self,
                     ddsDataArray: list):

            # SAVING INPUT VARIABLES
            self.__MessageType = ddsDataArray[0]
            self.__MessageType_name = ddsDataArray[1]
            self.__Topic_name = ddsDataArray[2]

            try:
                func = getattr(self.__MessageType, f"{self.__MessageType_name}")  # inputting the idl special datatype
                self.__data = func()
            except AttributeError:
                print(f"{self.__MessageType_name}.{self.__MessageType_name}() not found")
                raise

            # use factory to make participant
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.__participant_qos = fastdds.DomainParticipantQos()
            factory.get_default_participant_qos(self.__participant_qos)
            self.__participant = factory.create_participant(0, self.__participant_qos)

            # create name and initialize the __data type for the topic
            # myPubSubType() is the message type being defined
            try:
                funcOne = getattr(self.__MessageType, f"{self.__MessageType_name}PubSubType")  # inputting the idl special datatype
                self.__topic_data_type = funcOne()
                print(f"Found: {self.__MessageType_name}.{self.__MessageType_name}PubSubType()")
            except AttributeError:
                print(f"{self.__MessageType_name}.{self.__MessageType_name}PubSubType() not found")
                raise

            # creation of a topic name and registering __data type and topic with fastdds
            self.__topic_data_type.setName(f"{self.__MessageType_name}")
            self.__type_support = fastdds.TypeSupport(self.__topic_data_type)
            self.__participant.register_type(self.__type_support)

            # create the topic itself and name it
            self.__topic_qos = fastdds.TopicQos()
            self.__participant.get_default_topic_qos(self.__topic_qos)
            self.__topic = self.__participant.create_topic(f"{self.__Topic_name}", self.__topic_data_type.getName(), self.__topic_qos)

            # create the particular subscriber
            self.__subscriber_qos = fastdds.SubscriberQos()
            self.__participant.get_default_subscriber_qos(self.__subscriber_qos)
            self.__subscriber = self.__participant.create_subscriber(self.__subscriber_qos)

            # create the __data reader object, and listen to the topic

            #####################################################################################################

            self.__listener = ddsDataArray[3](self.__data)
            # By default, reader data should be a queue
            self.__readerData = self.__listener.getDataReturn()

            #####################################################################################################

            # creation of the __data reader
            self.__reader_qos = fastdds.DataReaderQos()
            self.__subscriber.get_default_datareader_qos(self.__reader_qos)
            self.__reader = self.__subscriber.create_datareader(self.__topic, self.__reader_qos, self.__listener)

        def getReader(self) -> type:
            return self.__reader

        def getListener(self) -> type:
            return self.__listener

        def getData(self) -> type:
            return self.__data

        def getData(self) -> Queue:
            return self.__readerData

        # Returns a Queue by reference, so the whole queue is constantly returned
        def dataRunReturn(self) -> Queue:
            while True:
                if not self.__readerData.empty():
                    self.__listener.getDataReturn()
                else:
                    return None

        def run(self) -> None:
            dataThread = Thread(target=(self.dataRunReturn), daemon=True)
            dataThread.start()

        def delete(self) -> None:
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.__participant.delete_contained_entities()
            factory.delete_participant(self.__participant)

    class WriterListener (fastdds.DataWriterListener):
        def __init__(self, writer: type):
            self._writer = writer
            super().__init__()

        def on_publication_matched(self, datawriter: type, info: type) -> None:
            print("Sending...")
            if(0 < info.current_count_change):
                print("Publisher matched subscriber {}".format(info.last_subscription_handle))

                self._writer._cvDiscovery.acquire()
                self._writer._cvDiscovery.notify()
                self._writer._matched_reader += 1
                self._writer._cvDiscovery.release()
            else:
                print("Publisher unmatched subscriber {}".format(info.last_subscription_handle))
                self._writer._cvDiscovery.acquire()
                self._writer._matched_reader -= 1
                self._writer._cvDiscovery.notify()
                self._writer._cvDiscovery.release()

    class Writer:

        def __init__(self, ddsDataArray: list):
            # SAVING INPUT VARIABLES
            self.__MessageType = ddsDataArray[0]
            self.__MessageType_name = ddsDataArray[1]
            self.__Topic_name = ddsDataArray[2]

            # SAVING THE DATA TYPE OF THE MESSAGE
            try:
                # __data = HelloWorld.HelloWorld()
                func = getattr(self.__MessageType, f"{self.__MessageType_name}")  # inputting the idl special datatype
                self.data = func()
            except AttributeError:
                print(f"{self.__MessageType_name}.{self.__MessageType_name}() not found")

            self._matched_reader = 0
            self._cvDiscovery = Condition()
            self.__index = 0

            # creating a fastdds factory to generate participant.
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.__participant_qos = fastdds.DomainParticipantQos()
            factory.get_default_participant_qos(self.__participant_qos)
            self.__participant = factory.create_participant(0, self.__participant_qos)

            # myPubSubType() is the message type being defined
            try:
                funcOne = getattr(self.__MessageType, f"{self.__MessageType_name}PubSubType")  # inputting the idl special datatype
                self.__topic_data_type = funcOne()
                print(f"Found: {self.__MessageType_name}.{self.__MessageType_name}PubSubType()")
            except AttributeError:
                print(f"{self.__MessageType_name}.{self.__MessageType_name}PubSubType() not found")

            self.__topic_data_type.setName(f"{self.__MessageType_name}")  # setting name of topic to myPubSubType_name, <idl-name>
            self.__type_support = fastdds.TypeSupport(self.__topic_data_type)
            self.__participant.register_type(self.__type_support)

            # creating a topic using the topic name and idl file name
            self.__topic_qos = fastdds.TopicQos()
            self.__participant.get_default_topic_qos(self.__topic_qos)
            self.__topic = self.__participant.create_topic(self.__Topic_name, self.__topic_data_type.getName(), self.__topic_qos)

            # making the participant a publisher
            self.__publisher_qos = fastdds.PublisherQos()
            self.__participant.get_default_publisher_qos(self.__publisher_qos)
            self.__publisher = self.__participant.create_publisher(self.__publisher_qos)

            # making a __data writer
            self.__listener = Entity.WriterListener(self)
            self._writer_qos = fastdds.DataWriterQos()
            self.__publisher.get_default_datawriter_qos(self._writer_qos)
            self.__writer = self.__publisher.create_datawriter(self.__topic, self._writer_qos, self.__listener)

        def getWriter(self) -> type:
            return self.__writer

        def getData(self) -> type:
            return self.data

        def setIndex(self) -> None:
            self.__index += 1

        def getIndex(self) -> int:
            return self.__index

        def wait_discovery(self) -> None:
            self._cvDiscovery.acquire()
            print(f"{self.__MessageType_name}Writer is waiting discovery...")
            self._cvDiscovery.wait_for(lambda: self._matched_reader != 0)
            self._cvDiscovery.release()
            print("Writer discovery finished...")

        def delete(self) -> None:
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.__participant.delete_contained_entities()
            factory.delete_participant(self.__participant)
