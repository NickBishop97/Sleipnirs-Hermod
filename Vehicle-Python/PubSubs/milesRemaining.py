from threading import Thread
import signal
import sys

# ADT IMPORTS
sys.path.insert(0, '../ADTs/')
from Writers import *  # noqa E402,F403 (linting exemptions)
from Readers import *  # noqa E402,F403 (linting exemptions)
from Calculators import *  # noqa E402,F403 (linting exemptions)
from TopicNames import TopicNames  # noqa E402,F403 (linting exemptions)

# IDL DATA IMPORTS
sys.path.insert(1, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)
sys.path.insert(2, '../MessageFormats/MpG/')
import MpG as MpG  # noqa E402 (linting exemption)
sys.path.insert(3, '../MessageFormats/CLK/')
import CLK as CLK  # noqa E402 (linting exemption)

sys.path.insert(4, '../MessageFormats/MilesToRefuel/')
import MilesToRefuel as MilesToRefuel  # noqa E402 (linting exemption)


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

    readers.append(FuelGauge([Fuel,  # noqa: F405
                              "Fuel",
                              TopicNames.getTopicName("Fuel"),
                              FuelRL]))  # noqa: F405

    readers.append(MpGDisplay([MpG,  # noqa: F405
                               "MpG",
                               TopicNames.getTopicName("MpG"),
                               MpGRL]))  # noqa: F405

    readers.append(CLKDisplay([CLK,  # noqa: F405
                               "CLK",
                               TopicNames.getTopicName("CLK"),
                               CLKRL]))  # noqa: F405

    writers.append(MilesRemaining([MilesToRefuel,  # noqa: F405
                                   "MilesToRefuel",
                                   TopicNames.getTopicName("MilesToRefuel")],
                                   MileRemainCalc()))  # noqa: F405, E127

    # Add readers and start threads
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))

    threadMpG = Thread(target=(writers[0].run),
                       args=(
        readers[0].getData(),
        readers[1].getData(),
        readers[2].getData(),),
        daemon=True)

    for thread in threads:
        thread.start()
    threadMpG.start()

    signal.pause()


main()
