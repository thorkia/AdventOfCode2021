filename = '.\\Day10\\input.txt'
#filename = '.\\Day10\\testinput.txt'

with open(filename) as f:
    items = [item.strip() for item in f.readlines()]
    f.close()

pairs = { '(' : ')', '[' : ']', '{':'}','<':'>' }
points = { ')': 3, ']': 57, '}': 1197, '>': 25137}

#Part 1
illegalchars = [ ] 

for item in items:
    corrupt = False
    stack = [ ]
    for c in item:     
        if corrupt == True:
            continue

        if c in pairs.keys():
           stack.append(c)
        else: #closing brace remove item
            openbrace = stack.pop()
            if c != pairs[openbrace]:
                illegalchars.append(c)
                corrupt = True
        
print(illegalchars)
print(sum([points[i] for i in illegalchars]))

#Part 2
points2 = { ')': 1, ']': 2, '}': 3, '>': 4 }
incompleteScores = []

for item in items:
    corrupt = False
    stack = [ ]
    for c in item:     
        if corrupt == True:
            continue

        if c in pairs.keys():
           stack.append(c)
        else: #closing brace remove item
            openbrace = stack.pop()
            if c != pairs[openbrace]:                
                corrupt = True
    
    if corrupt == False:
        #do the calc for the item here
        score = 0
        while len(stack) > 0:
            score = (score * 5) + points2[pairs[stack.pop()]]
        
        incompleteScores.append(score)

incompleteScores.sort()
middle = int(len(incompleteScores)/2)
print(incompleteScores[middle])