from threading import Condition
import time
import random
import sys
import psutil

#IDL DATA IMPORTS
sys.path.insert(0, './Fuel/')
import Fuel as F
sys.path.insert(1, './Miles/')
import Miles as M

from Writers import Fuel, Miles

import subprocess

#print('\nStarting publisher.')
#fuelWriter = Fuel(F, "Fuel", "FuelRemaining")
#fuelWriter.run()

#mileSensor = Miles(M, "Miles", "MilesTraveled")
#mileSensor.run()
