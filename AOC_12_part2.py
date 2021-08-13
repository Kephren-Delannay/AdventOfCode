with open(file='AOC_12_input.txt') as f:
    data = f.read().split('\n')

def turn(degrees):
    global current_direction
    amount = int(degrees / 90)
    temp = waypoint_positions.copy()
    for i in range(4):
        _dir = directions[i]
        new_direction = int((i + amount) % 4)
        index = directions[new_direction]
        waypoint_positions[index] = temp.get(_dir)

def instruction(_instr):
    _dir = _instr[0]
    _mag = _instr[1:]
    return (_dir, _mag)

def move(_instr):
    _direction = _instr[0]
    _magnitude = int(_instr[1])

    if _direction == 'F':
        for _pos in ship_positions:
            _wp = waypoint_positions[_pos]
            ship_positions[_pos] += _wp * _magnitude
    elif _direction == 'L':
        turn(-_magnitude)
    elif _direction == 'R':
        turn(_magnitude)
    elif _direction == 'N':
        waypoint_positions['North'] += _magnitude
    elif _direction == 'S':
        waypoint_positions['South'] += _magnitude
    elif _direction == 'W':
        waypoint_positions['West'] += _magnitude
    elif _direction == 'E':
        waypoint_positions['East'] += _magnitude


def calculate_manhattan():
    east_west = abs(ship_positions.get('East') - ship_positions.get('West'))
    north_south = abs(ship_positions.get('North') - ship_positions.get('South'))
    return abs(east_west + north_south)

directions = ['North', 'East', 'South', 'West']
ship_positions = {'North' : 0, 'East' : 0, 'South' : 0, 'West' : 0}
waypoint_positions = {'North' : 1, 'East' : 10, 'South' : 0, 'West' : 0}

current_direction = 1 #East

for d in data:
    _instr = instruction(d)
    #print(_instr)
    move(_instr)
    #print('SHIP')
    #print(ship_positions)
    #print('WAYPOINT')
    #print(waypoint_positions)
    #print('----------------------------')

print(calculate_manhattan())