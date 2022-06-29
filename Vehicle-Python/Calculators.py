import time

# NOTE THAT THESE ARE SELF DEFINED CLASSES, EACH TYPE OF CLASS WILL BE DIFFERENT AND WILL HAVE DIFFERENT UNITS

class FuelConsumption:
    #CAPACITY IS INPUTTED AS GALLONS
    def __init__(self, capacity):
        #for better precision, use numpy dtype float64
        self.gallonToLiters  = float(3.785412) 
        self.capacityGallons = capacity
        self.capacityLiters  = capacity * self.gallonToLiters
        
    def consumeFuel(self, delta):
        self.capacity = self.capacity - delta
    
    #KILL SENSOR WHEN CONDITION IS MET, THIS IS A BASIC SIGNAL
    def controlSignal(self):
        time.sleep(50)
        return True
    

class DistanceTraversed:
    def __init__(self,):
        