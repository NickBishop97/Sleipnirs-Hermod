from threading import Thread
import signal
import time
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel
sys.path.insert(1, '../MessageFormats/Miles/')
import Miles as Miles  
sys.path.insert(2, '../MessageFormats/LowFuel/')
import LowFuel as LowFuel  

#ADT IMPORTS
sys.path.insert(3, '../ADTs/')
from Writers import *  
from Readers import *
from Calculators import *


def calcLowFuel(fuelQueue, lowFuelWriter):
    while True:
        if not fuelQueue.empty():
            lowFuel = LowFuel(50) #this is the actual calculator
            alert = lowFuel.lowFuelAlert(fuelQueue.get())
            lowFuelWriter.run(alert)


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
    FuelReader    = FuelGauge([Fuel, "Fuel", "FuelRemaining", FuelRL])  # noqa: F405
    lowFuelWriter = LowFuelWriter([LowFuel, "LowFuel", "LowFuelAlert"])
    
    readers.append(FuelReader)
    writers.append(lowFuelWriter)

    # Add readers and start threads
    FuelThread = Thread(target=(FuelReader.run), daemon=True)
    CalcThread = Thread(target=(calcLowFuel),
                        args=(
                            readers[0].dataQueue,
                            lowFuelWriter),
                        daemon=True)

    threads.append(FuelThread)
    threads.append(lowFuelWriter)
    threads.append(CalcThread)

    for thread in threads:
        thread.start()

    signal.pause()


main()

###