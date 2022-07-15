from threading import Thread
import signal
import time
import sys
from queue import Queue

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel
sys.path.insert(1, '../MessageFormats/Miles/')
import Miles as Miles  

#ADT IMPORTS
sys.path.insert(2, '../ADTs/')
from Writers import *  
from Readers import *
from Calculators import *


def main() -> None:
    writers = []
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nStopped!"),
                    [reader.delete() for reader in readers],
                    [writer.delete() for writer in writers],
                    sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")
    
    #MAKING THREADS TO RUN READER AND WRITER OBJECTS
    FuelReader = FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL])  # noqa: F405
    DistWriter = MilesWriter([Miles, "Miles", "MilesTraveled"], DistTrav(0))  # noqa: F405

    readers.append(FuelReader)
    writers.append(DistWriter)

    # Add readers and start threads
    FuelThread = Thread(target=(FuelReader.run), daemon=True)
    DistThread = Thread(target=(DistWriter.run), 
                        args=(readers[0].getDataQueue(),),
                        daemon=True)
    

    threads.append(FuelThread)
    threads.append(DistThread)
    

    for thread in threads:
        thread.start()

    signal.pause()


main()
