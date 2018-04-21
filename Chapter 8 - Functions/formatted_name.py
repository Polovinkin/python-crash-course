def get_formatted_name(first_name, second_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + second_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)