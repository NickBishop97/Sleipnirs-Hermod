"""@package docstring
This py file starts up and runs the clk signal for syncing purposes

@author Maxwell Rosales
@version 0.1
@date 2022-07-21
@copyright Copyright (c) 2022
"""
import signal
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/CLK/')
import CLK as CLK  # noqa E402,F403 (linting exemptions)

# ADT IMPORTS
sys.path.insert(1, '../ADTs/')
from Writers import CLKWriter  # noqa E402,F403 (linting exemptions)
from TopicNames import TopicNames  # noqa E402,F403 (linting exemptions)


# MAIN
def runSensor() -> None:
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                      print("\nInterrupted!\n"),
                      clkWriter.setStopSignal(True),
                      clkWriter.delete(),
                      exit(),
                  ))

    print('\nStarting publisher.')

    clkPeriod = 0.25 / 2.0
    clkWriter = CLKWriter([CLK,
                           "CLK",
                           TopicNames.getTopicName("CLK")],
                          clkPeriod)

    clkWriter.run()
    signal.pause()


runSensor()
