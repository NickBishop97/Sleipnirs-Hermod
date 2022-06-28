from threading import Thread
import signal
import time
import random
import sys

#IDL DATA IMPORTS
sys.path.insert(0, './Fuel/')
import Fuel as F
sys.path.insert(1, './Miles/')
import Miles as M

from Writers import FuelWriter, MilesWriter

def runSensor():

    signal.signal(signal.SIGINT, 
                    lambda sig, frame : (
                        print("\nInterrupted!\n"),
                        fuelWriter.delete(),
                        exit(),
                    ))

    print('\nStarting publisher.')
    fuelWriter = FuelWriter(F, "Fuel", "FuelRemaining")
    fuelWriter.run()

    #code is not unreachable, just a bug
    signal.pause()
    

runSensor()