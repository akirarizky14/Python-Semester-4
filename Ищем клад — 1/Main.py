the_minimum_number_of_instructions = 0
x = int(input())
y = int(input())
x_y = [0, 0]
direction_of_movement = input()
if x == 0 and y == 0:
    print(0)
while direction_of_movement != 'стоп':
    steps = int(input())
    the_minimum_number_of_instructions += 1
    if direction_of_movement == 'север':
        x_y[1] += steps
    elif direction_of_movement == 'запад':
        x_y[0] -= steps
    elif direction_of_movement == 'юг':
        x_y[1] -= steps
    elif direction_of_movement == 'восток':
        x_y[0] += steps
    if int(x) == x_y[0] and int(y) == x_y[1]:
        print(the_minimum_number_of_instructions)
        break
    direction_of_movement = input()