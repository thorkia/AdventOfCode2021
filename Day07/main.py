import sys

filename = '.\\Day07\\input.txt'
#filename = '.\\Day07\\testinput.txt'

with open(filename) as f:
    line = f.readline().strip()
    f.close()

positions = [int(item) for item in line.split(",")]
minLoc = min(positions)
maxLoc = max(positions)

#Part 1 - sum of total distance away from target
fuel = sys.maxsize
optimalPos = -1

for i in range(minLoc, maxLoc+1):
    #calculate fuel needed
    fuelNeeded = sum([abs(p-i) for p in positions])
    if fuelNeeded < fuel:
        fuel = fuelNeeded
        optimalPos = i

print(fuel)
print(optimalPos)

#Part 2 - fuel needed is the sum of the steps needed.
def sumTotal(n : int): 
    if n % 2 == 0:
        return int((n/2)*(n+1))
    else:
        return int(((n+1)/2) * n)
    
fuel = sys.maxsize
optimalPos = -1

for i in range(minLoc, maxLoc+1):
    #calculate fuel needed
    fuelNeeded = sum([sumTotal(t) for t in [abs(p-i) for p in positions]])
    if fuelNeeded < fuel:
        fuel = fuelNeeded
        optimalPos = i

print(fuel)
print(optimalPos)