with open(file="AOC_4_input.txt") as f:
    data = f.read().split("\n")

processeddata = []
final_data = []
cur = 0
for i in range(len(data)):
    if data[i] == "":
        processeddata.append(data[cur:i])
        cur = i

for el in processeddata:
    if el[0] =="":
        el.pop(0)
    a = ' '.join(el)
    secondprocess = a.split(" ")
    final_data.append((secondprocess))

def check1():
    num_of_valids = 0
    references = [['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'],['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']]
    def isvalid(_passport):
        """
        return if a passport is valid 
        to be valid : should contain 8 fields but cid is optional
        """
        keys = []
        for i in range(len(_passport)):
            key = _passport[i].split(":")[0]
            keys.append(key)
        keys.sort()
        if keys == references[0] or keys == references[1]:
            return True
        else : return False

    for passport in final_data:
        if isvalid(passport):
            num_of_valids += 1
    
    return num_of_valids

#print(check1())

import numpy as np
import pandas as pd


def check2():
    further_checks = []
    num_of_valids = 0
    references_for_keys = [['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'],['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']]
    
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

    for passport in final_data:
        if possesses_all_fields(passport):
            further_checks.append(passport)
    
    #trim down dataset to create pandas dataframe
    
    for element in further_checks:
        element.sort()
        for f in element:
            if f [:3] == 'cid':
                element.remove(f)
    
    datachecks = further_checks.copy()        
    for passport in datachecks:
        for i in range(len(passport)):
            passport[i]  =passport[i][4:]

    _data = np.array(datachecks)
    test = pd.DataFrame(_data, columns=["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"])
    print(test)
check2()