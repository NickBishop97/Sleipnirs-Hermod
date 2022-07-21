import signal
import sys
from threading import Thread

#ADT IMPORTS
sys.path.insert(0, '../ADTs/')
from Writers     import FuelWriter
from Readers     import CLKDisplay, CLKRL
from TopicNames  import TopicNames
from Calculators import FuelConsump


# IDL DATA IMPORTS
sys.path.insert(1, '../MessageFormats/CLK/')
import CLK as CLK  

sys.path.insert(2, '../MessageFormats/Fuel/')
import Fuel as Fuel  


def runSensor():
    writers = []
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                      print("\nInterrupted!\n"),
                      fuelWriter.setStopSignal(True),
                      [thread.join for thread in threads],
                      [reader.delete() for reader in readers],
                      [writer.delete() for writer in writers],
                      sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")

    # MAKING THREADS TO RUN READER AND WRITER OBJECTS
    clkReader = CLKDisplay([CLK, 
                            "CLK", 
                            TopicNames.getTopicName("CLK"), 
                            CLKRL])  # noqa: F405
    
    fuelWriter = FuelWriter([Fuel,
                             "Fuel", 
                             TopicNames.getTopicName("Fuel")], 
                            FuelConsump(100,100, 0.01)) 

    readers.append(clkReader)
    writers.append(fuelWriter)

    # Add readers and start threads
    CLKThread = Thread(target=(clkReader.run), daemon=True)
    FuelThread = Thread(target=(fuelWriter.run), 
                        args = (readers[0].getData(),),
                        daemon=True)

    threads.append(CLKThread)
    threads.append(FuelThread)

    for thread in threads:
        thread.start()

    signal.pause()


runSensor()
