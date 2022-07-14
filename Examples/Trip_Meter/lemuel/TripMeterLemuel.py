import time

class TripData():

    current_time = 3600.0

    def __init__(self, mileage, mpg, start_time, avg_speed):
        self.mileage = mileage
        self.mpg = mpg
        self.start_time = start_time
        self.avg_speed = avg_speed
        self.return_time = 0.0
    
    def get_miles_traveled(self):
        return self.mileage
    
    def get_mpg(self):
        return self.mpg
    
    def get_time(self):
        self.return_time = self.current_time - self.start_time
        return self.return_time
    
    def get_avg_speed(self):
        a = self.mileage
        b = self.return_time
        if self.return_time == 0:
            return 0.0
        else:
            self.avg_speed = round(a/b, 2)
            return self.avg_speed
    
    def set_miles_traveled(self, miles_traveled):
        self.mileage = miles_traveled

    def set_mpg(self, mpg):
        self.mpg = mpg

    def set_avg_speed(self, avg_speed):
        self.avg_speed = avg_speed
    
    def check_for_alarm(self):
        if self.current_time < 7200:
            return "Everything good."
        elif self.current_time >= 7200:
            return "Alert! Alert!"
    
    def reset_data(self):
        self.mileage = 0.0
        self.mpg = 0.0
        self.return_time = 0.0
        self.avg_speed = 0.0



class TripMeter():

    def __init__(self, trip_a, trip_b):
        self.trip_a = trip_a
        self.trip_b = trip_b
        self.current_trip = 0
        self.trip_data_list = []
        self.trip_data_list.append(trip_a)
        self.trip_data_list.append(trip_b)
    
    def change_trip(self):
        self.current_trip += 1
        if self.current_trip >= len(self.trip_data_list):
            self.current_trip = 0

    def add_trip(self, trip_i):
        self.trip_data_list.append(trip_i)
    
    def display_miles_traveled(self):
        return self.trip_data_list[self.current_trip].get_miles_traveled()
    
    def display_mpg(self):
        return self.trip_data_list[self.current_trip].get_mpg()
    
    def display_time(self):
        return self.trip_data_list[self.current_trip].get_time()
    
    def display_avg_speed(self):
        return self.trip_data_list[self.current_trip].get_avg_speed()
    
    def check_for_alarm_for_current_trip(self):
        return self.trip_data_list[self.current_trip].check_for_alarm()

    def reset_data_for_current_trip(self):
        self.trip_data_list[self.current_trip].reset_data()



class Button():

    def __init__(self, tm):
        self.tm = tm
    
    def display(self):
        print(self.tm.display_miles_traveled())
        print(self.tm.display_mpg())
        print(self.tm.display_time())
        print(self.tm.display_avg_speed())

    def short_press(self):
        self.tm.change_trip()
        self.display()
    
    def long_press(self):
        self.tm.reset_data_for_current_trip()
        self.display()



class Dashboard():

    def __init__(self, trip_meter):
        self.trip_meter = trip_meter
        self.button = Button(self.trip_meter)