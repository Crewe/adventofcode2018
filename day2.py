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

def findDifference(vals):
    row_count = len(vals)
    valid_id_length = len(vals[0]) - 1
    for i in range(row_count):
        for j in range(row_count):
            if i == j: continue
            # See how many characters differ by finding the intersect
            diff = len([value for value in vals[i] if value not in vals[j]])
            if diff == 1:
                char_list = []
                # Check that the position matches
                for x in range(len(vals[0])):
                    if vals[i][x] == vals[j][x]:
                        char_list.append(vals[i][x])
                output = ''.join(c for c in char_list)
                # Check it's the correct length
                if len(output) == valid_id_length:
                    return ''.join(c for c in char_list)
    return "Not found."

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

# Part 1
def partOne(data):
    res = sortArrayData(data)
    counts = countOccurrances(res)
    print("{} => {}".format(counts, counts[2] * counts[3]))

#Part 2
def partTwo(data):
    res = findDifference(data)
    print("The common string between the matching IDs is: {}".format(res))

data = getInput("input2.txt")
partOne(data)
partTwo(data)
