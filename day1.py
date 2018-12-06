import io

def getInput(filename):
    value_array = []
    with open(filename) as f:
        for line in f:
            value_array.append(line.replace('\n',''))
    return value_array

def calculateFrequency(filename):
    result = 0
    freqs = getInput(filename)
    for val in freqs:
        result = result + int(val)
    return result

def calculateRecurringFrequency(filename):
    reccurrance_found = False
    tally = 0
    result = set()
    result.add(0)
    while not reccurrance_found:
        freqs = getInput(filename)
        for val in freqs:
            tally = tally + int(val)
            if tally in result:
                reccurrance_found = True
                return tally
            else:
                result.add(tally)

filename = "input1.txt"
output = "The frequency is {}, and first duplicate frequency is {}.".format(
    calculateFrequency(filename),
    calculateRecurringFrequency(filename))

print(output)
