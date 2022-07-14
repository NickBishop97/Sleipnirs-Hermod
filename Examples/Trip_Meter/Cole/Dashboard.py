from trip_meter import TripMeter
import random


# Button Status Codes
NO_PRESS = 0
SHORT_PRESS = 1
LONG_PRESS = 2


# Time (in s) required for long button press
LONG_THRESH = 1


class StickButton:
    def __init__(self):
        self.longPress = False
        self.shortPress = False

    def getButtonType(pressTime):
        if pressTime >= LONG_THRESH:
            return LONG_PRESS
        elif pressTime > 0:
            return SHORT_PRESS
        else:
            return NO_PRESS


class Dashboard:
    def __init__(self):
        self.tm = TripMeter()
        self.b = StickButton()
        self.fg = FuelGauge()
        self.m = MilesSensor()

    def getCurrentMileage(self):
        # Get current mileage from dds here
        # For this example we will just choose a random number
        return random.uniform(0, 20000)

    def getCurrentFuel(self):
        # Get current fuel level from dds here
        # For this example we will just choose a random number
        return random.uniform(0, 25)

    def getCurrentTime(self):
        # Get current UTC time or time from some system clock here
        # For this example it will just be a random number
        return random.uniform(1, 600)

    def sendToMeter(self, pressTime):
        buttonType = self.b.getButtonType(pressTime)
        if buttonType == SHORT_PRESS:
            self.tm.toggleTrip()
            if self.tm.getMileage(self.getCurrentMileage()) == 0:  # If meter cleared or uninitialized
                self.tm.startNewTrip(self.getCurrentMileage(), self.getCurrentFuel())
        elif buttonType == LONG_PRESS:
            self.tm.clear()

    def displayMpg(self):
        return self.tm.getAvMpg(self.getCurrentMileage(), self.getCurrentFuel())
        # Should send to topic instead of returning in actual implementation

    def displaySpeed(self):
        return self.tm.getAvSpeed(self.getCurrentMileage(), self.getCurrentTime())
        # Should send to speed topic instead of returning when actually implemented