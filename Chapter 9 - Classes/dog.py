class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initiate name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in responce to a command"""
        print(self.name.title() + "is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in responce to a command"""
        print(self.name.title() + " rolled over!")