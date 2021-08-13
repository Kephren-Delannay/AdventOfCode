with open(file='AOC_12_input.txt') as f:
    data = f.read().split('\n')

def instruction(_instruction):
    '''
    return the direction and magnitude of the movement vector as a tuple
    '''
    _dir = _instruction[0]
    _mag = _instruction[1:]
    return (_dir, _mag)

def turn(degrees):
    global current_direction
    amount = degrees / 90
    new_direction = (current_direction + amount) % 4
    current_direction = int(new_direction)
    
def move(_instruction):
    global positions, current_direction
    _direction = _instruction[0]
    _magnitude = int(_instruction[1])

    if _direction == 'F':
        positions[directions[current_direction]] += _magnitude
    elif _direction == 'L':
        turn(-_magnitude)
    elif _direction == 'R':
        turn(_magnitude)
    elif _direction == 'N':
        positions['North'] += _magnitude
    elif _direction == 'S':
        positions['South'] += _magnitude
    elif _direction == 'W':
        positions['West'] += _magnitude
    elif _direction == 'E':
        positions['East'] += _magnitude

def calculate_manathan_position():
    global positions
    east_west = abs(positions.get('East') - positions.get('West'))
    north_south = abs(positions.get('North') - positions.get('South'))
    return abs(east_west + north_south)


directions = ['North', 'East', 'South', 'West']
positions = {'North' : 0, 'South' : 0, 'East' : 0, 'West' : 0}

current_direction = 1 #East

for d in data:
    _instr = instruction(d)
    print(_instr)
    move(_instr)
    print(positions)

print(calculate_manathan_position())


