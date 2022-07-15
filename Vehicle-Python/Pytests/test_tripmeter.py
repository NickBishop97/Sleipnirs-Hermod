from queue import Queue
import sys

#ADT IMPORTS
sys.path.insert(1, '../ADTs/')
from Calculators import TripCalc as TripCalc

#TEST: CHECK IF DATA THE DATA IS SET TO ALL ZERO/FALSE WHEN INITIALIZING 
def test_initializer():
    trip = TripCalc()
    
    assert trip.currentTripNum == 0
    assert len(trip.trips) == 2
    for i in range(len(trip.trips)):
        tripData = trip.trips[i]
        for key in tripData:
            if str(key) == "twoHours":
                assert tripData[str(key)] == False
            else:
                assert tripData[str(key)] == 0

#TEST: CHECK IF DATA UNDER ONE HOUR IS CORRECT, TRIP HAS NOT BEEN RESET
def test_update_under_hour():
    trip = TripCalc()
    
    dataArray = []

    index = 1; hoursElapsed = 1.9; 
    for i in range(4):
        q = Queue()
        q.put([index,hoursElapsed])
        dataArray.append(q)

    trip.update(dataArray)
    
    trip_dict = {
                "averageSpeed"     : hoursElapsed,
                "distance"         : hoursElapsed,
                "time"             : hoursElapsed,
                "MpG"              : hoursElapsed,
                "twoHours"         : False,
                "resetCounterDist" : 0,
                "resetCounterTime" : 0
                
            }
    
    for i in range(len(trip.trips)):
        tripData = trip.trips[i]
        assert tripData == trip_dict
        
#TEST: CHECK IF DATA OVER TWO HOURS IS CORRECT, TRIP HAS NOT BEEN RESET
def test_update_over_two_hours():
    trip = TripCalc()
    
    dataArray = []
    
    index = 1; hoursElapsed = 2; 
    for i in range(4):
        q = Queue()
        q.put([index,hoursElapsed])
        dataArray.append(q)

    trip.update(dataArray)
    
    trip_dict = {
                "averageSpeed"     : hoursElapsed,
                "distance"         : hoursElapsed,
                "time"             : hoursElapsed,
                "MpG"              : hoursElapsed,
                "twoHours"         : True,
                "resetCounterDist" : 0,
                "resetCounterTime" : 0
                
            }
    
    for i in range(len(trip.trips)):
        tripData = trip.trips[i]
        assert tripData == trip_dict


#TEST: CHECK IF THE TRIP NUMBER HAS SWITCHED 
def test_reset_switch_trips():
    trip = TripCalc()
    
    dataArray = []
    
    index = 1; allData = 2
    for i in range(4):
        q = Queue()
        q.put([index,allData])
        dataArray.append(q)

    trip.update(dataArray)
    trip.reset(2)
    
    #Trip nums are zero indexed, should move from 0 to 1
    assert trip.currentTripNum == 1
        
#TEST: CHECK IF DATA HAS BEEN RESET FOR ONE TRIP BUT NOT THE OTHER
def test_reset_one_trip():
    trip = TripCalc()
    
    dataArray = []
    
    index = 1; distanceTimeDelta = 2
    for i in range(4):
        q = Queue()
        q.put([index,distanceTimeDelta])
        dataArray.append(q)

    trip.update(dataArray)
    trip.reset(3)
    
    tripData = trip.trips[0]
    trip_dict = {
            "averageSpeed"     : 0,
            "distance"         : 0,
            "time"             : 0,
            "MpG"              : 0,
            "twoHours"         : False,
            "resetCounterDist" : distanceTimeDelta,
            "resetCounterTime" : distanceTimeDelta
            
        }
    assert tripData == trip_dict
    

    tripData = trip.trips[1]
    trip_dict = {
            "averageSpeed"     : distanceTimeDelta,
            "distance"         : distanceTimeDelta,
            "time"             : distanceTimeDelta,
            "MpG"              : distanceTimeDelta,
            "twoHours"         : True,
            "resetCounterDist" : 0,
            "resetCounterTime" : 0
            
        }
    assert tripData == trip_dict 

            
#TEST: CHECK IF DISTANCE IS CORRECT FOR A TRIP AFTER THE RESET AND THEN UPDATING THE TRIP
def test_reset_after_trip():
    trip = TripCalc()
    
    dataArray = []
    
    index = 1; distanceTimeDelta = 1
    for i in range(4):
        q = Queue()
        q.put([index,distanceTimeDelta])
        dataArray.append(q)
    trip.update(dataArray)
    
    trip.reset(3)
    
    dataArrayTwo = []
    for i in range(4):
        q = Queue()
        q.put([index + 1,distanceTimeDelta + 0.5])
        dataArrayTwo.append(q)
    trip.update(dataArrayTwo)
    
    tripData = trip.trips[0]
    trip_dict = {
            "averageSpeed"     : distanceTimeDelta + 0.5,
            "distance"         : (distanceTimeDelta + 0.5) - distanceTimeDelta,
            "time"             : (distanceTimeDelta + 0.5) - distanceTimeDelta,
            "MpG"              : distanceTimeDelta + 0.5,
            "twoHours"         : False,
            "resetCounterDist" : distanceTimeDelta,
            "resetCounterTime" : distanceTimeDelta
            
        }
    assert tripData == trip_dict
            
    tripData = trip.trips[1]
    trip_dict = {
            "averageSpeed"     : distanceTimeDelta + 0.5,
            "distance"         : distanceTimeDelta + 0.5,
            "time"             : distanceTimeDelta + 0.5,
            "MpG"              : distanceTimeDelta + 0.5,
            "twoHours"         : False,
            "resetCounterDist" : 0,
            "resetCounterTime" : 0
            
        }

