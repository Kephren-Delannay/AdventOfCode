with open(file='AOC_14_input.txt') as f:
    _data = f.read().split('\n')
print(_data)

mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
memory_bits = {}

def data2bin(d):
    global mask
    value = bin(d)[2:]
    missing = len(mask) - len(value)
    v = ['0' for x in range(missing)]
    added = ''.join(v)
    return added + value
    
def masked_value(d):
    global mask
    returned = []
    _d = list(d)
    _m = list(mask)
    for i in range(len(_d)):
        if _m[i] == 'X':
            returned.append(str(_d[i]))
        else:
            returned.append(str(_m[i]))
    return ''.join(returned)

def bin2dec(d):
    value ='0b' + d
    return eval(value)

def write_in_memory(memory, d):
    global memory_bits
    value = data2bin(d)
    memory_bits[memory] = masked_value(value)

def instruction(line):
    global mask
    instr = line.split(' = ')
    if instr[0] == 'mask':
        mask = instr[1]
    else:
        allocated_memory = instr[0]
        write_in_memory(allocated_memory, eval(instr[1]))

for line in _data:
    instruction(line)

bin_values = memory_bits.values()
values = []
for v in bin_values:
    values.append(bin2dec(v))

print(memory_bits)
print(sum(values))
