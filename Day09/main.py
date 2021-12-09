filename = '.\\Day09\\input.txt'
#filename = '.\\Day09\\testinput.txt'

with open(filename) as f:
    items = [item.strip() for item in f.readlines()]
    f.close()

def getAdjacentCoords(x, y, maxX, maxY):
    coords = [ ]

    if x >= 1:
        coords.append( (x-1, y) )
    if x+1 < maxX:
        coords.append( (x+1, y) )
    if y >= 1:
        coords.append( (x, y-1) )
    if y+1 < maxY:
        coords.append( (x, y+1) )

    return coords

#Part 1

maxY = len(items)
maxX = len(items[0])

lowPointVals = [ ]
lowPointCoords = [ ]
for y in range(maxY):
    for x in range(maxX):
        posVal = int(items[y][x])
        if posVal == 9: #If it is 9, it will not be lower than adjacent
            continue

        coords = getAdjacentCoords(x,y, maxX, maxY)        
        if len( [item for item in coords if int(items[item[1]][item[0]]) < posVal] ) == 0:
            lowPointVals.append( (posVal+1))
            lowPointCoords.append( (x,y) )

print(sum(lowPointVals))

#Part 2 - get Basins
def getBasin(coord):
    adjacent = getAdjacentCoords(coord[0], coord[1], maxX, maxY)

    basinCoords = [ ]
    basinCoords.append(coord)

    for item in adjacent:        
        #9 is never part of a basin, and each adjacent item must larger       
        if int(items[coord[1]][coord[0]]) < int(items[item[1]][item[0]]) and int(items[item[1]][item[0]]) != 9: 
            newBasin = getBasin(item)
            basinCoords.extend(newBasin)

    return set(basinCoords)


basinSizes = [ ]

for lowpoint in lowPointCoords:
    basin = getBasin(lowpoint)    
    basinSizes.append(len(basin))    

basinSizes.sort()
prod = 1
for size in basinSizes[-3:]:
    prod*=size

print(basinSizes[-3:])
print(prod)

