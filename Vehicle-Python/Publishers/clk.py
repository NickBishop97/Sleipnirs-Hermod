import signal
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/CLK/')
import CLK as CLK  

#ADT IMPORTS
sys.path.insert(1, '../ADTs/')
from Writers    import CLKWriter  
from TopicNames import TopicNames

    
#MAIN
def runSensor() -> None:
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nInterrupted!\n"),
                    clkWriter.setStopSignal(True),
                    clkWriter.delete(),
                    exit(),
                  ))

    print('\nStarting publisher.')
    
    clkPeriod = 0.25/2.0
    clkWriter = CLKWriter([CLK,
                             "CLK", 
                             TopicNames.getTopicName("CLK")], 
                            clkPeriod)
    

    clkWriter.run()
    signal.pause()


runSensor()
