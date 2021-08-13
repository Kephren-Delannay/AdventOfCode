#%%
def decode_row(_input):
    """
    return row number from the whole set of characters
    """
    _data = _input[:-3]
    seat_range = range(0, 128)
    for element in _data:
        if element == 'F':
            new_end = int(len(seat_range) / 2)
            seat_range = range(seat_range.start, seat_range.start + new_end)
        else:
            new_start = int(len(seat_range) / 2)
            seat_range = range(seat_range.start + new_start, seat_range.stop)

    return seat_range[-1]

def decode_column(_input):
    """
    return column number from the whole set of characters
    """
    _data = _input[-3:]
    col_range = range(0,8)
    for element in _data:
        if element == 'L':
            new_end = int(len(col_range) / 2)
            col_range = range(col_range.start, col_range.start + new_end)
            
        else:
            new_start = int(len(col_range) / 2)
            col_range = range(col_range.start + new_start, col_range.stop)
            

    return col_range[-1]

# %%
with open(file="AOC_5_input.txt") as f:
    dump_data = f.readlines()
for i in range(len(dump_data)):
    dump_data[i] = dump_data[i].split('\n')[0]

# %%
_ids = []
for boardingpass in dump_data:
    col = decode_column(boardingpass)
    row = decode_row(boardingpass)
    _id = row * 8 + col
    _ids.append(_id)
# %%
_ids.sort()
print(_ids[-1])
# %%
test = range(0, 855)
# %%
testing = []
for e in test:
    if e not in _ids:
        testing.append(e) #! ANSWER was 552 (last in the list every other was at the very begining)
