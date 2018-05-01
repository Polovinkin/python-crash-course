while True:
    name = input("Whats your name, dear guest? ")
    if name.strip() == 'quit':
        break
    with open('guest_book.txt', 'a') as guest_book:
        guest_book.write("Good morning, " + name.title() + '.\n')