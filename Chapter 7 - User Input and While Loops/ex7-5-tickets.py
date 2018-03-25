while True:
    age = input("\nWhat is your age? ")
    if age != 'quit':
        if int(age) < 3:
            print("The ticket if free for you!")
            break
        elif int(age) < 12:
            print("The ticket if 10$ for you!")
            break
        else:
            print("The ticket if 15$ for you!")
            break
    else:
        break