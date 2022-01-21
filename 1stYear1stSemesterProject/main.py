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
    
def qMoversMove(board, cboard, mboard, move, hrmboard, hlmboard, humboard, hdmboard, vrmboard, vlmboard, vumboard, vdmboard, kboard, cpboard):
    #move, assign to new board
    #merge boards, by getting posstions on each board, then writing to mboard

    vumboard = Move(Vumover, move, cboard, vumboard, vumrow, vumcol)
    vdmboard = Move(Vdmover, move, cboard, vdmboard, vdmrow, vdmcol)
    vlmboard = Move(Vlmover, move, cboard, vlmboard, vlmrow, vlmcol)
    vrmboard = Move(Vrmover, move, cboard, vrmboard, vrmrow, vrmcol)
    humboard = Move(Humover, move, cboard, humboard, humrow, humcol)
    hdmboard = Move(Hdmover, move, cboard, hdmboard, hdmrow, hdmcol)
    hlmboard = Move(Hlmover, move, cboard, hlmboard, hlmrow, hlmcol)
    hrmboard = Move(Hrmover, move, cboard, hrmboard, hrmrow, hrmcol)
    merge = copy.deepcopy(cboard)
    merge = merger(merge, kboard)
    merge = merger(merge, cpboard)
    merge = merger(merge, vumboard)
    merge = merger(merge, vdmboard)
    merge = merger(merge, vlmboard)
    merge = merger(merge, vrmboard)
    merge = merger(merge, humboard)
    merge = merger(merge, hdmboard)
    merge = merger(merge, hlmboard)
    merge = merger(merge, hrmboard)

    return merge

def merger(Board, targetBoard):
    Drow = 0
    Dcol = 0
    dummy = copy.deepcopy(Board)
    toggle = False
    for y in targetBoard:
        for x in y:
            if x != "." and x != "t" and x != "T":
                toggle = True
                dummy[Drow][Dcol] = x
            Dcol += 1
        Drow += 1; Dcol = 0
        if toggle == False:
            dummy = 0
            return dummy
        
    return dummy

def Move(m, move, cboard, currboard, row, col):
    dummy = copy.deepcopy(cboard)
    k = currboard
    for i in range(len(row)):
        if move == up:
            if m == Vdmover:
                if row[i] + 1 > Srow - 1:
                    row[i] = 0
                else:
                    row[i] = row[i] + 1
            elif m == Vrmover:
                if col[i] + 1 > Scol - 1:
                    col[i] = 0
                else:
                    col[i] = col[i] + 1
            elif m == Vlmover:
                if col[i] - 1 < 0:
                    col[i] = Scol - 1
                else:
                    col[i] = col[i] - 1
            elif m == Player or m == Vumover:
                if row[i] - 1 < 0:
                    row[i] = Srow - 1
                else:
                    row[i] = row[i] - 1
            dummy[row[i]][col[i]] = m

        elif move == down:
            if m == Vumover:
                if row[i] - 1 < 0:
                    row[i] = Srow - 1
                else:
                    row[i] = row[i] - 1
            elif m == Vrmover:
                if col[i] + 1 > Scol - 1:
                    col[i] = 0
                else:
                    col[i] = col[i] + 1
            elif m == Vlmover:
                if col[i] - 1 < 0:
                    col[i] = Scol - 1
                else:
                    col[i] = col[i] - 1
            elif m == Player or m == Vdmover:
                if row[i] + 1 > Srow - 1:
                    row[i] = 0
                else:
                    row[i] = row[i] + 1
            dummy[row[i]][col[i]] = m
            
        elif move == left:
            if m == Humover:
                if row[i] - 1 < 0:
                    row[i] = Srow - 1
                else:
                    row[i] = row[i] - 1
            elif m == Hdmover:
                if row[i] + 1 > Srow - 1:
                    row[i] = 0
                else:
                    row[i] = row[i] + 1
            elif m == Hrmover:
                if col[i] + 1 > Scol - 1:
                    col[i] = 0
                else:
                    col[i] = col[i] + 1
            elif m == Player or m == Hlmover:
                if col[i] - 1 < 0:
                    col[i] = Scol - 1
                else:
                    col[i] = col[i] - 1
            dummy[row[i]][col[i]] = m

        elif move == right:
            if m == Humover:
                if row[i] - 1 < 0:
                    row[i] = Srow - 1
                else:
                    row[i] = row[i] - 1
            elif m == Hdmover:
                if row[i] + 1 > Srow - 1:
                    row[i] = 0
                else:
                    row[i] = row[i] + 1
            elif m == Hlmover:
                if col[i] - 1 < 0:
                    col[i] = Srow - 1
                else:
                    col[i] = col[i] - 1
            elif m == Player or m == Hrmover:
                if col[i] + 1 > Scol - 1:
                    col[i] = 0
                else:
                    col[i] = col[i] + 1 
            dummy[row[i]][col[i]] = m
        k = copy.deepcopy(dummy)
    return k

def swap(board, ch):
    s = ""
    Drow = 0; Dcol = 0
    for x in board:
        for y in x:
            if y != "." and y != "\n" and y != Target and y != Target.upper():
                board[Drow][Dcol] = ch
            Dcol += 1
        Drow += 1; Dcol = 0
    return board

def checksur(move, board, row, col, kboard, cpboard, Srow, Scol):
    x = board
    gameover = False

    if move == up:
        if row - 1 == -1:
            row = Srow - 1
        else:
            row = row - 1
        if board[row][col] == Key:
            cpboard = swap(cpboard, "P")
            kboard = swap(kboard, ".")
            x = merger(board, cpboard)
        elif board[row][col] != Ovswitch and board[row][col] != Oport and board[row][col] != Target and board[row][col] != Target.upper() and board[row][col] != Key and board[row][col] != Key.upper() and board[row][col] != ".":
            print("You lose!")
            gameover = True
        
    elif move == down:
        if row + 1 == Srow:
            row = 0
        else:
            row = row + 1
        if board[row][col] == Key:
            cpboard = swap(cpboard, "P")
            kboard = swap(kboard, ".")
            x = merger(board, cpboard)
        elif board[row][col] != Ovswitch and board[row][col] != Oport and board[row][col] != Target and board[row][col] != Target.upper() and board[row][col] != Key and board[row][col] != Key.upper() and board[row][col] != ".":
            print("You lose!")
            gameover = True


    elif move == left:
        if col - 1 < 0:
            col = Scol - 1
        else:
            col = col - 1
        if board[row][col] == Key:
            cpboard = swap(cpboard, "P")
            kboard = swap(kboard, ".")
            x = merger(board, cpboard)
        elif board[row][col] != Ovswitch and board[row][col] != Oport and board[row][col] != Target and board[row][col] != Target.upper() and board[row][col] != Key and board[row][col] != Key.upper() and board[row][col] != ".":
            print("You lose!")
            gameover = True
        
    elif move == right:
        if col + 1 == Scol - 1:
            col = 0
        else:
            col = col + 1
        if board[row][col] == Key:
            cpboard = swap(cpboard, "P")
            kboard = swap(kboard, ".")
            x = merger(board, cpboard)
        elif board[row][col] != Ovswitch and board[row][col] != Oport and board[row][col] != Target and board[row][col] != Target.upper() and board[row][col] != Key and board[row][col] != Key.upper() and board[row][col] != ".":
            print("You lose!")
            gameover = True
        
    return x, gameover

def switches(board):
    Drow = 0; Dcol = 0
    for x in board:
        for y in x:
            if y != "." and y != "\n" and y != Target and y != Target.upper():
                board[Drow][Dcol] = y.swapcase()
            Dcol += 1
        Drow += 1; Dcol = 0
    return board

up = "k"; down = "j"; left = "h"; right = "l"
BNumber = "01"

Player = "s" #or S
Target = "t" #or T
Wall = "x" #or X
Cvswitch = "v"; Ovswitch = "V"
Chswitch = "h"; Ohswitch = "H"
Key = "k" #or K
Cport = "p"; Oport = "P"
Hrmover = "r"; Hlmover = "l"; Humover = "u"; Hdmover = "d"
Vrmover = "R"; Vlmover = "L"; Vumover = "U"; Vdmover = "D"


s = open("C:\\Users\\Jayden\\Code\\Python-Dev\\1stYear1stSemesterProject\\boards\\board_"+ BNumber+ ".txt")
Title = s.readline()
Dimentions = s.readline()
Srow = int(Dimentions[0])
Scol = int(Dimentions[2])
print(Srow, Scol)

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

prow, pcol, pboard = finder(Player, Board, Cboard)
trow, tcol, tboard = finder(Target, Board, Cboard)
cvsrow, cvscol, cvsboard = finder(Cvswitch, Board, Cboard)
chsrow, chscol, chsboard = finder(Chswitch, Board, Cboard)
ohsrow, ohscol, ohsboard = finder(Ohswitch, Board, Cboard)
ovsrow, ovscol, ovsboard = finder(Ovswitch, Board, Cboard)

Board = merger(Board, ohsboard)
Board = merger(Board, chsboard)
Board = merger(Board, ovsboard)
Board = merger(Board, cvsboard)

krow, kcol, kboard = finder(Key, Board, Cboard)
cprow, cpcol, cpboard = finder(Cport, Board, Cboard)
oprow, opcol, opboard = finder(Oport, Board, Cboard)
hrmrow, hrmcol, hrmboard = finder(Hrmover, Board, Cboard)
hlmrow, hlmcol, hlmboard = finder(Hlmover, Board, Cboard)
humrow, humcol, humboard = finder(Humover, Board, Cboard)
hdmrow, hdmcol, hdmboard = finder(Hdmover, Board, Cboard)
vrmrow, vrmcol, vrmboard = finder(Vrmover, Board, Cboard)
vlmrow, vlmcol, vlmboard = finder(Vlmover, Board, Cboard)
vumrow, vumcol, vumboard = finder(Vumover, Board, Cboard)
vdmrow, vdmcol, vdmboard = finder(Vdmover, Board, Cboard)

#inp = input()

Mfile = open("C:\\Users\\Jayden\\Code\\Python-Dev\\1stYear1stSemesterProject\\boards\\moves_"+ BNumber+ ".txt")
mf = Mfile.readline()
#print(mf)
for inp in mf:
    print(inp+ "_")


   # while inp != "x":
    # while inp != up and inp != down and inp != left and inp != right and inp != "x":
    #     print("Incorrect input")
    #     printBoard(Board)
    #     inp = input()
    Board  = qMoversMove(Board, Cboard, Mboard, inp, hrmboard, hlmboard, humboard, hdmboard, vrmboard, vlmboard, vumboard, vdmboard, kboard, cpboard)    
    #toggle keys, switches
    if inp == up or inp == down:
        ovsboard = switches(ovsboard)
        cvsboard = switches(cvsboard)
        Board = merger(Board, ovsboard)
        Board = merger(Board, cvsboard)
        Board = merger(Board, ohsboard)
        Board = merger(Board, chsboard)
    elif inp == right or left:
        ohsboard = switches(ohsboard)
        chsboard = switches(chsboard)
        Board = merger(Board, ohsboard)
        Board = merger(Board, chsboard)
        Board = merger(Board, ovsboard)
        Board = merger(Board, cvsboard)

    #check player surroundings
    Board = merger(Board, ovsboard)
    Board, Gameover = checksur(inp, Board, prow[0], pcol[0], kboard, cpboard, Srow, Scol)
    
    p = Move(Player, inp, Cboard, pboard, prow, pcol)
    prow, pcol, pboard = finder(Player, p, Cboard)
    Board = merger(Board, pboard)
    
    if prow == trow and pcol == tcol:
        print("You won!")
        printBoard(Board)
        exit()
    elif Gameover == True:
        #print("You lose!")
        printBoard(Board)
        exit()
    printBoard(Board)

    # inp = input("")
Mfile.close