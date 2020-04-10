board = [[False, False, False, True, False],
         [False, True, False, True, False],
         [False, True, False, True, False],
         [False, False, False, True, False],
         [False, True, False, False, False]]
values = [[100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100]]
closedBoard = [[False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False]]
start = [4, 0]
end = [0, 4]
val = 0
current = board[start[0]][start[1]]
coords = [start[1], start[0]]
# first board dimension is y
# second board dimension is x
# coords dimensions are in order

def ShortestDistance (minDist):
    for i in board:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == False:
                    values[i][j] = (abs(j - end[1]) + abs(i - end[0]) + (abs(j - start[1]) + abs(i - start[0])))
    closedBoard[coords[1]][coords[0]] = True
    nextMove = NextMove(0)
    coords[0] = nextMove[1]
    coords[1] = nextMove[0]
    minDist += 1
    closedBoard[coords[1]][coords[0]] = True
    reversedCoords = [coords[1], coords[0]]
    if(reversedCoords != end):
        return ShortestDistance(minDist)
    else:
        return minDist

    #coords[0] = min(values[coords[0] - 1][0], values[coords[0] -2][0])

def NextMove (closestDist):
    neighbours = []
    enums = []
    distances = [[100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100]]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == False and closedBoard[i][j] == False:
                distances[i][j] = (abs(j - coords[0]) + abs(i - coords[1]))
    for i in range(len(board)):
        for j in range(len(board)):
            if distances[i][j] == 1:
                neighbours.append([i, j])
    if len(neighbours) == 0:
        return None
    endDistances = []
    for neighbour in neighbours:
        endDistances.append(abs(neighbour[1] - end[1]) + (abs(neighbour[0] - end[0])))
    for i in enumerate(endDistances):
        enums.append(i)
        closestDist = min(endDistances)
    for enum in enums:
        if closestDist == enum[1]:
            closestDist = enum[0]
    return neighbours[closestDist]

print(ShortestDistance(0))
