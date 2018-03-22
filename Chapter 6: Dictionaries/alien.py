alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position is ' + str(alien_0['x_position']))

# Move alien to the right
# Determine how far to move the alien based on it's current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # That must be a fast one!
    x_increment = 3

# The new position is the old one plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New position: ' + str(alien_0['x_position']))