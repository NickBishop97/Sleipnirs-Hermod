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

# Flask Imports
import json
import random
# from datetime import datetime

from flask import Flask, Response, render_template, stream_with_context

# ADT IMPORTS
sys.path.insert(0, '../ADTs/')
from Writers import *  # noqa E402,F403 (linting exemptions)
from Readers import *  # noqa E402,F403 (linting exemptions)
from Calculators import *  # noqa E402,F403 (linting exemptions)
from TopicNames import TopicNames

# IDL DATA IMPORTS
sys.path.insert(1, '../MessageFormats/Fuel/')
import Fuel as Fuel  # noqa E402 (linting exemption)
sys.path.insert(2, '../MessageFormats/Miles/')
import Miles as Miles  # noqa E402 (linting exemption)
sys.path.insert(3, '../MessageFormats/MpG/')
import MpG as MpG  # noqa E402 (linting exemption)
sys.path.insert(4, '../MessageFormats/LowFuelAlert/')
import LowFuelAlert as LowFuelAlert  # noqa E402 (linting exemption)
sys.path.insert(5, '../MessageFormats/MilesToRefuel/')
import MilesToRefuel as MilesToRefuel  # noqa E402 (linting exemption)
sys.path.insert(5, '../MessageFormats/CLK/')
import CLK as CLK  # noqa E402 (linting exemption)

#####################################################
#####################################################
#####################################################

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
                    'index': readers[2].getData().get()[0],
                    'mpg': readers[2].getData().get()[1],
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
                      # [reader.delete() for reader in readers],
                      sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")

    readers = []
    threads = []
    readers.append(FuelGauge([Fuel, 
                              "Fuel", 
                              TopicNames.getTopicName("Fuel"), 
                              FuelRL]))  # noqa F405 (linting exemption)
    
    readers.append(DistanceDisplay([Miles, 
                                    "Miles", 
                                    TopicNames.getTopicName("Miles"),
                                    DistanceRL]))  # noqa F405
    
    readers.append(MpGDisplay([MpG,
                               "MpG",
                               TopicNames.getTopicName("MpG"),
                               MpGRL]))  # noqa F405 (linting exemption)
    
    readers.append(LowFuelAlertDisplay([LowFuelAlert,
                                        "LowFuelAlert",
                                        TopicNames.getTopicName("LowFuelAlert"),
                                        LowFuelAlertRL]))  # noqa F405
    
    readers.append(MilesRemainDisplay([MilesToRefuel,
                                       "MilesToRefuel",
                                       TopicNames.getTopicName("MilesToRefuel"),
                                       MilesRemainRL]))  # noqa F405
    
    
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))

    for thread in threads:
        thread.start()

    application.run(debug=True, threaded=True)
    signal.pause()
