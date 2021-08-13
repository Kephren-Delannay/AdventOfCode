with open(file="AOC_11_input.txt") as f:
    _data= f.read().split('\n')

data = []
for i in range(len(_data)):
    data.append(list(_data[i]))

def visibility(seat_row, seat_col):
    seats = []
    #look for up
    _y = seat_row - 1
    while _y >= 0:
        next_seat = data[_y][seat_col]
        if next_seat != '.':
            seats.append(next_seat)
            break
        _y -= 1
    #look for down
    _y = seat_row + 1
    while _y < len(data):
        next_seat = data[_y][seat_col]
        if next_seat != '.':
            seats.append(next_seat)
            break
        _y += 1
    #look for right
    _x = seat_col + 1
    while _x < len(data[0]):
        next_seat = data[seat_row][_x]
        if next_seat != '.':
            seats.append(next_seat)
            break
        _x += 1
    #look for left
    _x = seat_col - 1
    while _x >= 0:
        next_seat = data[seat_row][_x]
        if next_seat != '.':
            seats.append(next_seat)
            break
        _x -= 1
    #look for diagonnaly up-left
    _x = seat_col - 1
    _y = seat_row - 1
    while _x >= 0 and _y >= 0:
        next_seat = data[_y][_x]
        if next_seat != '.':
            seats.append(next_seat)
            break
        _x -= 1
        _y -= 1
    #look for diagonnaly up-right
    _x = seat_col + 1
    _y = seat_row - 1
    while _x < len(data[0]) and _y >= 0:
        next_seat = data[_y][_x]
        if next_seat != '.':
            seats.append(next_seat)
            break
        _x += 1
        _y -= 1
    #look for diagonnaly down-left
    _x = seat_col - 1
    _y = seat_row + 1
    while _x >= 0 and _y < len(data):
        next_seat = data[_y][_x]
        if next_seat != '.':
            seats.append(next_seat)
            break
        _x -= 1
        _y += 1
    #look for diagonnaly down-right
    _x = seat_col + 1
    _y = seat_row + 1
    while _x < len(data[0]) and _y < len(data):
        next_seat = data[_y][_x]
        if next_seat != '.':
            seats.append(next_seat)
            break
        _x += 1
        _y += 1

    
    return seats

def seat(seat_row, seat_col):
    if data[seat_row][seat_col] == 'L':
        _seats = visibility(seat_row, seat_col)
        if not ('#' in _seats):
            return '#'
        else:
            return 'L'
    elif data[seat_row][seat_col] == '#':
        _seats = visibility(seat_row, seat_col)
        if _seats.count('#') >= 5:
            return 'L'
        else:
            return '#'
    else:
        return data[seat_row][seat_col]

def round():
    global data
    '''
    simulate a round of simulation
    '''
    next_data = [x[:] for x in data]
    for y in range(len(data)):
        for x in range(len(data[0])):
            next_data[y][x] = seat(y, x)
    data = next_data

def render(d):
    for row in d:
        print(''.join(row)) 

previous = []
for i in range(1000):
    print('-------------------' + str(i) + '--------------------')
    round()
    render(data)
    if data == previous:
        break
    previous = [x[:] for x in data]

s=[]
for line in data:
    s.append(line.count('#'))
print(sum(s))