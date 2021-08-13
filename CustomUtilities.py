def ReadFileBlanks(filename):
    """
    Reads a file that contains data separated by 
    blank spaces, returns data in a list
    """
    with open(file=filename) as f:
        data = f.read().split('\n')

    processeddata = []
    cur = 0
    for i in range(len(data)):
        if data[i] == "":
            processeddata.append(data[cur:i])
            cur = i
    return processeddata

def FlattenList(l):
    return [item for sublist in l for item in sublist]