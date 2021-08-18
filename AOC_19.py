with open(file="AOC_19_input_rules.txt") as f:
    rules = f.read().split('\n')
with open(file="AOC_19_input_data.txt") as f:
    data = f.read().split('\n')

def get_rules_order():
    '''
    returns the order to process the rules
    '''
    pass

def create_rules_dict():
    rules_dict = {}
    for el in rules:
        splited = el.split(':')
        index = splited[0]
        val = splited[1]#list(splited[1].replace(' ', ''))
        rules_dict[index] = val
    return rules_dict

r = create_rules_dict()

for k , i in r.items():
    if k != '0':
        for el in r[k]:
            if el == " " or el == "|":
                continue
            if el in r.keys():
                #print('replacing ', el, ' with ', r[el])
                r[k] = r[k].replace(el, r[el])
                #print(r[k])
        #print(k, i)
print(r)


for k , i in r.items():
    if k != '0':
        for el in r[k]:
            if el == " " or el == "|":
                continue
            if el in r.keys():
                #print('replacing ', el, ' with ', r[el])
                r[k] = r[k].replace(el, r[el])
                #print(r[k])
        #print(k, i)
print(r['1'])