from threading import Thread
import signal
import time
import sys

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


def calc(dataQueue, connected, startStopCondition):
    while True:

        #if not dataQueue.empty():
        print(f"Fuel Data: {dataQueue.get()}")
        print(f"Connected? {str(connected.connected)}")
        startStopCondition.milesStarter = True
        
        if float(dataQueue.get()[0]) <= 0:
            startStopCondition.milesStopper = True
            print("Fuel has ran out!")
            


class StartStopCondition:
    milesStarter = False
    milesStopper = False

def main():
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
    startStopCondition = StartStopCondition()
    FuelReader = FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL])  # noqa: F405
    DistWriter = MilesWriter([Miles, "Miles", "MilesTraveled"], DistTrav(0))  # noqa: F405

    readers.append(FuelReader)
    writers.append(DistWriter)

    # Add readers and start threads
    FuelThread = Thread(target=(FuelReader.run), daemon=True)
    DistThread = Thread(target=(DistWriter.run), args=(startStopCondition,), daemon=True)
    CalcThread = Thread(target=(calc),
                        args=(
                            readers[0].dataQueue,
                            readers[0].connected,
                            startStopCondition,),
                        daemon=True)

    threads.append(FuelThread)
    threads.append(DistThread)
    threads.append(CalcThread)

    for thread in threads:
        thread.start()

    signal.pause()


main()
