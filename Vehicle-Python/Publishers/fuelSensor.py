import signal
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel  

#ADT IMPORTS
sys.path.insert(1, '../ADTs/')
from Writers import FuelWriter  
from Calculators import FuelConsump



def runSensor():
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nInterrupted!\n"),
                    exit(),
                  ))

    print('\nStarting publisher.')
    fuelWriter = FuelWriter([Fuel, "Fuel", "FuelRemaining"], FuelConsump(100,100))  # noqa: F821
    fuelWriter.run()

    # code is not unreachable, just a bug
    signal.pause()


runSensor()
