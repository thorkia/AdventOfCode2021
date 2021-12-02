
filename = '.\\Day02\\input.txt'
#filename = '.\\Day02\\testinput.txt'

with open(filename) as f:
    lines = [(item.split()[0],int(item.split()[1])) for item in f.readlines()]
    f.close()

#part 1
depth = 0
distance = 0
for dir,amt in lines:
    if dir=="forward":
        distance+=amt
    elif dir=="up":
        depth-=amt #going up when underwater decreases your depth
    elif dir=="down":
        depth+=amt #going down when underwater increases your depth

print("depth: " + str(depth) + " distance: " + str(distance) + " product:" + str(distance*depth))

#part 2
depth = 0
distance = 0
aim = 0

for dir,amt in lines:
    if dir=="forward":
        distance+=amt
        depth+= (aim*amt)
    elif dir=="up":
        aim-=amt #going up when underwater decreases your depth
    elif dir=="down":
        aim+=amt #going down when underwater increases your depth

print("depth: " + str(depth) + " distance: " + str(distance) + " product:" + str(distance*depth))