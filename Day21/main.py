from collections import defaultdict

#filename = '.\\Day21\\testinput.txt'
filename = '.\\Day21\\input.txt'

items = [ ]
with open(filename) as f:
    items = [item.strip() for item in f.readlines()]
    f.close()

playersPosition = defaultdict(int)
playersScore  = defaultdict(int)

for item in items:
    pos = int(item.split(':')[1].strip())
    player = item.split("starting")[0].strip()
    playersPosition[player] = pos
    playersScore[player] = 0

#Part 1
targetScore = 1000
roll = 0

while max(playersScore.values()) < 1000:
    for player in playersPosition.keys():
        moveAmount = 0
        for i in range(3):
            roll+=1
            if roll % 100 == 0:
                moveAmount += 100
            else:    
                moveAmount += (roll % 100)
        
        playersPosition[player] = (playersPosition[player] + moveAmount) % 10
        if playersPosition[player] == 0:
            playersScore[player]+=10
        else:
            playersScore[player]+=playersPosition[player]

        if playersScore[player] >= 1000:
            break

print( min(playersScore.values()) )
print( roll )
print( (roll*min(playersScore.values())) )

#Part 2

def calcRound( positions: dict, scores: dict, roll: int, PlayerOneturn: bool, player: int):
    winsForPlayer = 0

    #add the roles to the players turn
    if PlayerOneturn == True:
        positions[1] = (positions[1] + roll) % 10
        if positions[1] == 0: 
            positions[1] = 10
        scores[1] += positions[1]
    else:    
        positions[2] = (positions[2] + roll) % 10
        if positions[2] == 0: 
            positions[2] = 10
        scores[2] += positions[2]
    
    #change the players turns:
    PlayerOneturn = (not PlayerOneturn)

    #check if anyone won    
    if (max(scores.values()) >=21 ):
            #if the player we are counting won - return 1, or else return 0
            if scores[player] >= 21:
                return 1
            else:
                 return 0
    else: #count the wins for all the next possible rolls
        #multiply them by the number of ways to make that roll - the order doesn't matter when totally just the number of ways to make 
        winsForPlayer += calcRound(positions, scores, 9, PlayerOneturn, player) 
        winsForPlayer += (calcRound(positions, scores, 8, PlayerOneturn, player) * 3) #there are 3 ways to make an 8
        winsForPlayer += (calcRound(positions, scores, 7, PlayerOneturn, player) * 6) #6 ways to make 7
        winsForPlayer += (calcRound(positions, scores, 6, PlayerOneturn, player) * 7) #7 ways to make a 6
        winsForPlayer += (calcRound(positions, scores, 5, PlayerOneturn, player) * 6) #6 ways to make a 5
        winsForPlayer += (calcRound(positions, scores, 4, PlayerOneturn, player) * 3) #3 ways to make a 4
        winsForPlayer += calcRound(positions, scores, 3, PlayerOneturn, player) #check if a 3 is rolled


    return winsForPlayer

#Hard code the values - no need for dictionary as there are only 2 players
player1_wins = 0
player2_wins = 0
player1_start = 10
player2_start = 9
states = defaultdict(int)
states[(player1_start - 1, player2_start - 1, 0, 0)] = 1
die_rolls = [sum((x, y, z)) for z in (1, 2, 3) for y in (1, 2, 3) for x in (1, 2, 3)]
while len(states) > 0:
    # player 1
    new_states = defaultdict(int)
    for state, count in states.items():
        for n in die_rolls:
            new_pos = (state[0] + n) % 10
            new_score = state[2] + new_pos + 1
            if new_score >= 21:
                player1_wins += count
            else:
                new_states[(new_pos, state[1], new_score, state[3])] += count
    states = new_states

    # player 2
    new_states = defaultdict(int)
    for state, count in states.items():
        for n in die_rolls:
            new_pos = (state[1] + n) % 10
            new_score = state[3] + new_pos + 1
            if new_score >= 21:
                player2_wins += count
            else:
                new_states[(state[0], new_pos, state[2], new_score)] += count
    states = new_states

print(f"Part 2: {max(player1_wins,player2_wins)}; {player1_wins=}, {player2_wins=}")