# from threading import Thread
import signal
# import time
# import random
import sys

# IDL DATA IMPORTS
sys.path.insert(0, './Fuel/')
import Fuel as F  # noqa: E402
# sys.path.insert(1, './Miles/')
# import Miles as M  # noqa: E402

# from Writers import FuelWriter, MilesWriter  # noqa: E402


def runSensor():

    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nInterrupted!\n"),
                    fuelWriter.delete(),
                    exit(),
                  ))

    print('\nStarting publisher.')
    fuelWriter = FuelWriter(F, "Fuel", "FuelRemaining")  # noqa: F821
    fuelWriter.run()

    # code is not unreachable, just a bug
    signal.pause()


runSensor()
