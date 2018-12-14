import io

def getInput(filename):
    value_array = []
    with open(filename) as f:
        for line in f:
            value_array.append(line.replace('\n',''))
    return value_array

def sortLog(filename):
    log = getInput(filename)
    return "Sorted log"


log = sortLog("test.txt")
print(log)
