filename = '.\\Day11\\input.txt'
#filename = '.\\Day11\\testinput.txt'

with open(filename) as f:
    items = [item.strip() for item in f.readlines()]
    f.close()

maxX = len(items[0])
maxY = len(items)

def GetNeighbours(x: int, y: int):
    coords = set()

    if x >= 1:
        coords.add( (x-1, y) )
        if y >= 1:
            coords.add( (x-1, y-1) )
        if y+1 < maxY:
            coords.add( (x-1, y+1) )
    
    if x+1 < maxX:
        coords.add( (x+1, y) )
        if y >= 1:
            coords.add( (x+1, y-1) )
        if y+1 < maxY:
            coords.add( (x+1, y+1) )
    
    if y >= 1:
        coords.add( (x, y-1) )
    if y+1 < maxY:
        coords.add( (x, y+1) )
    
    return coords

# Part 1
locationEnergy = dict()

#Build current energy maps
for x in range(maxX):
    for y in range(maxY): 
        energy = int(items[y][x])        
        locationEnergy[(x,y)] = energy

flashCount = 0
for step in range(100):
    #increment everything by 1:
    for k in locationEnergy.keys():
        locationEnergy[k]+=1    
    #get the >9s
    nines = [key for key in locationEnergy if locationEnergy[key] > 9]
    while len(nines) > 0: 
        for nine in nines:
            flashCount+=1
            locationEnergy[nine] = 0
            #Get and increment all neighbours by 1
            neighbours = GetNeighbours(nine[0], nine[1])
            for neighbour in neighbours:
                if locationEnergy[neighbour] != 0:
                    locationEnergy[neighbour]+=1
        #Get the new set of nines - can be greater than 9 if 2 neighbours flashed
        nines = [key for key in locationEnergy if locationEnergy[key] > 9]

print(flashCount)

#Part 2 - all flash at the same time
locationEnergy = dict()

#Build current energy maps
for x in range(maxX):
    for y in range(maxY): 
        energy = int(items[y][x])        
        locationEnergy[(x,y)] = energy

synch = False
step = 0
while synch == False:
    step+=1

    flashCount = 0
    #increment everything by 1:
    for k in locationEnergy.keys():
        locationEnergy[k]+=1    
    #get the >9s
    nines = [key for key in locationEnergy if locationEnergy[key] > 9]
    while len(nines) > 0: 
        for nine in nines:
            flashCount+=1
            locationEnergy[nine] = 0
            #Get and increment all neighbours by 1
            neighbours = GetNeighbours(nine[0], nine[1])
            for neighbour in neighbours:
                if locationEnergy[neighbour] != 0:
                    locationEnergy[neighbour]+=1
        #Get the new set of nines - can be greater than 9 if 2 neighbours flashed
        nines = [key for key in locationEnergy if locationEnergy[key] > 9]
    
    if flashCount == 100:
        synch = True

print(step)