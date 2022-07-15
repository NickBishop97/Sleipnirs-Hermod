from threading import Thread
import signal
import time
import sys

#ADT IMPORTS
sys.path.insert(0, '../ADTs/')
from Writers import *  
from Readers import *
from Calculators import *
from TopicNames import *

# IDL DATA IMPORTS
sys.path.insert(1, '../MessageFormats/Fuel/')
import Fuel as Fuel
sys.path.insert(2, '../MessageFormats/Miles/')
import Miles as Miles  
sys.path.insert(3, '../MessageFormats/MpG/')
import MpG as MpG  
sys.path.insert(4, '../MessageFormats/LowFuelAlert/')
import LowFuelAlert as LowFuelAlert  
sys.path.insert(5, '../MessageFormats/MilesToRefuel/')
import MilesToRefuel as MilesToRefuel  
sys.path.insert(6, '../MessageFormats/Button/')
import Button as Button  

#####################################################
#####################################################
#####################################################

#####################################################
#####################################################
#####################################################

def tripCalculator(queueList : list) -> None:
    while True:
        #if not queueList[0].empty():
        print(f"FUEL        :{queueList[0].get()}")
        print(f"MILES       :{queueList[1].get()}")
        print(f"MPG         :{queueList[2].get()}")
        print(f"LOWFUEL     :{queueList[3].get()}")
        print(f"MILESREMAIN :{queueList[4].get()}")
        print("\n\n")
        time.sleep(0.3)  

def main() -> None:
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nStopped!"),
                    [reader.delete() for reader in readers],
                    sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")

    readers.append(FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL]))
    readers.append(DistanceDisplay([Miles, "Miles", "MilesTraveled", DistanceRL]))
    readers.append(MpGDisplay([MpG, "MpG", "MpGCumulative", MpGRL]))
    readers.append(LowFuelAlertDisplay([LowFuelAlert, "LowFuelAlert", "LowFuelAlert", LowFuelAlertRL]))
    readers.append(MilesRemainDisplay([MilesToRefuel, "MilesToRefuel", "MilesToRefuelTopic", MilesRemainRL]))
    
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))
    threads.append(Thread(target=(tripCalculator),
                          args=([reader.dataQueue for reader in readers],), 
                          daemon=True))
    
    for thread in threads:
        thread.start()
    
    signal.pause()

main()