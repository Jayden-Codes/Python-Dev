import copy

"""finds positions of characters"""
def finder(ch, board):
    R = 0; C = 0
    Rpos = []; Cpos = []
    for x in board:
        for y in x:
            if y == ch.upper() or  y == ch.lower() :
                Rpos.append(R)
                Cpos.append(C)
            C += 1
        R += 1
        C = 0
    return Rpos, Cpos

"""prints boards in nice format"""
def printBoard(board):
    sf = ""
    for x in board:
        for y in x:
            sf += y        
    print(sf)
    
"""player movement"""
def playerMove(Move, board, cboard):
    if Move == up:
        dummy = copy.deepcopy(cboard)
        Prow, Pcol = finder("o", board)
        for i in range(len(Prow)):
            if board[Prow[i]-1][Pcol[i]] != ".":
                print("You lose!")
                printBoard(board)
                return exit()
            else:
                Prow[i] = Prow[i] - 1
                dummy[Prow[i]][Pcol[i]] = "o"
                x = copy.deepcopy(dummy)

    return x


up = "8"
down = "2"
left = "4"
right = "6"

s = open("C:\\Users\\Jayden\\Code\\Python-Dev\\boards\\board_1.txt")
Board = []
Cboard = []
for x in s:
    Dummy = []
    for y in x:
        Dummy.append(y)
    Board.append(Dummy)
s.close

Prow, Pcol = finder("x", Board)
print(Prow, Pcol)
Cboard = copy.deepcopy(Board)
Drow = 0; Dcol = 0

for x in Cboard:
    for y in x:
        if y != "x" and y!= "." and y != "t" and y!= "\n":
            Cboard[Drow][Dcol] = "."    
        Dcol += 1
    Drow += 1
    Dcol = 0

printBoard(Cboard)
Move = input()
while Move != "":
    Board = playerMove(Move, Board, Cboard)
    printBoard(Board)
    Move = input()



   