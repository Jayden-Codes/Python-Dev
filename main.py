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

def moversMove(board, cboard, mboard, move):
    Vrow, Vcol = finder("v", mboard)
    Hrow, Hcol = finder("h", mboard)
    dummy = copy.deepcopy(cboard)
    k=0
    for i in range(len(Vrow)):
        if move == up:
            Vrow[i] = Vrow[i] - 1
            dummy[Vrow[i]][Vcol[i]] = "v"
        elif move == down:
            Vrow[i] = Vrow[i] + 1
            dummy[Vrow[i]][Vcol[i]] = "v"
        k = copy.deepcopy(dummy)
    return k


up = "8"
down = "2"
left = "4"
right = "6"

s = open("C:\\Users\\Jayden\\Code\\Python-Dev\\boards\\board_01.txt")
Board = []
Cboard = []
for x in s:
    Dummy = []
    for y in x:
        Dummy.append(y)
    Board.append(Dummy)
s.close

Prow, Pcol = finder("x", Board)
Cboard = copy.deepcopy(Board)
Mboard = copy.deepcopy(Board)
Drow = 0; Dcol = 0
Mrow = 0; Mcol = 0
for x in Cboard:
    for y in x:
        if y == "t" or y == "T" or y== "o" or y == "O":
            Mboard[Mrow][Mcol] = "."
        if y != "x" and y!= "." and y != "t" and y!= "\n":
            Cboard[Drow][Dcol] = "."    
        Dcol += 1
        Mcol += 1
    Drow += 1; Dcol = 0
    Mrow += 1; Mcol = 0
#printBoard(Cboard)
Move = input()
while Move != "":
    Mboard = moversMove(Board, Cboard, Mboard, Move)
    printBoard(Mboard)
    Board = playerMove(Move, Board, Cboard)
    #printBoard(Board)
    Move = input()



   