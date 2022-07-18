from threading import Thread
import signal
# import time
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)
sys.path.insert(1, '../MessageFormats/Miles/')
# import Miles as Miles
sys.path.insert(2, '../MessageFormats/LowFuelAlert/')
import LowFuelAlert as LowFuelAlert  # noqa E402 (linting exemption)

# ADT IMPORTS
sys.path.insert(2, '../ADTs/')
from Writers import *  # noqa E402,F403 (linting exemptions)
from Readers import *  # noqa E402,F403 (linting exemptions)
from Calculators import *  # noqa E402,F403 (linting exemptions)


def main():
    writers = []
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                      print("\nStopped!"),
                      [reader.delete() for reader in readers],
                      sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")
    FuelReader = FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL])  # noqa: F405
    lowFuelWriter = LowFuelWriter([LowFuelAlert, "LowFuelAlert", "LowFuelAlert"])  # noqa F405 (linting exemption)

    readers.append(FuelReader)
    writers.append(lowFuelWriter)

    # Add readers and start threads
    FuelThread = Thread(target=(FuelReader.run), daemon=True)
    CalcThread = Thread(target=(writers[0].run),
                        args=(
                            readers[0].dataQueue,),
                        daemon=True)

    threads.append(FuelThread)
    threads.append(CalcThread)

    for thread in threads:
        thread.start()

    signal.pause()


main()
