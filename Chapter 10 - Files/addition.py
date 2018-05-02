while True:
    x = input('First number: ')
    y = input('Second number: ')
    if x == 'q' or y == 'q':
        break
    try:
        c = int(x) + int(y)
    except ValueError:
        msg = 'Please, input the numbers!'
        print(msg)
    else:
        print('The sum is: ' + c)