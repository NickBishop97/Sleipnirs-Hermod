<<<<<<< HEAD
=======
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
>>>>>>> master
from threading import Thread
import signal
import time
import sys

<<<<<<< HEAD
# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel
sys.path.insert(1, '../MessageFormats/Miles/')
import Miles as Miles  
sys.path.insert(2, '../MessageFormats/MpG/')
import MpG as MpG  
sys.path.insert(3, '../MessageFormats/LowFuelAlert/')
import LowFuelAlert as LowFuelAlert  
sys.path.insert(4, '../MessageFormats/MilesToRefuel/')
import MilesToRefuel as MilesToRefuel  

#ADT IMPORTS
sys.path.insert(5, '../ADTs/')
#from Writers import *  
from Readers import *
#from Calculators import *
from TopicNames import TopicNames
=======
# Flask Imports
import json
import random
# from datetime import datetime

from flask import Flask, Response, render_template, stream_with_context

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)
sys.path.insert(1, '../MessageFormats/Miles/')
import Miles as Miles  # noqa E402 (linting exemption)
sys.path.insert(2, '../MessageFormats/MpG/')
import MpG as MpG  # noqa E402 (linting exemption)
sys.path.insert(3, '../MessageFormats/LowFuelAlert/')
import LowFuelAlert as LowFuelAlert  # noqa E402 (linting exemption)
sys.path.insert(4, '../MessageFormats/MilesToRefuel/')
import MilesToRefuel as MilesToRefuel  # noqa E402 (linting exemption)

# ADT IMPORTS
sys.path.insert(5, '../ADTs/')
from Writers import *  # noqa E402,F403 (linting exemptions)
from Readers import *  # noqa E402,F403 (linting exemptions)
from Calculators import *  # noqa E402,F403 (linting exemptions)

>>>>>>> master

#####################################################
#####################################################
#####################################################

#####################################################
#####################################################
#####################################################

<<<<<<< HEAD
def printer(queueList):
    while True:
        #if not queueList[0].empty():
=======

def printer(queueList):
    while True:
        # if not queueList[0].empty():
>>>>>>> master
        print(f"FUEL        :{queueList[0].get()}")
        print(f"MILES       :{queueList[1].get()}")
        print(f"MPG         :{queueList[2].get()}")
        print(f"LOWFUEL     :{queueList[3].get()}")
        print(f"MILESREMAIN :{queueList[4].get()}")
        print("\n\n")
<<<<<<< HEAD
        time.sleep(0.3)  
        
import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template, stream_with_context
=======
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

    readers.append(FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL]))  # noqa F405 (linting exemption)
    readers.append(DistanceDisplay([Miles, "Miles", "MilesTraveled", DistanceRL]))  # noqa F405 (linting exemption)
    readers.append(MpGDisplay([MpG, "MpG", "MpGCumulative", MpGRL]))  # noqa F405 (linting exemption)
    readers.append(LowFuelAlertDisplay([LowFuelAlert, "LowFuelAlert", "LowFuelAlert", LowFuelAlertRL]))  # noqa F405
    readers.append(MilesRemainDisplay([MilesToRefuel, "MilesToRefuel", "MilesToRefuelTopic", MilesRemainRL])) # noqa F405

    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))
    threads.append(Thread(target=(printer),
                          args=([reader.dataQueue for reader in readers],),
                          daemon=True))

    for thread in threads:
        thread.start()

    signal.pause()


# main()
>>>>>>> master

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
<<<<<<< HEAD
                'index': readers[2].getDataQueue().get()[0], 
                'mpg': readers[2].getDataQueue().get()[1],
                 })
            yield f"data:{json_data}\n\n"
            time.sleep(0.25)

    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
=======
                    'index': readers[2].dataQueue.get()[0],
                    'mpg': readers[2].dataQueue.get()[1],
                })
            yield f"data:{json_data}\n\n"
            time.sleep(0.25)

    response = Response(stream_with_context(
        generate_random_data()), mimetype="text/event-stream")
>>>>>>> master
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response


if __name__ == '__main__':
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nStopped!"),
<<<<<<< HEAD
                    #[reader.delete() for reader in readers],
=======
                    # [reader.delete() for reader in readers],
>>>>>>> master
                    sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")
<<<<<<< HEAD
    
    readers = []
    threads = []
    readers.append(FuelGauge([Fuel, 
                              "Fuel", 
                              TopicNames.getTopicName("Fuel"), 
                              FuelRL]))
    readers.append(DistanceDisplay([Miles, 
                                    "Miles", 
                                    TopicNames.getTopicName("Miles"), 
                                    DistanceRL]))
    readers.append(MpGDisplay([MpG, 
                               "MpG", 
                               TopicNames.getTopicName("MpG"), 
                               MpGRL]))
    readers.append(LowFuelAlertDisplay([LowFuelAlert, 
                                        "LowFuelAlert", 
                                        TopicNames.getTopicName("LowFuelAlert"), 
                                        LowFuelAlertRL]))
    readers.append(MilesRemainDisplay([MilesToRefuel, 
                                       "MilesToRefuel", 
                                       TopicNames.getTopicName("MilesToRefuel"), 
                                       MilesRemainRL]))
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))
    
    for thread in threads:
        thread.start()
        
    application.run(host="localhost", port=8000, debug=True, threaded=True)
    signal.pause()


=======

    readers = []
    threads = []
    readers.append(FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL])) # noqa F405 (linting exemption)
    readers.append(DistanceDisplay([Miles, "Miles", "MilesTraveled", DistanceRL]))  # noqa F405
    readers.append(MpGDisplay([MpG, "MpG", "MpGCumulative", MpGRL]))  # noqa F405 (linting exemption)
    readers.append(LowFuelAlertDisplay([LowFuelAlert, "LowFuelAlert", "LowFuelAlert", LowFuelAlertRL]))  # noqa F405
    readers.append(MilesRemainDisplay([MilesToRefuel, "MilesToRefuel", "MilesToRefuelTopic", MilesRemainRL]))  # noqa F405
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))

    for thread in threads:
        thread.start()

    application.run(debug=True, threaded=True)
    signal.pause()
>>>>>>> master
