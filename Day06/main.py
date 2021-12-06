filename = '.\\Day06\\input.txt'
#filename = '.\\Day06\\testinput.txt'

with open(filename) as f:
    items = [int(item) for item in f.readline().strip().split(",")]    
    f.close()

dayDict = dict.fromkeys(range(0,9),0)

for item in items:
    dayDict[item] += 1

print(dayDict)

#Part 1 -> count 80 days
for day in range(1,81):
    day0 = dayDict[0]
    for i in range(1,9):
        dayDict[i-1] = dayDict[i]
    
    #add day 0 to day 6 and set day day 8 to day 6
    dayDict[6] += day0
    dayDict[8] = day0
    #print(dayDict)

print(str(sum(dayDict.values())))

#part 2 -> 256 days
for day in range(81,257):
    day0 = dayDict[0]
    for i in range(1,9):
        dayDict[i-1] = dayDict[i]
    
    #add day 0 to day 6 and set day day 8 to day 6
    dayDict[6] += day0
    dayDict[8] = day0
    #print(dayDict)

print(str(sum(dayDict.values())))