class Car():
    """A simple attemot to sepresent a car"""

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

class ElectricCar(Car):
    """Represents electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('Tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())