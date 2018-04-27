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

class Priveleges():
    def __init__(self, priveleges_list):
        """Different priveleges"""
        self.priveleges_list = ['can add post', 'can delete post', 'can ban users']

    def show_priveleges(self):
        print('Has priveleges: ' + str(self.priveleges_list) + '.')

class Admin(User):
    def __init__(self, first_name, last_name, age):
        """Admin info"""
        super().__init__(first_name, last_name, age)
        self.admin_priveleges = Priveleges(self)

administrator = Admin('Dmitry', 'Polovinkin', 23)
administrator.admin_priveleges.show_priveleges()

john = User('john', 'stevenson', 29)
kristie = User('kristie', 'hawking', 36)

john.describe_user()
john.greet_user()

kristie.describe_user()
kristie.greet_user()