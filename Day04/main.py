filename = '.\\Day04\\input.txt'
#filename = '.\\Day04\\testinput.txt'

class Board:    
    def __init__(self, rows):
        self.items : list[list[int]] =  [ ]
        self.locDict : dict[int, tuple[int, int]] = { } #Dictionary for quick look up if number is present
        self.currentSum : int = 0 #Sum of unselected items
        self.isWinner : bool = False
        self.winValue : int = 0

        rowNum = -1
        for rowIndex in range(0,len(rows)):            
            cols = [int(item) for item in rows[rowIndex].split()]
            self.currentSum += sum(cols)
            self.items.append(cols)            
            for colIndex in range(0,len(cols)):
                self.locDict[cols[colIndex]] = ( rowIndex, colIndex)


    def CallNumber(self, number : int):
        if number in self.locDict:
            self.currentSum -= number
            loc = self.locDict[number]
            self.items[loc[0]][loc[1]] = -1

            #check winner using row and column
            if (len(set(self.items[loc[0]])) == 1):
                self.isWinner = True
            
            row = [item[loc[1]] for item in self.items]
            if (len(set(row)) == 1):
                self.isWinner = True
            
            if self.isWinner:
                self.winValue = number * self.currentSum

def createBoards(lines) :
    boardStart = 2
    boardLength = 5
    boards = [ ]

    while boardStart < len(lines):
        b = Board(lines[boardStart: boardStart+boardLength])
        boards.append(b)
        boardStart+=(boardLength+1) #boards are 5 items long plus blank line in between
    return boards

with open(filename) as f:
    lines = [item.strip() for item in f.readlines()]
    f.close()

#Part 1
#create boards and numbers
callNumbers = [int(item) for item in lines[0].split(',')]
boards = createBoards(lines)

winnerFound = False
callIndex = 0

while winnerFound == False and callIndex < len(callNumbers):
    for b in boards:
        b.CallNumber(callNumbers[callIndex])
        if b.isWinner:
            winnerFound = True
            winningBoard = b

    callIndex+=1

print(str(winningBoard.winValue))

#Part 2
callIndex = 0
boards = createBoards(lines)
while callIndex < len(callNumbers):
    for b in boards:
        if b.isWinner:
            continue
        
        b.CallNumber(callNumbers[callIndex])
        if b.isWinner:
            lastBoardToWin = b            

    callIndex+=1

print(str(lastBoardToWin.winValue))