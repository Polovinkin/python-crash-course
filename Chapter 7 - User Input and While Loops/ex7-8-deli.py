sandwich_orders = ['chicken sandwich', 'pastrami', 'carry sandwich', 'beef sandwich', 'pastrami',
                   'vegan sandwich', 'pastrami']

finished_sandwiches = []

if 'pastrami' in sandwich_orders:
    print("Sorry, but we are out of pastrami!")
    for sandwich in sandwich_orders:
        if sandwich == 'pastrami':
            sandwich_orders.remove(sandwich)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I've made you a " + sandwich + '.')
    finished_sandwiches.append(sandwich)

print("\nHere, some sandwiches for you: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())