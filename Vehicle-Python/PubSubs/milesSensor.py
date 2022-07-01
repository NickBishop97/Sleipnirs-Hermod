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


def calc(fuelQueue, milesStopper):
    while True:
        if not fuelQueue.empty():
            print(f"Fuel Data: {fuelQueue.get()}")
        if float(fuelQueue.get()) <= 0:
            milesStopper.milesStopper = True


class MilesStopper:
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
    milesStopper = MilesStopper()
    FuelReader = FuelGauge([Fuel, "Fuel", "FuelRemaining", FuelRL])  # noqa: F405
    DistWriter = MilesWriter([Miles, "Miles", "MilesTraveled"], DistTrav(0))  # noqa: F405

    readers.append(FuelReader)
    writers.append(DistWriter)

    # Add readers and start threads
    FuelThread = Thread(target=(FuelReader.run), daemon=True)
    DistThread = Thread(target=(DistWriter.run), args=(milesStopper,), daemon=True)
    CalcThread = Thread(target=(calc),
                        args=(
                            readers[0].dataQueue,
                            milesStopper,),
                        daemon=True)

    threads.append(FuelThread)
    threads.append(DistThread)
    threads.append(CalcThread)

    for thread in threads:
        thread.start()

    signal.pause()


main()