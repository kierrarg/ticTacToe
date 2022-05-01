XPLAY = 1
OPLAY = -1
EMPTY = 0

boarD = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

def printBoard(b):
    moves = {XPLAY: 'X', OPLAY: 'O', EMPTY: ' '}
    for x in b:
        for y in x:
            mov = moves[y]
            print(f'| {mov} |', end = ' ')
        print('\n' + '-----------------')
    print('=================')

#enumerate to return iterable 
def clearBoard(b):
    for x, row in enumerate(b):
        for y, col in enumerate(row):
            b[x][y] = EMPTY
            

def boardEmpty(b):
    emptyB = []
    for x, row in enumerate(b):
        for y, cold in enumerate(row):
            if b[x][y] == EMPTY:
                 emptyB.append([x, y])
    return emptyB



def boardFull(b):
    if len(boardEmpty(b)) == 0:
        return True
    else:
        return False