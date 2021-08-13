with open(file="AOC_11_input.txt") as f:
    _data= f.read().split('\n')

data = []
for i in range(len(_data)):
    data.append(list(_data[i]))

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

def seat(_seatRow, _seatCol):
    '''
    return seat's future state
    '''
    if data[_seatRow][_seatCol] == 'L':
        adjacent_seats = adjacent(_seatRow, _seatCol)
        if adjacent_seats.count('#') == 0:
            return '#'
        else:
            return 'L'
    elif data[_seatRow][_seatCol] == '#':
        adjacent_seats = adjacent(_seatRow, _seatCol)
        if adjacent_seats.count('#') >=4 :
            return 'L'
        else:
            return '#'
    else:
        return data[_seatRow][_seatCol]

def adjacent(seat_row, seat_col):
    seats = []
    for y in range(max(seat_row - 1, 0), (min(seat_row + 1, len(data) - 1)) + 1):
          for x in range(max(seat_col - 1, 0), (min(seat_col + 1, len(data[0]) - 1)) + 1):
              if (x == seat_col and y == seat_row):
                  continue
              seats.append(data[y][x])
    return seats

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



