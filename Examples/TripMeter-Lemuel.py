import time

class TripData():

    def __init__(self, mileage, mpg, start_time, avg_speed):
        self.mileage = mileage
        self.mpg = mpg
        self.start_time = start_time
        self.avg_speed = avg_speed
    
    def get_miles_traveled(self):
        return self.mileage
    
    def get_mpg(self):
        return self.mpg
    
    def get_time(self):
        current_time = round(round(int(round(time.time() * 1000)))/1000)
        return current_time - self.start_time
    
    def get_avg_speed(self):
        return round((self.mileage/self.get_time()), 2) 
    
    def reset_data():
        self.start_mileage = 0.0
        self.mpg = 0.0
        self.start_time = 0
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
    
    def display_data_for_current_trip(self):
        print("Data for Trip Container #" + str(self.current_trip))
        print(self.trip_data_list[self.current_trip].get_miles_traveled())
        print(self.trip_data_list[self.current_trip].get_mpg())
        print(self.trip_data_list[self.current_trip].get_time())
        print(self.trip_data_list[self.current_trip].get_avg_speed())
    
    def add_trip(self, trip_i):
        self.trip_data_list.append(trip_i)
    
    def reset_data_for_current_trip(self):
        self.trip_data_list[self.current_trip].reset_data()
    
class Button():

    def __init__(self, tm):
        self.tm = tm

    def short_press():
        self.tm.change_trip()
        self.tm.display_data_for_current_trip()
    
    def long_press():
        self.tm.change_trip()
        self.tm.display_data_for_current_trip()

class Dashboard():

    def __init__(self, trip_meter):
        self.trip_meter = trip_meter
        self.button = Button(self.trip_meter)



# TESTING AREA
millisec_start = 0.0
testTD1 = TripData(25.0, 100.0, millisec_start, 35.0)
testTD2 = TripData(30.0, 90.0, millisec_start, 20.0)
testTM = TripMeter(testTD1, testTD2)
testDash = Dashboard(testTM)
testDash.button.short_press()