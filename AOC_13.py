def generate_schedule(ID):
    departs = []
    departs.append(ID)
    x = ID
    while x < arrival_time + ID:
        x = departs[-1] + ID
        departs.append(x)

    return departs

def get_IDs(l):
    Ids = [eval(x) for x in l if x != 'x']
    return Ids

with open(file='AOC_13_input.txt') as f:
    data = f.readlines()

arrival_time = eval(data[0].split('\n')[0])
IDs = get_IDs(data[1].split(','))

schedules = {}
new_dict = {}

for ID in IDs:
    _sch = generate_schedule(ID)
    sch = [x for x in _sch if x >= arrival_time]
    schedules[ID] = sch[0]
    for key, value in schedules.items():
        new_dict[value] = key

departs = schedules.values()
minimum_departure = min(departs)
print(minimum_departure)
ID_mimimum = new_dict[minimum_departure]
print(ID_mimimum)
span = minimum_departure - arrival_time
print(ID_mimimum * span)