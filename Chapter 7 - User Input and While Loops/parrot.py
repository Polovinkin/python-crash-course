prompt = '\nTell me something and I will return it to you!'
prompt += '\nType "quit" to end the program. Type here: '

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)