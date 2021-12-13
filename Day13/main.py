filename = '.\\Day12\\input.txt'
#filename = '.\\Day12\\testinput.txt'

with open(filename) as f:
    items = [item.strip() for item in f.readlines()]
    f.close()

grid =  [ ]
instructions = [ ]

instructionStart = items.index("")
for i in range(instructionStart):
    coord = items[i].split(",")
    grid.append( ( int(coord[0]), int(coord[1])) )

for i in range(instructionStart+1, len(items)):
    instruction = items[i].split("=")
    instructions.append( (instruction[0][-1], int(instruction[1])) )

for instruction in instructions:
    #Assume fold on x axis and adjust if y axis
    foldDirection = 0    
    if (instruction[0]) == 'y':
        foldDirection = 1        
    
    newGrid = set()
    for coord in grid:
        if coord[foldDirection] <= instruction[1]:
            newGrid.add(coord)
            continue
        #items move the same distance from the fold direction.  If fold in half, an item that is 2cm below the line becomes 2 cm above
        #so we use the fold line to do the math
        moveAmount = coord[foldDirection] - instruction[1]
        if foldDirection == 0:
            newGrid.add( (instruction[1]-moveAmount, coord[1]) )
        else: 
            newGrid.add( (coord[0], instruction[1]-moveAmount) )
    
    grid = list(newGrid)
    print(len(grid))

print(len(grid))

#Part 2 - Display the grid
#get the max x and max y
maxX = max([x[0] for x in grid])
maxY = max([y[1] for y in grid])

setGrid = set(grid)

for y in range(maxY+1):
    display = ""
    for x in range(maxX+1):
        if (x,y) in setGrid:
            display+="*"
        else:
            display+="."
    print(display)

