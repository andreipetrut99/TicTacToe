repeat = True;

def printBoard(board):
    counter = 0
    for row in board:
        for column in row:
            print("{} |".format(column), end=" ")
        print()
    print()


def checkBoard(board):
    if (board[0] == ["X", "X", "X"]) | (board[0] == ["O", "O", "O"]):
        return True
    if (board[1] == ["X", "X", "X"]) | (board[1] == ["O", "O", "O"]):
        return True
    if (board[2] == ["X", "X", "X"]) | (board[2] == ["O", "O", "O"]):
        return True
    if (((board[0][0] == "X") & (board[1][0] == "X") & (board[2][0] == "X"))
            | ((board[0][0] == "O") & (board[1][0] == "O") & (board[2][0] == "O"))):
        return True
    if (((board[0][1] == "X") & (board[1][1] == "X") & (board[2][1] == "X"))
            | ((board[0][1] == "O") & (board[1][1] == "O") & (board[2][1] == "O"))):
        return True
    if (((board[0][2] == "X") & (board[1][2] == "X") & (board[2][2] == "X"))
            | ((board[0][2] == "O") & (board[1][2] == "O") & (board[2][2] == "O"))):
        return True
    if (((board[0][0] == "X") & (board[1][1] == "X") & (board[2][2] == "X"))
            | ((board[0][0] == "O") & (board[1][1] == "O") & (board[2][2] == "O"))):
        return True
    if (((board[0][2] == "X") & (board[1][1] == "X") & (board[2][0] == "X"))
            | ((board[0][2] == "O") & (board[1][1] == "O") & (board[2][0] == "O"))):
        return True


while repeat:
    gameOver = False
    moves = 9
    usedIds = {"-1"}

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    print("Incepe jocul!")
    print("Se vor introduce pozitii de la 1 la 9")

    while not gameOver:
        moves -= 1
        printBoard(board)
        idOnBoard = int(input("X alege:"))
        if idOnBoard in usedIds:
            print("Spatiu ocupat! Incercati iar.")
            continue
        else:
            usedIds.add(idOnBoard)

        board[int((idOnBoard - 1) / 3)][int((idOnBoard - 1) % 3)] = "X"
        printBoard(board)

        if checkBoard(board):
            print("X castiga.")
            break

        idOnBoard = int(input("O alege:"))
        if idOnBoard in usedIds:
            print("Spatiu ocupat! Incercati iar.")
            continue
        else:
            usedIds.add(idOnBoard)

        board[int((idOnBoard - 1) / 3)][int((idOnBoard - 1) % 3)] = "O"
        printBoard(board)

        if checkBoard(board):
            print("O castiga.")
            break

        if moves == 0:
            print("Remiza.")
            break

    playAgain = input("Vrei sa joci iar?(D/n)")
    if (playAgain == "D") | (playAgain == "d"):
        repeat = True
    else:
        repeat = False
