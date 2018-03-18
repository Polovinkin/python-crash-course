my_foods = ["pizza", "pasta", "carrot"]
friend_food = my_foods[:]
print(friend_food)
my_foods.append("ice_cream")
friend_food.append("salami")
print("My friend's food are:")
for item in friend_food:
    print(item.title())