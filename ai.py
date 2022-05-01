import player as player
import endGame as end
import board as board
from random import choice
from math import inf



def miniMax(b, depth, alpha, beta, play):
    row = -1
    col = -1
    if depth == 0 or end.win(b):
        return [row, col, end.score(b)]
    else: 
        for emp in board.boardEmpty(b):
            player.setMove(b, emp[0], emp[1], play)
            point = miniMax(b, depth - 1, alpha, beta, -play)
            if play == board.XPLAY:
                if point[2] > alpha:
                    alpha = point[2]
                    row = emp[0]
                    col = emp[1]
            else:
                if point[2] < beta:
                    beta = point[2]
                    row = emp[0]
                    col = emp[1]
            player.setMove(b, emp[0], emp[1], board.EMPTY)
            if alpha >= beta:
                break
        if play == board.XPLAY:
            return [row, col, alpha]
        else: 
            return [row, col, beta]

def aiMove(b):
    if len(board.boardEmpty(b)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        player.setMove(b, x, y, board.OPLAY)
        board.printBoard(b)
    else: 
        result = miniMax(b, len(board.boardEmpty(b)), -inf, inf, board.OPLAY)
        player.setMove(b, result[0], result[1], board.OPLAY)
        board.printBoard(b)


def makeMove(b, play, mode):
    if play == board.XPLAY:
        player.playMove(b)
    else:
        aiMove(b)


def playVai():
    while True:
        try:
            order = int(input('Would you like to go first or second? (1/2) '))
            if not (order == 1 or order == 2):
                print('Please pick 1 or 2')
            else: break
        except(KeyError, ValueError):
            print('Enter a number')

    board.clearBoard(board.boarD)
    if order == 2:
        current = board.OPLAY
    else:
        current = board.XPLAY
    while not (board.boardFull(board.boarD) or end.win(board.boarD)):
        makeMove(board.boarD, current, 1)
        current *= -1
    end.printResult(board.boarD)

def setMove(b, x, y, play):
    b[x][y] = play

def playMove(b):
    temp = True
    moves = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    while temp:
        try:
            print("Pick a position between 1 and 9:\n")
            move = input(">>")
            if move < 1 or move > 9:
                print("Invalid number\n")
            elif not (moves[move] in board.boardEmpty(b)):
                print("Box filled")
            else:
                setMove(b, moves[move][0], moves[move][1], board.XPLAY)
                board.printBoard(b)
                temp = False
        except(KeyError, ValueError):
            print("Please pick a number!")