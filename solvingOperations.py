import pygame, drawing

def neighbours(maze, v, length):
    returnList = []

    cv = (v[0] + int(length / 2), v[1])
    if cv in maze:
        returnList.append(cv)

    cv = (v[0] - int(length / 2), v[1])
    if cv in maze:
        returnList.append(cv)

    cv = (v[0], v[1] + int(length / 2))
    if cv in maze:
        returnList.append(cv)

    cv = (v[0], v[1] - int(length / 2))
    if cv in maze:
        returnList.append(cv)

    return returnList


def backtrack(goal, root, cameFrom, pixelArr, colour, length):
    current = goal
    path = [goal]
    while not current == root:
        path.append(current)
        current = cameFrom[current]
    path.append(root)

    path.reverse()

    for v in path:
        drawing.drawSquare(pixelArr, int(length / 2), v[0], v[1], colour)
        pygame.display.update()