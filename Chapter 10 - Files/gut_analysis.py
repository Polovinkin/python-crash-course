with open('gutenberg.txt') as opened_gut:
    gut = opened_gut.read()
    count = gut.lower().count('the')
    print(count)

#Not working heh, dunno why