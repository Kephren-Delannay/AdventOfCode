#%%
import CustomUtilities as util
data = util.ReadFileBlanks("AOC_6_input.txt")
for i in range(len(data)):
    el = data[i]
    if el[0] == "":
        el.pop(0)
# %%
def check(_answers):
    return len(set(util.FlattenList(_answers)))


# %%
answ = []
for i in range(len(data)):
    tot = check(data[i])
    answ.append(tot)

print(sum(answ))

# %%
def check2(_answers):
    _answers.sort(key=len)
    reference = _answers[0] #get the first as a ref
    goal = len(_answers)
    _ans = util.FlattenList(_answers)
    n = 0
    for i in reference:
        if _ans.count(i) == goal:
            n += 1
    return n

# %%
ans = []
for i in range(len(data)):
    tot = check2(data[i])
    ans.append(tot)

print(sum(ans))
# %%
