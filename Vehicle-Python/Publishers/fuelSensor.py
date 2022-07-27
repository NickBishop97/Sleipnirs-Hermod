import Fuel as Fuel
import CLK as CLK
from Calculators import FuelConsump
from TopicNames import TopicNames
from Readers import CLKDisplay, CLKRL
from Writers import FuelWriter
import signal
import sys
from threading import Thread

# ADT IMPORTS
sys.path.insert(0, '../ADTs/')


# IDL DATA IMPORTS
sys.path.insert(1, '../MessageFormats/CLK/')

sys.path.insert(2, '../MessageFormats/Fuel/')


def runSensor():
    writers = []
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                      print("\nInterrupted!\n"),
                      fuelWriter.setStopSignal(True),
                      [thread.join for thread in threads],
                      [reader.delete() for reader in readers],
                      [writer.delete() for writer in writers],
                      sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")

    # MAKING THREADS TO RUN READER AND WRITER OBJECTS
    fuelWriter = FuelWriter([Fuel,
                             "Fuel",
                             TopicNames.getTopicName("Fuel")],
                            FuelConsump(100, 100, 0.01))

    clkReader = CLKDisplay([CLK,
                            "CLK",
                            TopicNames.getTopicName("CLK"),
                            CLKRL])  # noqa: F405

    readers.append(clkReader)
    writers.append(fuelWriter)

    # Add readers and start threads
    CLKThread = Thread(target=(clkReader.run), daemon=True)
    FuelThread = Thread(target=(fuelWriter.run),
                        args=(readers[0].getData(),),
                        daemon=True)

    threads.append(CLKThread)
    threads.append(FuelThread)

    for thread in threads:
        thread.start()

    signal.pause()


runSensor()
