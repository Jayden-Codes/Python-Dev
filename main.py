import copy

"""finds positions of characters"""
def finder(ch, board):
    R = 0; C = 0
    Rpos = []; Cpos = []
    for x in board:
        for y in x:
            if ch == "s" or ch == "S":
                if y == ch:
                    Rpos.append(R)
                    Cpos.append(C)
            elif ch == "x" or ch == "X":
                if y == ch:
                    Rpos.append(R)
                    Cpos.append(C)
            elif ch == "k" or ch == "K":
                if y == ch:
                    Rpos.append(R)
                    Cpos.append(C)
            elif ch == "t" or ch == "T":
                if y == ch:
                    Rpos.append(R)
                    Cpos.append(C)
            elif y == ch:
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
def playerMove(board, cboard):
    if Move == up:
        dummy = copy.deepcopy(cboard)
        Prow, Pcol = finder(Player, board)
        for i in range(len(Prow)):
            if Board[Prow[i]-1][Pcol[i]] != ".":
                print("You lose!")
                printBoard(board)
                return exit()
            else:
                Prow[i] = Prow[i] - 1
                dummy[Prow[i]][Pcol[i]] = Player
                x = copy.deepcopy(dummy)
        return x

def moversMove(board, cboard, mboard, move):

    # mboard = dusty(Vrmover, move, cboard, mboard)
    # mboard = dusty(Vlmover, move, cboard, mboard)
    mboard = dusty(Vumover, move, cboard, mboard)
    # mboard = dusty(Vdmover, move, cboard, mboard)

    # mboard = dusty(Hrmover, move, cboard, mboard)
    # mboard = dusty(Hlmover, move, cboard, mboard)
    mboard = dusty(Humover, move, cboard, mboard)
    #mboard = dusty(Hdmover, move, cboard, mboard)
    return mboard
def dusty(x, move, cboard, mboard):
    row, col = finder(x, mboard)
    dummy = copy.deepcopy(cboard)
    k=mboard
    for i in range(len(row)):
        if move == up:
            if x == Vumover:
                row[i] = row[i] - 1
            elif x == Vdmover:
                row[i] = row[i] + 1
            elif x == Vrmover:
                col[i] = col[i] + 1
            elif x == Vlmover:
                col[i] = col[i] - 1
            dummy[row[i]][col[i]] = x
        elif move == down:
            if x == Vumover:
                row[i] = row[i] - 1
            elif x == Vdmover:
                row[i] = row[i] + 1
            elif x == Vrmover:
                col[i] = col[i] + 1
            elif x == Vlmover:
                col[i] = col[i] - 1
            dummy[row[i]][col[i]] = x
        k = copy.deepcopy(dummy)
    return k

up = "k"; down = "j"; left = "h"; right = "l"

Player = "s" #or S
Target = "t" #or T
Wall = "x" #or X

Cvswitch = "v"; Ovswitch = "V"
Chswitch = "h"; Ohswitch = "H"

Key = "k" #or K
Cport = "p"; Oport = "P"

Hrmover = "r"; Hlmover = "l"; Humover = "u"; Hdmover = "d"
Vrmover = "R"; Vlmover = "L"; Vumover = "U"; Vdmover = "D"

s = open("C:\\Users\\Jayden\\Code\\Python-Dev\\boards\\board_06.txt")
Title = s.readline()
Dimentions = s.readline()

Board = []; Cboard = []; Mboard = []
for x in s:
    Dummy = []
    for y in x:
        Dummy.append(y)
    Board.append(Dummy)
s.close

Cboard = copy.deepcopy(Board)
Mboard = copy.deepcopy(Board)
Drow = 0; Dcol = 0
Mrow = 0; Mcol = 0
for x in Cboard:
    for y in x:
        if y == Target or y == Target.upper or y == Player or y == Player.upper:
            Mboard[Mrow][Mcol] = "."
        if y != Wall and y != Wall.upper and y != "." and y != Target and y != Target.upper and y != "\n":
            Cboard[Drow][Dcol] = "."    
        Dcol += 1
        Mcol += 1
    Drow += 1; Dcol = 0
    Mrow += 1; Mcol = 0

#Steps
#Switches are turned on/off with boolean
#Movers move
#player moves
#if not fail, update clear board
printBoard(Board)
d = moversMove(Board, Cboard, Mboard, up)
Move = input()
while Move != "":
    Mboard  = moversMove(Board, Cboard, Mboard, Move)
    printBoard(Mboard)
    Board = playerMove(Board, Cboard)
    #printBoard(Board)
    Move = input()



   