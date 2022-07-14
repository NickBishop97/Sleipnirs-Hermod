class TripData:

    # Constructor
    def __init__(self, MT, MPG, SP, TIME):

        # Instance Variables
        self.milesTraveled = MT
        self.mpg = MPG
        self.avgspeed = SP
        self.time = TIME

    def updateData(self, MT, MPG, SP, TIME):
        if MT >= 0 and MPG >= 0 and SP >= 0 and TIME >= 0:
            self.milesTraveled = MT
            self.mpg = MPG
            self.avgspeed = SP
            self.time = TIME

    def resetData(self):
        self.milesTraveled = 0.0
        self.mpg = 0.0
        self.avgspeed = 0.0
        self.time = 0.0


class TripMeter:

    # Constructor
    def __init__(self):
        self.currently_selected = 0
        self.trip1 = TripData(0.0, 0.0, 0.0, 0.0)
        self.trip2 = TripData(0.0, 0.0, 0.0, 0.0)

    def curentTrip(self):
        if self.currently_selected == 0:
            return self.trip1
        else:
            return self.trip2

    def updateTrip(self, MT, MPG, SP, TIME):
        self.trip1.updateData(MT, MPG, SP, TIME)
        self.trip2.updateData(MT, MPG, SP, TIME)

    def resetTrip(self, trip):
        trip.resetData()


class Button:

    def __init__(self, TM):
        self.TripMeter = TM

    def click(self):
        if self.TripMeter.currently_selected == 0:
            self.TripMeter.currently_selected = 1
        else:
            self.TripMeter.currently_selected = 0

    def longclick(self):
        self.TripMeter.resetTrip(self.TripMeter.curentTrip())


class DashBoard:

    # Constructor
    def __init__(self):
        self.TM = TripMeter()
        self.BT = Button(self.TM)

    def showTrip(self):
        temp = self.TM.curentTrip()
        print(temp.mpg, "Mpg")
        print(temp.milesTraveled, "Mls")
        print(temp.avgspeed, "Mph")
        print(temp.time, "Hrs")

    def checkTime(self):
        temp = self.TM.curentTrip()
        if temp.time >= 2:
            # print("Drive Time over 2Hrs")
            return 1
        else:
            return 0


# def main():
    # d = DashBoard()
    # d.showTrip()


# if __name__ == "__main__":
    # main()
