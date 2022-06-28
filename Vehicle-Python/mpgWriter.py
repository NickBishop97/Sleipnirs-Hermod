from queue import Queue
from threading import Thread
import signal
import time

import sys

#IDL DATA IMPORTS
sys.path.insert(0, './Fuel/')
import Fuel as Fuel
sys.path.insert(1, './Miles/')
import Miles as Miles

from Readers import *


def controlSignal():
    time.sleep(50)
    return True

def calc(fuelQueue, mileQueue):
    while True:
        if not fuelQueue.empty():
            print(f"Fuel Data: {fuelQueue.get()}")
            
        if not mileQueue.empty():
            print(f"Miles Data: {mileQueue.get()}\n")
            
        
def main():
    writers = []
    readers = []
    threads = []
    signal.signal(signal.SIGINT, 
                    lambda sig, frame : (
                        print("\nStopped!"),
                        [reader.delete() for reader in readers],
                        sys.exit(0),
                    ))
    
    print("Press Ctrl+C to stop")
    
    readers.append(FuelGauge(Fuel, "Fuel", "FuelRemaining", FuelRL, controlSignal))
    readers.append(DistanceDisplay(Miles, "Miles", "MilesTraveled", DistanceRL, controlSignal))
    
    #Add readers and start threads
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))    
    threadCalc  = Thread(target=(calc), args=(readers[0].dataQueue,readers[1].dataQueue), daemon=True)
    
    for thread in threads:
        thread.start()
    threadCalc.start()

    signal.pause()
    

main()
