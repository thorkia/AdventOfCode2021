filename = '.\\Day05\\input.txt'
#filename = '.\\Day05\\testinput.txt'

with open(filename) as f:
    lines =  [(item.split("->")[0].strip(), item.split("->")[1].strip()) for item in f.readlines()]
    f.close()

def GetDelta(firstPoint: tuple, secondPoint: tuple):
    deltaX = 0
    deltaY = 0

    if firstPoint[0] > secondPoint[0]:
        deltaX = -1
    elif firstPoint[0] < secondPoint[0]:
        deltaX = 1

    if firstPoint[1] > secondPoint[1]:
        deltaY = -1
    elif firstPoint[1] < secondPoint[1]:
        deltaY = 1

    return (deltaX, deltaY)

def GetLineCoords(entry: tuple):
    firstCoord = (int(entry[0].split(",")[0]), int(entry[0].split(",")[1]) )
    secondCoord = (int(entry[1].split(",")[0]), int(entry[1].split(",")[1]) )

    delta = GetDelta(firstCoord, secondCoord)
    
    locs = [ entry[0] ]  

    #get all points in between
    while firstCoord[0] != secondCoord[0] or firstCoord[1] != secondCoord[1]:
        firstCoord = (firstCoord[0] + delta[0], firstCoord[1] + delta[1])
        locs.append( str(firstCoord[0]) + "," + str(firstCoord[1]))

    return locs; 

#Part 1

#We only consider straight lines
def IsStraightLine(entry : tuple):
    firstCoord = (int(entry[0].split(",")[0]), int(entry[0].split(",")[1]) )
    secondCoord = (int(entry[1].split(",")[0]), int(entry[1].split(",")[1]) )

    if firstCoord[0] == secondCoord[0] or firstCoord[1] == secondCoord[1]:
        return True
    
    return False

ventLocations = { }

for line in lines:
    if IsStraightLine(line) == False:
        continue

    locations = GetLineCoords(line)
    for location in locations:
        if location in ventLocations:
            ventLocations[location] = ventLocations[location]+1
        else:
            ventLocations[location] = 1

#Determine Number of Vents with a value > 2
numberOfMaXVents = len( list( filter(lambda val: val >= 2, ventLocations.values()) ) )

print(str(numberOfMaXVents))


#Part 2 - same as first but with no filter for Straight lines
ventLocations.clear()

for line in lines:
    locations = GetLineCoords(line)
    for location in locations:
        if location in ventLocations:
            ventLocations[location] = ventLocations[location]+1
        else:
            ventLocations[location] = 1

#Determine Number of Vents with a value > 2
numberOfMaXVents = len( list( filter(lambda val: val >= 2, ventLocations.values()) ) )

print(str(numberOfMaXVents))