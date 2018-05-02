def open_file(filenames):
    """Opens and reads what's inside text file"""
    try:
        with open(filename) as opened_file:
            contents = opened_file.read()
    except FileNotFoundError:
        """msg = 'Sorry, the ' + filename + ' is not here! :('
        print(msg)"""
        pass
    else:
        print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    open_file(filename)