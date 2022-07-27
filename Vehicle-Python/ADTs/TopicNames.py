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
        return cls.__topicNames[str(dataName)]

    @classmethod
    def setTopicName(cls, dataName: str, newTopicName: str) -> None:
        cls.__topicNames[str(dataName)] = str(newTopicName)
