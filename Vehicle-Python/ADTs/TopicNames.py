class TopicNames(object):
    __topicNames = {
            "Fuel"          : "FuelRemaining544645",
            "Button"        : "ButtonTopic",
            "LowFuel"       : "LowFuelAlert",
            "MpG"           : "MpGCumulative",
            "MilesToRefuel" : "MilesToRefuelTopic",
            "Miles"         : "MilesTraveled"
            
        }
    
    
    @classmethod
    def getTopicName(cls, dataName : str) -> str:
        return cls.__topicNames[str(dataName)]
    
    @classmethod
    def setTopicName(cls, dataName : str, newTopicName : str) -> None:
        cls.__topicNames[str(dataName)] = str(newTopicName)