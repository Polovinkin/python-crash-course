from random import randint

class Die():
    """Rolls a die with sides as argument"""
    
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        number = randint(1, self.sides)
        return(number)
    
dice = Die(20)
results = []

for i in range(10):
    result = dice.roll_die()
    results.append(result)
    i += 1
print(results)