class Restaurant():
    """Some info about restaurants you know."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initiate name ant cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Printing the name of the restaurant"""
        print('The restaurant is called ' + self.restaurant_name.title()
              + ' and you can taste some real ' + self.cuisine_type.title() + ' cuisine there!')
    
    def open_restaurant(self):
        """Stating that restaurant is open"""
        print('The ' + self.restaurant_name.title() + ' is totally open for visitors!')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number_inc):
        self.number_served += number_inc

restaurant = Restaurant('dubaevsk', 'european')
print(restaurant.number_served)

restaurant.number_served += 10
print(restaurant.number_served)

restaurant.set_number_served(50)
print(restaurant.number_served)

restaurant.increment_number_served(500)
print(restaurant.number_served)