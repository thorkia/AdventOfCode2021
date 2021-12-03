
filename = '.\\Day03\\input.txt'
#filename = '.\\Day03\\testinput.txt'

with open(filename) as f:
    lines = [item.strip() for item in f.readlines()]
    f.close()

#part 1 -> since we need to find the most and least common binary digit, we can just add all the ones.
#if the total is less than count*.5 0 is most common and 1 is least common
totals = [0] * len(lines[0])
for line in lines:
    for x in range(0, len(line)):
        totals[x] += int(line[x])

#convert to binary
mostCommon = ''
leastCommon = ''
mid = len(lines) / 2
for item in totals:
    if item > mid:
        mostCommon += '1'
        leastCommon += '0'
    else:
        mostCommon += '0'
        leastCommon += '1'

#convert binary to int and multiply
power = int(mostCommon,2) * int(leastCommon,2)
print(str(power))

#part 2
def getFilteredSet(items, isMostCommon):
    index = 0

    while index < len(lines[0]) and len(items) > 1:  
        total = 0

        for item in items:
            total += int(item[index])
        
        filterbit = ''
        if total >= (len(items)/2):
            if isMostCommon:
                filterbit = '1'
            else:
                filterbit = '0'
        elif total < (len(items)/2):
            if isMostCommon:
                filterbit = '0'
            else:
                filterbit = '1'        

        items = list(filter(lambda item: item[index] == filterbit, items))
        index += 1

    return items[0]

oxygen = getFilteredSet(lines, True)
co2 = getFilteredSet(lines, False)

lifesupport = int(oxygen,2) * int(co2,2)
print(str(lifesupport))