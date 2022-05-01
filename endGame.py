import board as board

def winningPlay(b, play):
    winState = [[b[0][0], b[0][1], b[0][2]],
                [b[0][0],b[1][1], b[2][2]],
                [b[0][0], b[1][0], b[2][0]],
                [b[0][1], b[1][1], b[2][1]],
                [b[0][2], b[1][2], b[2][2]],
                [b[0][2], b[1][1], b[2][0]],
                [b[1][0], b[1][1], b[1][2]],
                [b[2][0], b[2][1], b[2][2]]]
    if[play, play, play] in winState:
        return True
    else:
        return False

def win(b):
    return winningPlay(b, board.XPLAY) or winningPlay(b, board.OPLAY)

def score(b):
    if winningPlay(b, board.XPLAY):
        return 10
    elif winningPlay(b, board.OPLAY):
        return -10
    else:
        return 0

def printResult(b):
    if winningPlay(b, board.XPLAY):
        print("X has won\n")
    elif winningPlay(b, board.OPLAY):
        print("O has won\n")
    else:
        print("Draw\n")