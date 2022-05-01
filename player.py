import board as board

def setMove(b, x, y, play):
    b[x][y] = play

def playMove(b):
    temp = True
    moves = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    while temp:
        try:
            move = int(input("Please pick a position between 1 and 9:\n"))
            if move < 1 or move > 9:
                print("Invalid number\n")
   #         elif not (moves[move] in board.boardEmpty(b)):
     #           print("Box filled")
            else:
                setMove(b, moves[move][0], moves[move][1], board.XPLAY)
                board.printBoard(b)
                temp = False
        except(KeyError, ValueError):
            print("Please pick a number!")
