# from queue import Queue
from threading import Thread
import signal
# import time
# import queue
# from queue import Queue

import sys

# ADT IMPORTS
sys.path.insert(0, '../ADTs/')
from Writers     import MpGWriter  # noqa E402,F403 (linting exemptions)
from Readers     import FuelGauge, FuelRL, DistanceDisplay, DistanceRL, CLKDisplay, CLKRL
from Calculators import MpGCalc  # noqa E402,F403 (linting exemptions)
from TopicNames  import TopicNames

# IDL DATA IMPORTS
sys.path.insert(1, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)
sys.path.insert(2, '../MessageFormats/Miles/')
import Miles as Miles  # noqa E402 (linting exemption)
sys.path.insert(3, '../MessageFormats/CLK/')
import CLK as CLK  # noqa E402 (linting exemption)
sys.path.insert(4, '../MessageFormats/MpG/')
import MpG as MpG  # noqa E402 (linting exemption)



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

    readers.append(FuelGauge([Fuel,
                              "Fuel",
                              TopicNames.getTopicName("Fuel"),
                              FuelRL]))  # noqa: F405
    
    readers.append(DistanceDisplay([Miles,
                                    "Miles",
                                    TopicNames.getTopicName("Miles"),
                                    DistanceRL]))  # noqa: F405
    
    readers.append(CLKDisplay([CLK, 
                            "CLK", 
                            TopicNames.getTopicName("CLK"), 
                            CLKRL]))  # noqa: F405
    
    writers.append(MpGWriter([MpG,
                              "MpG",
                              TopicNames.getTopicName("MpG")],
                             MpGCalc()))  # noqa F405 (linting exemption)

    # Add readers and start threads
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))

    # writer
    threadMpG = Thread(target=(writers[0].run),
                       args=(
        readers[0].getData(),
        readers[1].getData(),
        readers[2].getData()),
        daemon=True)

    for thread in threads:
        thread.start()
    threadMpG.start()

    signal.pause()


main()
