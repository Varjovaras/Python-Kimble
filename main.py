from random import randint


# amount of starting pieces
pieces = {"blue": 4, "yellow": 4, "green": 4, "red": 4}

# contents of the table
# 0 means empty
# first integer of each list is their respective starting square
table = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


playerTurn = 0  # 0 first player, 3 last player


def rollDice():
    roll = randint(1, 6)
    return roll


def piecesHome(pieces):
    print("\n")
    print("  -------------")
    print("Blue pieces home:  ", pieces["blue"])
    print("Yellow pieces home:", pieces["yellow"])
    print("Green pieces home: ", pieces["green"])
    print("Red pieces home:   ", pieces["red"])
    print("  -------------")

    print("\n")


def move():
    input("Input anything to roll the dice: ")
    roll = rollDice()
    print("You rolled", roll)


def turnChanger(playerTurn):
    if playerTurn == 3:
        playerTurn = 0


def printBoard():
    piecesHome(pieces)

    # print trouble board
    print("  YELLOW")
    print(" ", *table[0], sep=" ")
    print("  - - - - - - -")
    for i in range(0, 7):
        if i == 0:
            print(str(table[1][i]), "|      GREEN|", str(table[2][6-i]))
        elif i == 6:
            print(str(table[1][i]), "|BLUE       |", str(table[2][6-i]))
        else:
            print(str(table[1][i]), "|           |", str(table[2][6-i]))
    # print("- - - - - - -")
    print("  - - - - - - -")
    print(" ", *table[3], sep=" ")
    print("              RED")

    move()


printBoard()
