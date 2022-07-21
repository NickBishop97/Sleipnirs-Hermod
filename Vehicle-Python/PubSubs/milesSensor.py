from threading import Thread
import signal
# import time
import sys

# ADT IMPORTS
sys.path.insert(0, '../ADTs/')
from Writers     import MilesWriter  # noqa E402,F403 (linting exemptions)
from Readers     import CLKDisplay, CLKRL, FuelGauge, FuelRL  # noqa E402,F403 (linting exemptions)
from Calculators import DistTrav  # noqa E402,F403 (linting exemptions)
from TopicNames  import TopicNames

# IDL DATA IMPORTS
sys.path.insert(1, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)
sys.path.insert(2, '../MessageFormats/Miles/')
import Miles as Miles  # noqa E402 (linting exemption)
sys.path.insert(3, '../MessageFormats/CLK/')
import CLK as CLK  # noqa E402 (linting exemption)



def main():
    writers = []
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                      print("\nInterrupted!\n"),
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
    
    FuelReader = FuelGauge([Fuel, 
                            "Fuel", 
                            TopicNames.getTopicName("Fuel"), 
                            FuelRL])  # noqa: F405
    
    DistWriter = MilesWriter([Miles, 
                              "Miles", 
                              TopicNames.getTopicName("Miles")], 
                             DistTrav(0,0.1))  # noqa: F405

    readers.append(clkReader)
    readers.append(FuelReader)
    writers.append(DistWriter)

    # Add readers and start threads
    FuelThread = Thread(target=(FuelReader.run), daemon=True)
    DistThread = Thread(target=(DistWriter.run), 
                        args = (readers[0].getData(),
                                readers[1].getData(),),
                        daemon=True)

    threads.append(FuelThread)
    threads.append(DistThread)

    for thread in threads:
        thread.start()

    signal.pause()


main()
