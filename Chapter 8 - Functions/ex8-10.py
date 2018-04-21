magicians = ['charlie', 'alex', 'steven']
mod_magicians = []

def show_magicians(list_name):
    for item in list_name:
        print(item.title() + ' is the real magician!')

show_magicians(magicians)


def make_great(list_name):
    while magicians:
        magician = magicians.pop()
        mod_magicians.append('the Great ' + magician)

make_great(mod_magicians)
show_magicians(mod_magicians)