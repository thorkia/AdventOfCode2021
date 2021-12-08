filename = '.\\Day08\\input.txt'
#filename = '.\\Day08\\testinput.txt'

with open(filename) as f:
    items = [(item.split("|")[0], item.split("|")[1]) for item in f.readlines()]
    f.close()

#Part 1
uniqueSegmentLengths = [2, 3, 4, 7] # 1 takes 2 segments, 7 takes 3 segments, 4 takes 4 segments, 8 takes 7 segments
count = 0

for item in items:
    lengths = [len(l) for l in item[1].split() if len(l) in uniqueSegmentLengths]
    count += len(lengths)

print(count)


#Part 2
def subtractList(removeFrom : list, itemsToRemove : set):
    return [i for i in removeFrom if i not in itemsToRemove]

def getNumberDefs(items : list):
    numbers = { }
    #1, 7, 4, 8 are unique in the number of segments they use
    numbers[1] = [i for i in items if len(i) == 2][0]
    numbers[7] = [i for i in items if len(i) == 3][0]
    numbers[4] = [i for i in items if len(i) == 4][0]
    numbers[8] = [i for i in items if len(i) == 7][0]
    
    items = subtractList(items, set(numbers.values()))

    #Get 3: subtract 7 should be only item left with 2 letters    
    numbers[3] = [i for i in items if len(subtractList(list(i), set(numbers[7]))) == 2][0]
    items.remove(numbers[3])

    #Get 9 and 0: Contains all of 1
    firstSet = [ i for i in items if len(subtractList(list(numbers[1]), set(i))) == 0]
    #Get 9: Contains all of 4
    numbers[9] = [i for i in firstSet if len(subtractList(list(numbers[4]), set(i))) == 0][0]    
    items.remove(numbers[9])
    #Get 0: only item left
    firstSet.remove(numbers[9])
    numbers[0] = firstSet[0]
    items.remove(numbers[0])

    #Get 5 and 2: subtract 3 - only 9,5,2  possible.  We already know 9
    fiveorTwo = [i for i in items if len(subtractList(list(i), set(numbers[3]))) == 1]
    #From 5 or 2, if I subtract 4, 5 will have 2 letters left and 2 will have have 3
    five = [i for i in fiveorTwo if len(subtractList(list(i), set(numbers[4]))) == 2]
    two = [i for i in fiveorTwo if len(subtractList(list(i), set(numbers[4]))) == 3]
    numbers[5] = five[0]
    numbers[2] = two[0]
    items.remove(numbers[5])
    items.remove(numbers[2])

    #Only 6 remains
    numbers[6] = items[0]

    return numbers

def getValue(numbers: dict, text : str):
    if set(text) == set(numbers[0]):
        return '0'
    elif set(text) == set(numbers[1]):
        return '1'
    elif set(text) == set(numbers[2]):
        return '2'
    elif set(text) == set(numbers[3]):
        return '3'
    elif set(text) == set(numbers[4]):
        return '4'
    elif set(text) == set(numbers[5]):
        return '5'
    elif set(text) == set(numbers[6]):
        return '6'
    elif set(text) == set(numbers[7]):
        return '7'
    elif set(text) == set(numbers[8]):
        return '8'
    else:
        return '9'


sum = 0
for item in items:
    numberDefs = getNumberDefs(item[0].split())    

    number = ''
    for num in item[1].split():
        number += getValue(numberDefs, num)
    sum += int(number)

print(sum)