class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initiate name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in responce to a command"""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in responce to a command"""
        print(self.name.title() + " rolled over!")

my_dog = Dog('Willie', 7)
your_dog = Dog("Lucie", 5)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()