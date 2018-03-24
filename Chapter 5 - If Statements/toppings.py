avaliable_toppings = ['mushrooms', 'cheese', 'olives', 'onion',
                      'pepperoni', 'love']

requested_toppings = ['mushrooms', 'french fries', 'cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print('Adding ' + requested_topping + '...')
    else:
        print('Sorry, ' + requested_topping + ' is not avaliable!')

print('\nFinished making a pizza!')