class TripData:

    # Constructor
    def __init__(self, MT, MPG, SP, TIME):

        # Instance Variables
        self.milesTraveled = MT
        self.mpg = MPG
        self.avgspeed = SP
        self.time = TIME

    def setMPG(self, MPG):
        self.mpg = MPG

    def setMT(self, MT):
        self.milesTraveled = MT

    def setSP(self, SP):
        self.avgspeed = SP

    def setTIME(self, TIME):
        self.time = TIME

    def resetData(self):
        self.milesTraveled = 0.0
        self.mpg = 0.0
        self.avgspeed = 0.0
        self.time = 0.0


class TripMeter:

    # Constructor
    def __init__(self):

        # Instance Variables
        self.currently_selected = 0
        self.trip1 = TripData(0.0, 0.0, 0.0, 0.0)
        self.trip2 = TripData(0.0, 0.0, 0.0, 0.0)

    def setCS(self, CS):
        self.currently_selected = CS

    def resetTrip(self, trip):
        trip.resetData()


class DashBoard:

    # Constructor
    def __init__(self):
        self.TM = TripMeter()


def main():
    d = DashBoard()
    d.TM.trip1.setMPG(1)
    print(d.TM.trip1.mpg)
    d.TM.trip1.resetTrip()


if __name__ == "__main__":
    main()
