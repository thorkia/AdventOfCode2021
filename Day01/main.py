
filename = '.\\Day01\\input.txt'
#filename = '.\\Day01\\testinput.txt'

with open(filename) as f:
    lines = [int(item) for item in f.readlines()]
    f.close()

#part 1
increases = 0
for x in range(1,len(lines)):
    if lines[x] > lines[x-1]:
        increases+=1

print(increases)

#part 2
previoussum = 1000000 #set sum to number beyond possible max
part2increases = 0
for x in range(0,len(lines)-2): #range does not include the last index
    total = sum(lines[x:x+3]) #get total of next 3 numbers
    if total > previoussum:
        part2increases+=1
    previoussum = total

print(part2increases)