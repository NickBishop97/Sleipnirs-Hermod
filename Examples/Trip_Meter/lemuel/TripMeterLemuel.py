# Trip Meter Program to simulate a trip meter
# ===========================================



# Class that will hold data and return calculations
# --------------------------------------------------
class TripData():

    current_time = 3600.0 # class variable to hold time that has passed.

    # initialization function
    def __init__(self, mileage, mpg, start_time, avg_speed):
        self.mileage = mileage       # amount of miles traveled
        self.mpg = mpg               # miles per gallon passed
        self.start_time = start_time # amount of seconds in record when the system starts
        self.avg_speed = avg_speed   # average speed that is being traveled
        self.return_time = 0.0       # amount of seconds returned when time is calculated
    
    # return amont of miles traveled
    def get_miles_traveled(self):
        return self.mileage
    
    # return current miles per gallon
    def get_mpg(self):
        return self.mpg
    
    # calculate time that has passed and return the value
    def get_time(self):
        self.return_time = self.current_time - self.start_time
        return self.return_time
    
    # calculate average speed using miles traveled and returned time and return the value
    def get_avg_speed(self):
        a = self.mileage
        b = self.return_time

        # if calculation will result in division by zero, return zero. otherwise, do calculation
        if self.return_time == 0:
            return 0.0
        else:
            self.avg_speed = round(a/b, 2)
            return self.avg_speed
    
    # manually set the amount of miles traveled
    def set_miles_traveled(self, miles_traveled):
        self.mileage = miles_traveled

    # manually set the miles per gallon
    def set_mpg(self, mpg):
        self.mpg = mpg
    
    # manually set the average speed of the system
    def set_avg_speed(self, avg_speed):
        self.avg_speed = avg_speed
    
    # if amount of time traveled is greater than 2 hours, trigger an alarm. otherwise, return that everything is ok
    def check_for_alarm(self):
        if self.current_time < 7200:
            return "Everything good."
        elif self.current_time >= 7200:
            return "Alert! Alert!"
    
    # reset all of the data values to 0
    def reset_data(self):
        self.mileage = 0.0
        self.mpg = 0.0
        self.return_time = 0.0
        self.avg_speed = 0.0



# Class that will hold and manage trip data objects
# --------------------------------------------------
class TripMeter():

    # initialization function
    def __init__(self, trip_a, trip_b):
        self.trip_a = trip_a               # initialize trip meter object with trip data a
        self.trip_b = trip_b               # initialize trip meter object with trip data b
        self.current_trip = 0              # index variable to access list of trip data objects
        self.trip_data_list = []           # list to hold all trip data objects 
        self.trip_data_list.append(trip_a) # add trip data object to trip meter list
        self.trip_data_list.append(trip_b) # add trip data object to trip meter list
    
    # change trip data that is being shown
    def change_trip(self):
        self.current_trip += 1
        # if index goes beyond the scope of the list, reset back to first place
        if self.current_trip >= len(self.trip_data_list):
            self.current_trip = 0
    
    # add trip data object to trip meter list
    def add_trip(self, trip_i):
        self.trip_data_list.append(trip_i)
    
    # display miles traveled from currently selected trip data object
    def display_miles_traveled(self):
        return self.trip_data_list[self.current_trip].get_miles_traveled()
    
    # display miles per gallon from currently selected trip data object
    def display_mpg(self):
        return self.trip_data_list[self.current_trip].get_mpg()
    
    # display returned time from currently selected trip data object
    def display_time(self):
        return self.trip_data_list[self.current_trip].get_time()
    
    # display current average speed from currently selected trip data object
    def display_avg_speed(self):
        return self.trip_data_list[self.current_trip].get_avg_speed()
    
    # determine if the time alarm will go off
    def check_for_alarm_for_current_trip(self):
        return self.trip_data_list[self.current_trip].check_for_alarm()
    
    # reset data for currently selected trip data
    def reset_data_for_current_trip(self):
        self.trip_data_list[self.current_trip].reset_data()



# Class that will simulate a button and hold a trip meter object
class Button():

    # initialization function
    def __init__(self, tm):
        self.tm = tm
    
    # display data from trip meter's currently selected trip data
    def display(self):
        print(self.tm.display_miles_traveled())
        print(self.tm.display_mpg())
        print(self.tm.display_time())
        print(self.tm.display_avg_speed())

    # simulate a short press to change display between the trip data objects
    def short_press(self):
        self.tm.change_trip()
        self.display()
    
    # simulate a long press to reset the values of the currently selected trip data object
    def long_press(self):
        self.tm.reset_data_for_current_trip()
        self.display()



# Dashboard that will simulate the display of a car and will also hold a button object
class Dashboard():

    def __init__(self, trip_meter):
        self.trip_meter = trip_meter          # initialize a trip meter object to give to the button object
        self.button = Button(self.trip_meter) # initialize a button object with a trip meter object