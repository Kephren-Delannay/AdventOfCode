test_input = [
"#0 nop +0",
"#1 acc +1",
"#2 jmp +4",
"#3 acc +3",
"#4 jmp -3",
"#5 acc -99",
"#6 acc +1",
"#7 jmp -4",
"#8 acc +6"]

commands = []
with open(file="test.txt") as f:
    data = f.readlines()
    

current = 0
acc = 0

def get_command_id(command:str):
    command = command.split(" ")
    return command[0]

def execute(command:str):
    global current, acc
    n_index = 0
    command = command.split(" ")
    print(command)
    
    if command[1] == "acc":
        acc += eval(command[2])
        n_index = "+1"
    elif command[1] == "jmp":
        n_index = command[2]
    else:
        n_index = "+1"

    current = (current + eval(n_index))
    
ids = []    
while True:
    _id = get_command_id(data[current])
    if _id in ids:
        break
    else:
        ids.append(_id)
        execute(data[current])

print(ids)    
print("acc : ", acc)
print("current:", current)

"""
print(commands)
for i in commands:
    f = open("test.txt", "a")
    f.write(i)
    f.close()"""
