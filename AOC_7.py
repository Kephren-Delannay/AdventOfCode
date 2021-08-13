#%%
example_input = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags'''

# %%
#data = example_input.split(".")
with open(file="AOC_7_input.txt") as f:
    data = f.read().split(".")
# %%
def process_color(sentence : str):
    a = sentence.split("bag")[0]
    if a.endswith(" "):
        a =  a[:-1]
    if a.startswith("\n"):
        a = a[1:]
    return a

# %%
def process_suffix(sentence : str):
    if sentence[:2] == "no":
        return "None"
    else:
        result = []
        bags = sentence.split(',')
        for b in bags:
            result.append(process_color(b))
        result[0] = result[0][2:]
        for i in range(1, len(result)):
            result[i] = result[i][3:]
        return result
# %%
d = {}
for i in range(len(data)):
    s = data[i].split(" contain ")
    prefix = process_color(s[0])
    suffix = s[-1]
    suffix = (process_suffix(suffix))
    d[prefix] = suffix

print(d)

# %%
allbags = []
finals = []
#first layer check 
results = []
for k, v in d.items():
    if ('shiny gold') in v:
        results.append(k)
# %%
allbags = results.copy()
while len(allbags) > 0:
    
    for bag in allbags:
        results = []
        for k, v in d.items():
            if (bag) in v:
                results.append(k)
        allbags += results
        allbags.remove(bag)
        finals.append(bag)
# %%
f = set(finals)
print(f)
# %%
print(len(f))
# %%
