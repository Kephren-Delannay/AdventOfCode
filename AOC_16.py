#%%%
ranges = {
    'dp_loc' : (range(47, 875), range(885, 961)),
    'dp_stn' : (range(25, 617), range(662, 965)),
    'dp_plt' : (range(42, 808), range(825, 967)),
    'dp_trc' : (range(36, 561), range(583, 966)),
    'dp_dte' : (range(37, 265), range(289, 969)),
    'dp_tme' : (range(27, 326), range(346, 955)),
    'ar_loc' : (range(37, 385), range(391, 951)),
    'ar_stn' : (range(35, 234), range(244, 964)),
    'ar_plt' : (range(26, 653), range(675, 950)),
    'ar_trc' : (range(41, 690), range(710, 955)),
    'class' : (range(27, 76), range(81, 953)),
    'duration' : (range(45, 785), range(807, 968)),
    'price' : (range(40, 351), range(374, 971)),
    'route' : (range(30, 893), range(904, 969)),
    'row' : (range(47, 145), range(151, 958)),
    'seat' : (range(28, 751), range(773, 974)),
    'train' : (range(30, 457), range(475, 951)),
    'type' : (range(34, 643), range(648, 969)),
    'wagon' : (range(42, 487), range(498, 971)),
    'zone' : (range(37, 153), range(167, 974))
}

# %%
def check_validity(tic):
    for key, value in ranges.items():
        for r in value:
            if tic in r:
                return True
            else:
                continue
    return False

# %%
def check_invalid_field_in_ticket(ticket):
    for field in ticket:
        if check_validity(field) == False:
            return field
        else:
            continue
    return 0

# %%
def create_tickets():
    with open(file='AOC_16_input.txt') as f:
        data = f.read().split('\n')
    return data
        
# %%
_tickets = create_tickets()
_tickets_ = [t.split(',') for t in _tickets]
tickets = [[eval(x) for x in t] for t in _tickets_]


# %%
s = []
for ticket in tickets:
    n = check_invalid_field_in_ticket(ticket)
    s.append(n)
print(s)
# %%
