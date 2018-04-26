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

class Battery():
    """Modelling a battery"""

    def __init__(self, battery_size=70):
        """Initialize the battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print('That car has a ' + str(self.battery_size) + 'kWh battery')

class ElectricCar(Car):
    """Represents electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class.
        Then initialize attributes specific to electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('Tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()