import TripMeter


class StickButton:
    def __init__(self):
        self.longPress = False
        self.shortPress = True

class Dashboard:
    def __init__(self):
        self.tm = TripMeter()
        self.b = StickButton()
        self.fg = FuelGauge()
        self.m = MilesSensor()

    def 
