class User():
    """Something something user info"""

    def __init__(self, first_name, last_name, age):
        """Initiate first and last names here"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describe_user(self):
        print("User's name is " + self.first_name.title() + " " 
              + self.last_name.title() + " and he/she is " + str(self.age) + " years old.")

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ", welcome back!")
    
john = User('john', 'stevenson', 29)
kristie = User('kristie', 'hawking', 36)

john.describe_user()
john.greet_user()

kristie.describe_user()
kristie.greet_user()