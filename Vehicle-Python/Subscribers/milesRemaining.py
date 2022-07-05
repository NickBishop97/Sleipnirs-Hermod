from threading import Thread
import signal
import time
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../PubSubs/')
import mpgWriter

#ADT IMPORTS
sys.path.insert(2, '../ADTs/')
from Readers import *


# Displays the Miles Remaining
def calc(milesQueue):
  while True:
    time.sleep(0.25)
    if not milesQueue.empty():
      print(f"Distance Travelled: {milesQueue.get()}")


def main():
    readers = []
    threads = []

    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nStopped!"),
                    sys.exit(0),
                  ))

    MilesReader = DistanceDisplay([Miles, "Miles", "MilesTraveled", DistanceRL])  # noqa: F405
    readers.append(MilesReader)

    DistThread = Thread(target=(MilesReader.run), daemon=True)
    CalcThread = Thread(
                        target = (calc),
                        args = (
                          readers[0].dataQueue,
                        ),
                        daemon = True,
                        )

    threads.append(DistThread)
    threads.append(CalcThread)

    for thread in threads:
      thread.start()

    signal.pause()


main()