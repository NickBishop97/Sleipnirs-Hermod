import signal
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)

# ADT IMPORTS
sys.path.insert(1, '../ADTs/')
from Writers import FuelWriter  # noqa E402 (linting exemption)
from Calculators import FuelConsump  # noqa E402 (linting exemption)


class TestFlag:
    def __init__(self):
        self.test_flag = False

    def makeTrue(self):
        self.test_flag = True

# MAIN


def runSensor():
    test_flag = TestFlag()

    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                      print("\nInterrupted!\n"),
                      test_flag.makeTrue(),
                      fuelWriter.write(test_flag.test_flag),
                      fuelWriter.delete(),
                      exit(),
                  ))

    print('\nStarting publisher.')
    # FuelRemaining544645
    fuelWriter = FuelWriter([Fuel, "Fuel", "FuelRemaining544645"], FuelConsump(100, 100))  # noqa: F821
    fuelWriter.run(test_flag.test_flag)

    signal.pause()


#runSensor()
