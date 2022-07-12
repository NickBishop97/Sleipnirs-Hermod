from Writers import *
import MilesToRefuel as MilesToRefuel
import LowFuelAlert as LowFuelAlert
import MpG as MpG
import Miles as Miles
from flask import Flask, Response, render_template, stream_with_context
from datetime import datetime
import random
import json
from Calculators import *
from Readers import *
import Fuel as Fuel
from threading import Thread
import signal
import time
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
sys.path.insert(1, '../MessageFormats/Miles/')
sys.path.insert(2, '../MessageFormats/MpG/')
sys.path.insert(3, '../MessageFormats/LowFuelAlert/')
sys.path.insert(4, '../MessageFormats/MilesToRefuel/')

# ADT IMPORTS
sys.path.insert(5, '../ADTs/')

#####################################################
#####################################################
#####################################################

#####################################################
#####################################################
#####################################################


def printer(queueList):
    while True:
        # if not queueList[0].empty():
        print(f"FUEL        :{queueList[0].get()}")
        print(f"MILES       :{queueList[1].get()}")
        print(f"MPG         :{queueList[2].get()}")
        print(f"LOWFUEL     :{queueList[3].get()}")
        print(f"MILESREMAIN :{queueList[4].get()}")
        print("\n\n")
        time.sleep(0.3)


def main():
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                      print("\nStopped!"),
                      [reader.delete() for reader in readers],
                      sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")

    readers.append(FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL]))
    readers.append(DistanceDisplay(
        [Miles, "Miles", "MilesTraveled", DistanceRL]))
    readers.append(MpGDisplay([MpG, "MpG", "MpGCumulative", MpGRL]))
    readers.append(LowFuelAlertDisplay(
        [LowFuelAlert, "LowFuelAlert", "LowFuelAlert", LowFuelAlertRL]))
    readers.append(MilesRemainDisplay(
        [MilesToRefuel, "MilesToRefuel", "MilesToRefuelTopic", MilesRemainRL]))

    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))
    threads.append(Thread(target=(printer),
                          args=([reader.dataQueue for reader in readers],),
                          daemon=True))

    for thread in threads:
        thread.start()

    signal.pause()


# main()


application = Flask(__name__)
random.seed()  # Initialize the random number generator


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/chart-data')
def chart_data():
    def generate_random_data():

        while True:
            json_data = json.dumps(
                {
                    'index': readers[2].dataQueue.get()[0],
                    'mpg': readers[2].dataQueue.get()[1],
                })
            yield f"data:{json_data}\n\n"
            time.sleep(0.25)

    response = Response(stream_with_context(
        generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response


if __name__ == '__main__':
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                      print("\nStopped!"),
                      #[reader.delete() for reader in readers],
                      sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")

    readers = []
    threads = []
    readers.append(FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL]))
    readers.append(DistanceDisplay(
        [Miles, "Miles", "MilesTraveled", DistanceRL]))
    readers.append(MpGDisplay([MpG, "MpG", "MpGCumulative", MpGRL]))
    readers.append(LowFuelAlertDisplay(
        [LowFuelAlert, "LowFuelAlert", "LowFuelAlert", LowFuelAlertRL]))
    readers.append(MilesRemainDisplay(
        [MilesToRefuel, "MilesToRefuel", "MilesToRefuelTopic", MilesRemainRL]))
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))

    for thread in threads:
        thread.start()

    application.run(debug=True, threaded=True)
    signal.pause()
