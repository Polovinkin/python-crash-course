def greet_users(names):
    """Print a simple greeting"""
    for name in names:
        msg = "Hello, " + name.title() + '!'
        print(msg)

usernames = ['hannah', 'michael', 'johnie']
greet_users(usernames)