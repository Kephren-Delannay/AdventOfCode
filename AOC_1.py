"""with open("AOC_1_input.txt") as f:
    data = f.readlines()
    output = [eval(x) for x in data]

sorted_output = output.copy()
sorted_output.sort()
reversed_output = output.copy()
reversed_output.sort(reverse=True)


for i in range(0, len(reversed_output)):
    s = reversed_output[i]
    j = 0
    while s < 2020:
        s = reversed_output[i] + sorted_output[j]
        j += 1
    if s == 2020:
        print(reversed_output[i])
        print(sorted_output[j-1])
        print(reversed_output[i] * sorted_output[j-1])
        break"""

with open("AOC_1_input.txt") as f:
    data = f.readlines()
    output = [eval(x) for x in data]

sorted_output = output.copy()
sorted_output.sort()
reversed_output = output.copy()
reversed_output.sort(reverse=True)
third_output = sorted_output.copy()

found = False

for i in range(len(sorted_output)):
    begining = sorted_output[i]
    threshold = 2020 - begining
    toadd = [x for x in sorted_output if x < threshold and x != begining]
    tryadd = [x + begining for x in toadd]
    #after first addition
    for adding in tryadd:
        if found == True:
            break
        new_threshold = 2020 - adding
        potentials = [x for x in sorted_output if x < threshold and x != begining and x != adding]
        for j in range(len(potentials)):
            maxsum = adding + potentials[j]
            if maxsum > 2020:
                break
            if maxsum == 2020:
                print(begining)
                print(adding - begining)
                print(potentials[j])
                print("-----------------")
                print(begining * (adding - begining) * potentials[j])
                found = True
                break
    
    
     

    

            

