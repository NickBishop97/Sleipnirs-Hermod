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

def calc(inputQueue):
    while True:
        if not inputQueue.empty():
            print(f"This the queue data: {inputQueue.get()}\n\n")

        

def main():
    signal.signal(signal.SIGINT, 
                    lambda sig, frame : (
                        print("\nInterrupted!\n"),
                        exit(),
                    ))

    readerFuel  = FuelGauge(Fuel, "Fuel", "FuelRemaining", FuelRL, controlSignal)
    readerMiles = DistanceDisplay(Miles, "Miles", "MilesTraveled", DistanceRL, controlSignal)
    threadFuel  = Thread(target=(readerFuel.run))
    #threadHello = Thread(target=(readerHello.run))
    threadCalc  = Thread(target=(calc), args=(readerFuel.dataQueue,))
    
    threadFuel.start()
    #threadHello.start()
    threadCalc.start()

    signal.pause()
    readerFuel.delete()
    #readerHello.delete()
    
    exit()


main()