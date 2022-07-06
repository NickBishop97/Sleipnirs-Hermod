from threading import Thread
import signal
import time
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel
sys.path.insert(1, '../MessageFormats/Miles/')
import Miles as Miles  
sys.path.insert(2, '../MessageFormats/MpG/')
import MpG as MpG  
sys.path.insert(3, '../MessageFormats/LowFuelAlert/')
import LowFuelAlert as LowFuelAlert  
sys.path.insert(4, '../MessageFormats/MilesToRefuel/')
import MilesToRefuel as MilesToRefuel  

#ADT IMPORTS
sys.path.insert(5, '../ADTs/')
from Writers import *  
from Readers import *
from Calculators import *

def printer(queueList):
    while True:
        #if not queueList[0].empty():
        print(f"FUEL        :{queueList[0].get()}")
        print(f"MILES       :{queueList[1].get()}")
        print(f"MPG         :{queueList[2].get()}")
        print(f"LOWFUEL     :{queueList[3].get()}")
        print(f"MILESREMAIN :{queueList[4].get()}")
        print("\n\n")
        time.sleep(0.3)

        

def main():
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nStopped!"),
                    [reader.delete() for reader in readers],
                    sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")
    
    #MAKING THREADS TO RUN READER AND WRITER OBJECTS
    readers.append(FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL]))
    readers.append(DistanceDisplay([Miles, "Miles", "MilesTraveled", DistanceRL]))
    readers.append(MpGDisplay([MpG, "MpG", "MpGCumulative", MpGRL]))
    readers.append(LowFuelAlertDisplay([LowFuelAlert, "LowFuelAlert", "LowFuelAlert", LowFuelAlertRL]))
    readers.append(MilesRemainDisplay([MilesToRefuel, "MilesToRefuel", "MilesToRefuelTopic", MilesRemainRL]))

    # Add readers and start threads
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))
        
    printerThread = Thread(target=(printer),
                           args=([reader.dataQueue for reader in readers],), 
                           daemon=True)
    
    for thread in threads:
        thread.start()
    printerThread.start()
    
    signal.pause()


main()
