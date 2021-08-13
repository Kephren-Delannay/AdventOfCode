sequence = [0, 3, 6] #starting numbers
ranks_last_spoken = {0 : 1, 3 : 2, 6 : 3}
rank = 3

def get_next(current):
    if sequence.count(current) > 1:
        diff = (rank-1) - ranks_last_spoken.get(current)
        ranks_last_spoken[current] = rank-1
        return diff    
    else:
        ranks_last_spoken[current] = rank
        return 0

def next_turn():
    n = get_next(sequence[-1])
    sequence.append(n)

while rank < 10:
    rank += 1
    next_turn()
    print(rank)
    print(sequence)
    print('--------------')