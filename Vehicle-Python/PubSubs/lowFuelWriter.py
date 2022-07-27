from threading import Thread
import signal
# import time
import sys

# ADT IMPORTS
sys.path.insert(0, '../ADTs/')
from Writers     import LowFuelWriter, LowFuelCalc  # noqa E402,F403 (linting exemptions)
from Readers     import FuelGauge, FuelRL, CLKDisplay, CLKRL  # noqa E402,F403 (linting exemptions)
from Calculators import LowFuelCalc  # noqa E402,F403 (linting exemptions)
from TopicNames  import TopicNames

# IDL DATA IMPORTS
sys.path.insert(1, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)

sys.path.insert(2, '../MessageFormats/LowFuelAlert/')
import LowFuelAlert as LowFuelAlert  # noqa E402 (linting exemption)

def main():
    writers = []
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                      print("\nInterrupted!\n"),
                      [reader.delete() for reader in readers],
                      [writer.delete() for writer in writers],
                      sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")
    
    clkReader = CLKDisplay([CLK, 
                            "CLK", 
                            TopicNames.getTopicName("CLK"), 
                            CLKRL])
    
    FuelReader    = FuelGauge([Fuel,
                               "Fuel",
                               TopicNames.getTopicName("Fuel"),
                              FuelRL])  # noqa: F405
    
    lowFuelWriter = LowFuelWriter([LowFuelAlert,
                                   "LowFuelAlert",
                                   TopicNames.getTopicName("LowFuelAlert")],
                                  LowFuelCalc(50))  # noqa F405 (linting exemption)
    
    
    readers.append(FuelReader)
    readers.append(clkReader)
    writers.append(lowFuelWriter)

    # Add readers and start threads
    CLKThread  = Thread(target=())
    FuelThread = Thread(target=(FuelReader.run), daemon=True)
    LowFThread = Thread(target=(writers[0].run),
                        args=(
                            readers[0].getData(),
                            readers[1].getData(),),
                        daemon=True)

    threads.append(FuelThread)
    threads.append(CLKThread)
    threads.append(LowFThread)

    for thread in threads:
        thread.start()

    signal.pause()


main()
