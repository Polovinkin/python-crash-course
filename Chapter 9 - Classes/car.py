"""A class that can be used to represent a car."""

class Car():
    """A simple attempt to sepresent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print the statement showing the car mileage"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        """Set odometer meter to given number"""
        self.odometer_reading = mileage

    def imcrement_odometer(self, miles):
        """Add the given amount to odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a5', 2014)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23000)
my_new_car.read_odometer()

my_new_car.imcrement_odometer(100)
my_new_car.read_odometer()