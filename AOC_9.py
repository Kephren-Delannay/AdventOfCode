with open(file="AOC_9_input.txt") as f:
    data = f.read().split('\n')


startindex = 0
preamblelength = 25
preamble = data[startindex:startindex+preamblelength]
#print(preamble)

'''test_data=['35',
'20',
'15',
'25',
'47',
'40',
'62',
'55',
'65',
'95',
'102',
'117',
'150',
'182',
'127',
'219',
'299',
'277',
'309',
'576']'''
#preamble = ['35', '20', '15', '25', '47']


def get_all_sums(l : list):
    sums = []
    for el in l:
        for i in range(len(l)):
            if el != l[i]:
                sums.append(eval(el) + eval(l[i]))
    return sums 


def check_valid(preamble, next_n):
    sums = get_all_sums(preamble)
    return int(next_n) in sums

starting_n = 30
n = starting_n
#print(check_valid(preamble, 40))

while check_valid(preamble, n):
   startindex += 1
   end_index = startindex + preamblelength
   #print(startindex, end_index)
   preamble = data[startindex : end_index]
   #print(preamble)
   n = data[end_index] 
print(n)

#print(check_valid(preamble, '55'))
