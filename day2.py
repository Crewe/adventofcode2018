import io

def getInput(filename):
    value_array = []
    with open(filename) as f:
        for line in f:
            value_array.append(line.replace('\n',''))
    return value_array

def sortArrayData(vals):
    sorted_array = []
    for item in vals:
        sorted_array.append(sorted(item))
    return sorted_array

def countOccurrances(vals):
    occurred = {2: 0, 3: 0}
    cols = len(vals[0])
    for row in vals:
        count = 1
        matches = {2: False, 3: False}
        # skip all characters differ
        if len(set(row)) == cols: continue
        
        for i in range(cols, 1, -1):
            if row[i - 1] == row[i - 2]:
                count += 1
                # If at the last two positions 
                if i <= 2:
                    if count == 2 and not matches[2]:
                        occurred[2] += 1
                        matches[2] = True
                    if count == 3 and not matches[3]:
                        occurred[3] += 1
                        matches[3] = True
            else:
                if count == 2 and not matches[2]:
                    occurred[2] += 1
                    matches[2] = True
                if count == 3 and not matches[3]:
                    occurred[3] += 1
                    matches[3] = True
                count = 1

    return occurred

res = sortArrayData(getInput("input2.txt"))
res = countOccurrances(res)
print("{} => {}".format(res, res[2] * res[3]))
