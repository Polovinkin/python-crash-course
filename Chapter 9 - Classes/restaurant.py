class Restaurant():
    """Some info about restaurants you know."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initiate name ant cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Printing the name of the restaurant"""
        print('The restaurant is called ' + self.restaurant_name.title()
              + ' and you can taste some real ' + self.cuisine_type.title() + ' cuisine there!')
    
    def open_restaurant(self):
        """Stating that restaurant is open"""
        print('The ' + self.restaurant_name.title() + ' is totally open for visitors!')

palkin = Restaurant('palkin', 'russian')

palkin.describe_restaurant()
palkin.open_restaurant()