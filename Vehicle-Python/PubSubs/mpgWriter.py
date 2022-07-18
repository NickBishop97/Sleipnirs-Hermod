# from queue import Queue
from threading import Thread
import signal
<<<<<<< HEAD
import time
import queue
from queue import Queue
=======
# import time
# import queue
# from queue import Queue
>>>>>>> master

import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)
sys.path.insert(1, '../MessageFormats/Miles/')
<<<<<<< HEAD
import Miles as Miles  
sys.path.insert(2, '../MessageFormats/MpG/')
import MpG as MpG  

#ADT IMPORTS
sys.path.insert(3, '../ADTs/')
from Writers import *  
from Readers import *
from Calculators import *
=======
import Miles as Miles  # noqa E402 (linting exemption)
sys.path.insert(2, '../MessageFormats/MpG/')
import MpG as MpG  # noqa E402 (linting exemption)

# ADT IMPORTS
sys.path.insert(3, '../ADTs/')
from Writers import *  # noqa E402,F403 (linting exemptions)
from Readers import *  # noqa E402,F403 (linting exemptions)
from Calculators import *  # noqa E402,F403 (linting exemptions)
>>>>>>> master


def main():
    writers = []
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nStopped!"),
                    [reader.delete() for reader in readers],
                    [writer.delete() for writer in writers],
                    sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")

    readers.append(FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL]))  # noqa: F405
    readers.append(DistanceDisplay([Miles, "Miles", "MilesTraveled", DistanceRL]))  # noqa: F405

<<<<<<< HEAD
    writers.append(MpGWriter([MpG, "MpG", "MpGCumulative"]))
=======
    writers.append(MpGWriter([MpG, "MpG", "MpGCumulative"]))  # noqa F405 (linting exemption)
>>>>>>> master

    # Add readers and start threads
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))
<<<<<<< HEAD
        
    #writer
    threadMpG = Thread(target=(writers[0].run), 
                        args=(
                            readers[0].dataQueue, 
                            readers[1].dataQueue,), 
                        daemon=True)
=======

    # writer
    threadMpG = Thread(target=(writers[0].run),
                       args=(
                            readers[0].dataQueue,
                            readers[1].dataQueue,),
                       daemon=True)
>>>>>>> master

    for thread in threads:
        thread.start()
    threadMpG.start()

    signal.pause()


main()
