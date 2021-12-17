from random import randint
import sys

# amount of starting pieces
pieces = {1: 4,
          2: 4,
          3: 4,
          4: 4}

# contents of the table
# 0 means empty
# first integer of each list is their respective starting square
table = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
# BYGR
blueFinish = [0, 0, 0, 0]
yellowFinish = [0, 0, 0, 0]
greenFinish = [0, 0, 0, 0]
redFinish = [0, 0, 0, 0]


# 1 first player, 4 last player, 0 reserved for empty
playerTurn = 1


def piecesOnBoard():
    piecesOnBoard = 0
    for list in table:
        for piece in list:
            if piece == playerTurn:
                piecesOnBoard += 1

    return piecesOnBoard


def rollDice():
    input("Input anything to roll the dice: ")
    roll = randint(1, 6)
    print("-------------\n")
    print("You rolled", roll, "\n")

    return roll


def rolledSix():
    if pieces[playerTurn] == 4:
        input("Roll again to move your first piece: ")
    else:
        input("You rolled 6. Roll again: ")
    roll = randint(1, 6)
    print("-------------\n")
    print("You rolled", roll, "\n")

    return roll


def printPlayerTurn():
    if playerTurn == 1:
        print("BLUE PLAYERS TURN ")
    elif playerTurn == 2:
        print("YELLOW PLAYERS TURN")
    elif playerTurn == 3:
        print("GREEN PLAYERS TURN")
    elif playerTurn == 4:
        print("RED PLAYERS TURN")


def nextPlayer():
    global playerTurn
    if playerTurn == 4:
        playerTurn = 1
    else:
        playerTurn += 1


def move():
    # keeps rolling until legal move is made
    while True:
        printPlayerTurn()
        roll = rollDice()
        # print("You rolled", roll, "\n")
        pieceToMove = checkLegalMoves(roll)
        if pieceToMove == "next player rolls again":
            print("-------------\n")
        elif pieceToMove == "move complete":
            break
        elif pieceToMove == "move one piece":
            nextPlayer()
            break
        else:
            print("What is going on?")  # shouldnt happen (anymore)
            break


def checkLegalMoves(roll):
    global table
    pieceAmount = piecesOnBoard()
    # print("PIECE AMOUNT", pieceAmount)
    # print("PIECES PLAYERTURN", pieces[playerTurn])
    # print("ROLL", roll)
    if pieces[playerTurn] == 4 and roll < 6:
        print("Didn't roll 6. Can't move anything. Next players turn")
        nextPlayer()
        return "next player rolls again"

    elif pieces[playerTurn] == 4 and roll == 6:
        # table[playerTurn-1][0] = playerTurn
        newPiece()
        return "move complete"

    elif pieces[playerTurn] < 4 and pieceAmount == 1:

        if roll == 6:
            askIfYouWantNewPiece(roll)
            return "move complete"

        else:
            countMove(0, roll)
            nextPlayer()
            return "move complete"

    elif pieces[playerTurn] < 4 and pieceAmount > 1:

        if roll == 6:
            askIfYouWantNewPiece(roll)
            return "move complete"

        else:
            severalPieces(roll)
            nextPlayer()
            return "move complete"
    elif pieceAmount == 0 and roll < 6:
        print("Didn't roll 6. Can't move anything. Next players turn")
        nextPlayer()
        return "next player rolls again"

    elif pieceAmount == 0 and roll == 6:
        # table[playerTurn-1][0] = playerTurn
        newPiece()
        return "move complete"
    else:
        print("What ?")
        return False


def askIfYouWantNewPiece(roll):

    playerInput = input(
        "Do you want to play a new piece onto the board or play with existing one?\n---\nInput N for new piece and anything else to move your piece on board: ")
    if playerInput == "n" or playerInput == "N":
        newPiece()
        return

    else:
        pieceAmount = piecesOnBoard()
        if pieceAmount > 1:
            severalPieces(roll)
        else:
            countMove(0, roll)


def severalPieces(roll):
    newTable = []
    for i in range(0, 4):
        for j in range(0, 7):
            newTable.append(table[i][j])
    indexes = [i for i, j in enumerate(newTable) if j == playerTurn]
    print("You have pieces in", indexes,
          "\nMove by inputting 1, 2, 3 or 4 based on their order on the board")
    while True:
        playerInput = int(input("1, 2, 3 or 4? "))
        if playerInput <= len(indexes):
            break
        else:
            continue
    if playerInput == 1:
        print(indexes[0])
        countMove(indexes[0], roll)
    elif playerInput == 2:
        countMove(indexes[1], roll)
    elif playerInput == 3:
        countMove(indexes[2], roll)
    elif playerInput == 4:
        countMove(indexes[3], roll)
    else:
        print("What????")  # this shouldn't happen


def newPiece():
    roll = rolledSix()
    if table[playerTurn-1][0] != 0:
        pieces[table[playerTurn-1][0]] += 1
    pieces[playerTurn] -= 1
    table[playerTurn-1][roll] = playerTurn


def checkWin():

    if playerTurn == 1 and blueFinish == [1, 1, 1, 1]:
        print(table)
        sys.exit("BLUE WINS!!!11111")
    elif playerTurn == 2 and yellowFinish == [1, 1, 1, 1]:
        sys.exit("YELLOW WINS!!!11111")
    elif playerTurn == 3 and greenFinish == [1, 1, 1, 1]:
        sys.exit("GREEN WINS!!!11111")
    elif playerTurn == 4 and redFinish == [1, 1, 1, 1]:
        sys.exit("RED WINS!!!11111")


def checkFinish(roll):
    while True:
        if roll >= 4:
            break
        elif playerTurn == 1 and blueFinish[roll] == 0:
            blueFinish[roll] = 1
            checkWin()
            print("Your finish is currently: ", blueFinish)
            return True
        elif playerTurn == 2 and yellowFinish[roll] == 0:
            yellowFinish[roll] = 1
            checkWin()
            print("Your finish is currently: ", yellowFinish)
            return True

        elif playerTurn == 3 and greenFinish[roll] == 0:
            greenFinish[roll] = 1
            checkWin()
            print("Your finish is currently: ", greenFinish)

            return True

        elif playerTurn == 4 and redFinish[roll] == 0:
            redFinish[roll] = 1
            checkWin()
            print("Your finish is currently: ", redFinish)

            return True

    print("Didn't finish with this roll")
    if playerTurn == 1:
        print("Your finish is currently: ", blueFinish)
    elif playerTurn == 2:
        print("Your finish is currently: ", yellowFinish)
    elif playerTurn == 3:
        print("Your finish is currently: ", greenFinish)
    elif playerTurn == 4:
        print("Your finish is currently: ", redFinish)
    return False


def countMove(pieceToMove, roll):
    pieceAmount = piecesOnBoard()
    originalIndex = 0
    index = 0
    newTable = []
    finish = ""

    for i in range(0, 4):
        for j in range(0, 7):
            newTable.append(table[i][j])

    if pieceAmount == 1:
        originalIndex = newTable.index(playerTurn)
        index = originalIndex + roll

    elif pieceAmount > 1:
        originalIndex = pieceToMove
        index = originalIndex + roll

    # print(index, originalIndex, index-7)

    if playerTurn == 1 and index > 27:
        finish = checkFinish(index-28)
    elif playerTurn == 2 and originalIndex >= 1 and originalIndex < 7 and index > 6:
        finish = checkFinish(index-7)
    elif playerTurn == 3 and originalIndex >= 8 and originalIndex < 14 and index > 13:
        finish = checkFinish(index-14)
    elif playerTurn == 4 and originalIndex >= 15 and originalIndex < 20 and index > 20:
        finish = checkFinish(index-21)

    if index > 28:
        index = index - 28

    if finish == False:
        # print(table)  # testing
        # print(pieces)  # testing
        return

    # makes the starting square 0
    if originalIndex >= 0 and originalIndex < 7:
        table[0][originalIndex] = 0
    elif originalIndex >= 7 and originalIndex < 14:
        table[1][originalIndex-7] = 0
    elif originalIndex >= 14 and originalIndex < 21:
        table[2][originalIndex-14] = 0
    elif originalIndex >= 21 and originalIndex < 28:
        table[3][originalIndex-21] = 0

    if finish == True:
        print(True)
        # print(table)  # testing
        # print(pieces)  # testing
        return

    if index >= 0 and index < 7:
        if table[0][index] != 0:
            print(table[0][index])
            pieces[table[0][index]] += 1
        table[0][index] = playerTurn

    elif index >= 7 and index < 14:
        if table[1][index-7] != 0:
            pieces[table[1][index-7]] += 1
        table[1][index-7] = playerTurn

    elif index >= 14 and index < 21:
        if table[2][index-14] != 0:
            pieces[table[2][index-14]] += 1
        table[2][index-14] = playerTurn

    elif index >= 21 and index < 28:
        if table[3][index-21] != 0:
            pieces[table[3][index-21]] += 1
        table[3][index-21] = playerTurn
    print(table)  # testing
    print(pieces)  # testing


def printPiecesHome(pieces):
    print("\n")
    print("  -------------")
    print("Blue pieces home:  ", pieces[1])
    print("Yellow pieces home:", pieces[2])
    print("Green pieces home: ", pieces[3])
    print("Red pieces home:   ", pieces[4])
    print("  -------------")
    print("\n")


def printBoard():
    while True:

        table[3].reverse()  # red squares
        printPiecesHome(pieces)
        print("  YELLOW")
        print(" ", *table[1], sep=" ")  # yellow squares
        print("  - - - - - - -")

        # blue and green
        for i in range(0, 7):
            if i == 0:
                print(str(table[0][6-i]), "|      GREEN|", str(table[2][i]))
            elif i == 6:
                print(str(table[0][6-i]), "|BLUE       |", str(table[2][i]))
            else:
                print(str(table[0][6-i]), "|           |", str(table[2][i]))

        # print("- - - - - - -")
        print("  - - - - - - -")
        print(" ", *table[3], sep=" ")
        print("              RED")
        print("  -------------")

        move()


printBoard()


# askIfYouWantNewPiece() #testing
# severalPieces(4) #testing
# countMove(0, 6) #testing
# move() #testing
