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

    def increment_odometer(self, miles):
        """Add the given amount to odometer reading."""
        self.odometer_reading += miles