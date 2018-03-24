car = "BMW"
if car == "audi":
    print("I like audi!")
else:
    print("Well, it's another one!")

game1 = "Overwatch"
game2 = "WoW"
if game1 == game2:
    print("They are the same")
else:
    print("Different games they are!")

name1 = "Dmitry"
name2 = "dmitry"
if name1.lower() == name2.lower():
    print("The name is aready used!")
else:
    print("They are different!")

menu = ["shrimps", "potatoes", "cake"]
if "cake" in menu:
    print("the cake is there already")
else:
    print("I forgot to add a cake!")

new_menu = ["pie", "sushi", "green_stuff", "cabbage"]
if "cabbage" not in new_menu:
    print("I need to add a cabbage!")
else:
    print("Cabbage is there.")