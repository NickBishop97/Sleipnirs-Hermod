# from queue import Queue
from threading import Thread
import signal
# import time
# import queue
# from queue import Queue

import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)
sys.path.insert(1, '../MessageFormats/MpG/')
import MpG as MpG  # noqa E402 (linting exemption)

sys.path.insert(2, '../MessageFormats/MilesToRefuel/')
import MilesToRefuel as MilesToRefuel  # noqa E402 (linting exemption)

# ADT IMPORTS
sys.path.insert(3, '../ADTs/')
from Writers import *  # noqa E402,F403 (linting exemptions)
from Readers import *  # noqa E402,F403 (linting exemptions)
from Calculators import *  # noqa E402,F403 (linting exemptions)
from TopicNames import TopicNames


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

    readers.append(FuelGauge([Fuel,
                              "Fuel",
                              TopicNames.getTopicName("Fuel"),
                              FuelRL]))  # noqa: F405
    
    readers.append(MpGDisplay([MpG,
                               "MpG",
                               TopicNames.getTopicName("MpG"),
                               MpGRL]))  # noqa: F405

    writers.append(MilesRemaining([MilesToRefuel,
                                   "MilesToRefuel",
                                   TopicNames.getTopicName("MilesToRefuel")],
                                  MileRemainCalc()))  # noqa F405 (linting exemption)

    # Add readers and start threads
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))

    threadMpG = Thread(target=(writers[0].run),
                       args=(
        readers[0].getData(),
        readers[1].getData(),),
        daemon=True)

    for thread in threads:
        thread.start()
    threadMpG.start()

    signal.pause()


main()
