from collections import defaultdict

#filename = '.\\Day14\\testinput.txt'
filename = '.\\Day14\\input.txt'

with open(filename) as f:
    items = [item.strip() for item in f.readlines()]
    f.close()

instructions = { }

splitInstructions = [item.split(" -> ") for item in items[2:]]
for si in splitInstructions:
    instructions[si[0].strip()] = si[1].strip()

#Part 1
def do_Range_Inserts(startChain: list, insertCount: int, letterCount: dict):
    modifiedChain = startChain

    for step in range(0,insertCount):
        newChain = [ ]
        childChainLength = len(modifiedChain)
        for childPair in range(childChainLength):
            newChain.append(modifiedChain[childPair])
            key = ''.join(modifiedChain[childPair:childPair+2])        
            if key in instructions.keys():            
                newChain.append(instructions[key])
        
        modifiedChain = newChain
    
    for letter in newChain[:-1]:
            letterCount[letter]+=1
    
    return modifiedChain


letterCount = defaultdict(int)
chain = list(items[0].strip())

chain = do_Range_Inserts(chain, 10, letterCount) #get the most recent chain.
letterCount[chain[-1]]+=1

maxCount = max(letterCount.values())
minCount = min(letterCount.values())

print(maxCount-minCount)



#Part 2 - need 40 steps.  So need to add 30 steps
letterCount = defaultdict(int)
pairCounts = defaultdict(int)

initialValue = items[0].strip()
#get initial pairs
for i in range(len(initialValue)):
    letterCount[initialValue[i]]+=1
    pair = initialValue[i:i+2]
    if len(pair) == 2:
        pairCounts[pair]+=1
    
for i in range(40):
    newCounts = defaultdict(int)
    for countKey, countAmount in pairCounts.items():
        if countKey in instructions:
            newKey = countKey[0] + instructions[countKey]
            newSecondKey = instructions[countKey] + countKey[1]

            newCounts[newKey] += countAmount
            newCounts[newSecondKey] += countAmount

            letterCount[instructions[countKey]] += countAmount
        else:
            newCounts[countKey] = countAmount
    
    pairCounts = newCounts

maxCount = max(letterCount.values())
minCount = min(letterCount.values())

print(maxCount-minCount)