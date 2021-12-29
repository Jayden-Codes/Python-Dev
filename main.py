import copy

"""finds positions of characters"""
def finder(ch, board, cboard):
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

    chBoard = writer(ch, Rpos, Cpos, cboard)

    return Rpos, Cpos, chBoard

def writer(ch, row, col, cboard):
    dummy=copy.deepcopy(cboard)
    k=copy.deepcopy(cboard)
    for i in range(len(row)):
        dummy[row[i]][col[i]] = ch
        k = copy.deepcopy(dummy)
    return k


"""prints boards in nice format"""
def printBoard(board):
    b = ""
    for x in board:
        for y in x:
            b += y        
    print(b)
    
"""player movement"""
def playerMove(board, cboard, Prow, Pcol):
    if Move == up:
        dummy = copy.deepcopy(cboard)
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

def qMoversMove(board, cboard, mboard, move):
    #move, assign to new board
    #merge boards, by getting posstions on each board, then writing to mboard

    prow, pcol, pboard = finder(Player, Board, Cboard)
    trow, tcol, tboard = finder(Target, board, cboard)
    cvsrow, cvscol, cvsboard = finder(Cvswitch, board, cboard)
    chsrow, chscol, chsboard = finder(Chswitch, board, cboard)
    ohsrow, ohscol, ohsboard = finder(Ohswitch, board, cboard)
    ovsrow, ovscol, ovsboard = finder(Ovswitch, board, cboard)

    krow, kcol, kboard = finder(Key, board, cboard)
    cprow, cpcol, cpboard = finder(Cport, board, cboard)
    oprow, opcol, opboard = finder(Oport, board, cboard)

    hrmrow, hrmcol, hrmboard = finder(Hrmover, board, cboard)
    hlmrow, hlmcol, hlmboard = finder(Hlmover, board, cboard)
    humrow, humcol, humboard = finder(Humover, board, cboard)
    hdmrow, hdmcol, hdmboard = finder(Hdmover, board, cboard)
    vrmrow, vrmcol, vrmboard = finder(Vrmover, board, cboard)
    vlmrow, vlmcol, vlmboard = finder(Vlmover, board, cboard)
    vumrow, vumcol, vumboard = finder(Vumover, board, cboard)
    vdmrow, vdmcol, vdmboard = finder(Vdmover, board, cboard)
    
    vumboard = moverMove(Vumover, move, cboard, vumboard, vumrow, vumcol)
    vdmboard = moverMove(Vdmover, move, cboard, vdmboard, vdmrow, vdmcol)
    vlmboard = moverMove(Vlmover, move, cboard, vlmboard, vlmrow, vlmcol)
    vrmboard = moverMove(Vrmover, move, cboard, vrmboard, vrmrow, vrmcol)

    humboard = moverMove(Humover, move, cboard, humboard, humrow, humcol)
    hdmboard = moverMove(Hdmover, move, cboard, hdmboard, hdmrow, hdmcol)
    hlmboard = moverMove(Hlmover, move, cboard, hlmboard, hlmrow, hlmcol)
    hrmboard = moverMove(Hrmover, move, cboard, hrmboard, hrmrow, hrmcol)
    
    
    d = copy.deepcopy(vdmboard)
    print("^^^")
    return d

def moverMove(m, move, cboard, currboard, row, col):
    dummy = copy.deepcopy(cboard)
    k=currboard
    for i in range(len(row)):
        if move == up:
            if m == Vumover:
                row[i] = row[i] - 1
            elif m == Vdmover:
                if row[i] + 1 > len(row)+1:
                    row[i] = 0
                else:
                    row[i] = row[i] + 1
            elif m == Vrmover:
                col[i] = col[i] + 1
            elif m == Vlmover:
                col[i] = col[i] - 1
            elif m == Player:
                row[i] = row[i] - 1
            dummy[row[i]][col[i]] = m

        elif move == down:
            if m == Vumover:
                row[i] = row[i] - 1
            elif m == Vdmover:
                row[i] = row[i] + 1
            elif m == Vrmover:
                col[i] = col[i] + 1
            elif m == Vlmover:
                col[i] = col[i] - 1
            elif m == Player:
                row[i] = row[i] + 1
            dummy[row[i]][col[i]] = m
        elif move == left:
            if m == Humover:
                row[i] = row[i] - 1
            elif m == Hdmover:
                row[i] = row[i] + 1
            elif m == Hrmover:
                col[i] = col[i] + 1
            elif m == Hlmover:
                col[i] = col[i] - 1
            elif m == Player:
                col[i] = col[i] - 1
            dummy[row[i]][col[i]] = m
        elif move == right:
            if m == Humover:
                row[i] = row[i] - 1
            elif m == Hdmover:
                row[i] = row[i] + 1
            elif m == Hrmover:
                col[i] = col[i] + 1
            elif m == Hlmover:
                col[i] = col[i] - 1
            elif m == Player:
                col[i] = col[i] + 1
            dummy[row[i]][col[i]] = m
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
printBoard(Cboard)

prow, pcol, pboard = finder(Player, Board, Cboard)
    # trow, tcol, tboard = finder(Target, Board, Cboard)
    # cvsrow, cvscol, cvsboard = finder(Cvswitch, Board, Cboard)
    # chsrow, chscol, chsboard = finder(Chswitch, Board, Cboard)
    # ohsrow, ohscol, ohsboard = finder(Ohswitch, Board, Cboard)
    # ovsrow, ovscol, ovsboard = finder(Ovswitch, Board, Cboard)
    # krow, kcol, kboard = finder(Key, Board, Cboard)
    # cprow, cpcol, cpboard = finder(Cport, Board, Cboard)
    # oprow, opcol, opboard = finder(Oport, Board, Cboard)
    # hrmrow, hrmcol, hrmboard = finder(Hrmover, Board, Cboard)
    # hlmrow, hlmcol, hlmboard = finder(Hlmover, Board, Cboard)
    # humrow, humcol, humboard = finder(Humover, Board, Cboard)
    # hdmrow, hdmcol, hdmboard = finder(Hdmover, Board, Cboard)
    # vrmrow, vrmcol, vrmboard = finder(Vrmover, Board, Cboard)
    # vlmrow, vlmcol, vlmboard = finder(Vlmover, Board, Cboard)
    #vumrow, vumcol, vumboard = finder(Vumover, Board, Cboard)
    # vdmrow, vdmcol, vdmboard = finder(Vdmover, Board, Cboard)

Move = input()
while Move != "":
    Board  = qMoversMove(Board, Cboard, Mboard, Move)
    #printBoard(Mboard)
    print("-----")
    printBoard(Board)
    print("-----")
    #g = playerMove(Board, Cboard, prow, pcol)
    g = moverMove(Player, Move, Cboard, pboard, prow, pcol)
    prow, pcol, pboard = finder(Player, g, Cboard)
    printBoard(pboard)
    Move = input()



   