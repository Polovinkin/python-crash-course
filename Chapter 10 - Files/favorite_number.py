import json

def create_file():
    """Creates file with favourite number"""
    number = input('Whats your favourite number? ')
    fav_number_file = 'username.json'
    with open(fav_number_file, 'w') as f_obj:
        json.dump(number, f_obj)

def open_file():
    """Opens file with username"""
    fav_number_file = 'username.json'
    try:
        with open(fav_number_file) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        create_file()

#Well, I've got an idea, lets move to real project already!

