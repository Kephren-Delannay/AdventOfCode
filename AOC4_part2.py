#%%
import numpy as np
import pandas as pd

#%%
further_checks = []
num_of_valids = 0
references_for_keys = [['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'],['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']]
    
# %%
def possesses_all_fields(_passport):
    """
    return if a passport is valid 
    to be valid : should contain 8 fields but cid is optional
    """
    keys = []
    for i in range(len(_passport)):
        key = _passport[i].split(":")[0]
        keys.append(key)
    keys.sort()
    if keys == references_for_keys[0] or keys == references_for_keys[1]:
        return True
    else : return False
# %%
with open(file="AOC_4_input.txt") as f:
    data = f.read().split("\n")

# %%
processeddata = []
final_data = []
cur = 0
for i in range(len(data)):
    if data[i] == "":
        processeddata.append(data[cur:i])
        cur = i
# %%
for el in processeddata:
    if el[0] =="":
        el.pop(0)
    a = ' '.join(el)
    secondprocess = a.split(" ")
    final_data.append((secondprocess))
# %%
for passport in final_data:
    if possesses_all_fields(passport):
        further_checks.append(passport)
# %%
#Trim data for Pandas Dataframe
for element in further_checks:
    element.sort()
    for f in element:
            if f [:3] == 'cid':
                element.remove(f)
    for i in range(len(element)):
        element[i] = element[i][4:]
# %%
#Create Panda DF
_data = np.array(further_checks)
df = pd.DataFrame(_data, columns=["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"])
dfn = df.astype({'byr' : int, 'ecl' : str, 'eyr' : int, 'hcl' : str, 'hgt' : str, 'iyr' : int, 'pid' : str})
# %%
validates = [True for x in range(256)]
vn = np.array(validates)
vn.reshape(256,1)
dfn['valid'] = vn
# %%
#Validate each fields
def validate(year, _min, _max):
    return year <= _max and year >= _min

def color(c):
    ref = "0123456789ABCDEF"
    c = c.upper()
    if len(c) != 7:
        return False
    else:
        for e in c[1:]:
            if e not in ref:
                return False
    return True 

# %%
a = 0
for index, row in dfn.iterrows():
    #validate year
    if not validate(row['byr'], 1920, 2002):
        dfn['valid'][index] = False
        print('F')
        a += 1
        continue
    else:
        #validate iyr
        if not validate(row['iyr'], 2010, 2020):
            dfn['valid'][index] = False
            print('F2')
            a += 1
            continue
        else:
            #validate eyr
            if not validate(row['eyr'], 2020, 2030):
                dfn['valid'][index] = False
                print('F3')
                a += 1
                continue
            else:
                #validate hcl
                if not color(row['hcl']):
                    dfn['valid'][index] = False
                    print('F5')
                    a += 1
                    continue
                else:
                    #validate ecl
                    if not row['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        dfn['valid'][index] = False
                        print('F6')
                        a += 1
                        continue
                    else:
                        #validate pid
                        if not len(row['pid']) == 9:
                            dfn['valid'][index] = False
                            print('F7')
                            a += 1
                            continue
                        else:
                            #validate hgt
                            if row['hgt'][-2:] == "cm":
                                if not validate(eval(row['hgt'][:-2]), 150, 193):
                                    dfn['valid'][index] = False
                                    print('F8')
                                    a += 1
                                    continue
                                
                            elif row['hgt'][-2:] == "in":
                                if not validate(eval(row['hgt'][:-2]), 59, 76):
                                    dfn['valid'][index] = False
                                    print('F8')
                                    a += 1
                                    continue
                            else:
                                dfn['valid'][index] = False
                                print('F8')
                                a += 1
                                continue
 

# %%
print(dfn[(dfn['valid'] == True)])
print(dfn.shape)
# %%
