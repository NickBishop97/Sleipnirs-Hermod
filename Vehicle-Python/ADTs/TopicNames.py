"""@package docstring
This py file contains all of the topic names

@class TopicNames - Houses all of the topic names that are usable in this python implementation

@author Maxwell Rosales
@version 0.1
@date 2022-07-21
@copyright Copyright (c) 2022
"""
class TopicNames(object):
    # container will do the heavy lifting for topic name conflicts
    __topicNames = {
        "CLK": "CLK4877968574632",
        "Fuel": "FuelRemaining545",
        "Button": "ButtonTopic89765",
        "LowFuel": "LowFuelAlert987654",
        "MpG": "MpGCumulative9087654",
        "MilesToRefuel": "MilesToRefuelTopic0876",
        "Miles": "MilesTraveled809"
    }

    @classmethod
    def getTopicName(cls, dataName: str) -> str:
        """GetTopicName

        @param cls
        @param dataName
        Return the called for topic name based on the inputted param
        """
        return cls.__topicNames[str(dataName)]

    @classmethod
    def setTopicName(cls, dataName: str, newTopicName: str) -> None:
        """setTopicName

        @param cls
        @param dataName
        @param newTopicName - Changes the topic name to this
        Sets the topic name string to the inputted value
        """
        cls.__topicNames[str(dataName)] = str(newTopicName)
