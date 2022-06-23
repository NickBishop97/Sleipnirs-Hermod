from queue import Queue
from threading import Thread
import signal
import time

import sys

sys.path.insert(0, '/home/n13853/n13853/dev/sleipnir/fastdds_examples/HelloWorld/')
import HelloWorld

sys.path.insert(1, '/home/n13853/n13853/dev/sleipnir/fastdds_examples/Fuel')
import Fuel

import fastdds
from Readers import FuelGauge, FuelRL, Hello, HelloRL


def controlSignal():
    time.sleep(50)
    return True

def calc(inputQueue):
    while True:
        time.sleep(1)
        if not inputQueue.empty():
            print(f"This the queue data: {inputQueue.get()}\n\n")

        

def main():
    signal.signal(signal.SIGINT, 
                    lambda sig, frame : (
                        print("\nInterrupted!\n"),
                        exit(),
                    ))

    readerFuel  = FuelGauge(Fuel, "Fuel", "FuelRemaining", FuelRL, controlSignal)
    #readerHello = Hello(HelloWorld, "HelloWorld", "HelloWorldTopic1846",  HelloRL, controlSignal)

    threadFuel  = Thread(target=(readerFuel.run))
    #threadHello = Thread(target=(readerHello.run))
    threadCalc  = Thread(target=(calc), args=(readerFuel.dataQueue,))
    
    threadFuel.start()
    #threadHello.start()
    threadCalc.start()

    signal.pause()
    readerFuel.delete()
    exit()


main()