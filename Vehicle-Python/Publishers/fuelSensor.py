import signal
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel  

#ADT IMPORTS
sys.path.insert(1, '../ADTs/')
from Writers import FuelWriter  
from Calculators import FuelConsump

    
#MAIN
def runSensor() -> None:
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nInterrupted!\n"),
                    fuelWriter.stopSignalReceived(True),
                    fuelWriter.write(),
                    fuelWriter.delete(),
                    exit(),
                  ))

    print('\nStarting publisher.')
    #FuelRemaining544645
    fuelWriter = FuelWriter([Fuel, "Fuel", "FuelRemaining544645"], FuelConsump(100,100))  # noqa: F821
    fuelWriter.run()

    # code is not unreachable, just a bug
    signal.pause()


runSensor()
