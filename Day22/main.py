from collections import defaultdict

#filename = '.\\Day22\\testinput.txt'
filename = '.\\Day22\\input.txt'

items = [ ]
with open(filename) as f:
    items = [item.strip() for item in f.readlines()]
    f.close()

grid = defaultdict(int)

def getOperations(unparsed : str):

    instructions = { }
    splitparsed = unparsed.split(',')
    
    for item in splitparsed:
        axis = item[0]
        #use 2 so we also ignore the equals
        ranges = item[2:].split('..')
        instructions[axis] = (int(ranges[0]) , int(ranges[1]))

    return instructions

def isValidInstruction(instructions : dict):
    #any completely under or over the amount:
    for instruction in instructions.values():
        if instruction[1] < -50:
            return False
        if instruction[0] > 50:
            return False

    return True

def shrinkValidInstruction(instuctions : dict):
    for key in instuctions:
        min = instuctions[key][0]
        max = instuctions[key][1]
        if min < -50:
            min = -50
        if max > 50:
            max = 50
        instuctions[key] = (min, max)
    return

#Part 1
#Parse instructions
enginegrid = defaultdict(int)

filterSet = set()
filterSet = filterSet.union( [ ",".join([str(x),str(y),str(z)]) for x in range(-50, 51) for y in range(-50, 51) for z in range(-50, 51)] )

for item in items:
    onoff = 1
    if item.split(' ')[0] == 'off':
        onoff = 0
    operations = getOperations(item.split(' ')[1])

    if not isValidInstruction(operations):
        continue
    
    #TODO: make it valid - IE set the min and max
    shrinkValidInstruction(operations)

    cells = [ ",".join([str(x),str(y),str(z)]) for x in range(operations["x"][0], operations["x"][1]+1)
        for y in range(operations["y"][0], operations["y"][1]+1) for z in range(operations["z"][0], operations["z"][1]+1)]
    
    for cell in cells:
        enginegrid[cell] = onoff

print(sum(enginegrid.values()))

