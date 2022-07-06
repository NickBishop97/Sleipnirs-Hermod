<<<<<<< HEAD
from threading import Thread
import signal
import time
=======
# from queue import Queue
from threading import Thread
import signal
import time
import queue
from queue import Queue

>>>>>>> mpgWriter
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel
<<<<<<< HEAD
sys.path.insert(1, '../MessageFormats/Miles/')
import Miles as Miles  
sys.path.insert(2, '../MessageFormats/LowFuel/')
import LowFuel as LowFuel  
=======
sys.path.insert(1, '../MessageFormats/MpG/')
import MpG as MpG  

sys.path.insert(2, '../MessageFormats/MilesToRefuel/')
import MilesToRefuel as MilesToRefuel  
>>>>>>> mpgWriter

#ADT IMPORTS
sys.path.insert(3, '../ADTs/')
from Writers import *  
from Readers import *
from Calculators import *


<<<<<<< HEAD
def calcLowFuel(fuelQueue, lowFuelWriter):
    while True:
        if not fuelQueue.empty():
            lowFuel = LowFuel(50)
            alert = lowFuel.lowFuelAlert(fuelQueue.get())
            lowFuelWriter.run(alert)


=======
>>>>>>> mpgWriter
def main():
    writers = []
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nStopped!"),
                    [reader.delete() for reader in readers],
<<<<<<< HEAD
                    [writer.delete() for writer in writers],
=======
>>>>>>> mpgWriter
                    sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")
<<<<<<< HEAD
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
=======

    readers.append(FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL]))  # noqa: F405
    readers.append(MpGReader([MpG, "MpG", "MpGTopic", MpGRL]))  # noqa: F405

    writers.append(MilesRemaining([MilesToRefuel, "MilesToRefuel", "MilesToRefuelTopic"]))

    # Add readers and start threads
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))
        
    threadMpG = Thread(target=(writers[0].run), 
                        args=(
                            readers[0].dataQueue, 
                            readers[1].dataQueue,), 
                        daemon=True)

    for thread in threads:
        thread.start()
    threadMpG.start()
>>>>>>> mpgWriter

    signal.pause()


<<<<<<< HEAD
main()
=======
main()
>>>>>>> mpgWriter
