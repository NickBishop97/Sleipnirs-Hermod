from threading import Thread
import signal
# import time
import sys
from queue import Queue

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)
sys.path.insert(1, '../MessageFormats/Miles/')
import Miles as Miles  # noqa E402 (linting exemption)

# ADT IMPORTS
sys.path.insert(2, '../ADTs/')
from Writers import *  # noqa E402,F403 (linting exemptions)
from Readers import *  # noqa E402,F403 (linting exemptions)
from Calculators import *  # noqa E402,F403 (linting exemptions)


<<<<<<< HEAD
def main() -> None:
=======
def fuelConnectionStatus(dataQueue, connected, startStopCondition):
    while True:

        # print(f"Connected? {str(connected.connected)}")
        if not dataQueue.empty():
            data = dataQueue.get()
            startStopCondition.milesStarter = True

            if float(data[1]) <= 0:
                startStopCondition.milesStopper = True
                print("*****NO FUEL*****")

            print("\n")


class StartStopCondition:
    milesStarter = False
    milesStopper = False


def main():
>>>>>>> master
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
<<<<<<< HEAD
    
    #MAKING THREADS TO RUN READER AND WRITER OBJECTS
=======
    startStopCondition = StartStopCondition()

    # MAKING THREADS TO RUN READER AND WRITER OBJECTS
>>>>>>> master
    FuelReader = FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL])  # noqa: F405
    DistWriter = MilesWriter([Miles, "Miles", "MilesTraveled"], DistTrav(0))  # noqa: F405

    readers.append(FuelReader)
    writers.append(DistWriter)

    # Add readers and start threads
    FuelThread = Thread(target=(FuelReader.run), daemon=True)
<<<<<<< HEAD
    DistThread = Thread(target=(DistWriter.run), 
                        args=(readers[0].getDataQueue(),),
=======
    DistThread = Thread(target=(DistWriter.run), args=(startStopCondition,), daemon=True)

    # REAL TIME READ FLAG DATA FROM FUEL IS HERE
    CalcThread = Thread(target=(fuelConnectionStatus),
                        args=(
                            readers[0].dataQueue,
                            readers[0].connected,
                            startStopCondition,),
>>>>>>> master
                        daemon=True)
    

    threads.append(FuelThread)
    threads.append(DistThread)
    

    for thread in threads:
        thread.start()

    signal.pause()


main()
