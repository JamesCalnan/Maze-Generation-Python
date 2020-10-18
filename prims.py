import random, recursivebacktracker, drawing, pygame

def returnmaze(width, height, pixelArr, colour, length):

    V = []
    discovered = []
    maze = []

    availableV = recursivebacktracker.availableVertices(width, height, length)

    entry = (availableV[0][0], availableV[0][1] - int(length / 2))
    maze.append(entry)
    drawing.drawSquare(pixelArr, int(length / 2), entry[0], entry[1], colour)

    current = availableV[0]

    drawing.drawSquare(pixelArr, int(length / 2), current[0], current[1], colour)

    discovered.append(current)

    screenUpdate = 0

    maze.append(entry)
    maze.append(current)

    while True:
        pygame.event.get()

        availableVertices = recursivebacktracker.returnUnvisitedNeighbours(availableV,current,discovered,length)
        for v in availableVertices:
            if v not in V:
                V.append(v)
        if len(V) == 0:
            break

        current = V[random.randint(0, len(V) - 1)]

        drawing.drawSquare(pixelArr, int(length / 2), current[0], current[1], colour)

        visitedNeighbours = returnVisitedNeighbours(current, discovered, length)

        temp = visitedNeighbours[random.randint(0, len(visitedNeighbours) - 1)]

        wall = (int((temp[0] + current[0]) / 2), int((temp[1] + current[1]) / 2))

        drawing.drawSquare(pixelArr, int(length / 2), wall[0], wall[1], colour)

        maze.append(wall)
        maze.append(current)

        discovered.append(current)

        V.remove(current)
        if screenUpdate % 10 == 0:
            pygame.display.update()
        screenUpdate += 1

    end = (availableV[len(availableV) - 1][0], availableV[len(availableV) - 1][1] + int(length / 2))
    drawing.drawSquare(pixelArr, int(length / 2), end[0], end[1], colour)
    maze.append(end)

    return maze


def returnVisitedNeighbours(currentPoint, visited, length):
    returnList = []

    cv = (currentPoint[0] + length, currentPoint[1])
    if cv in visited:
        returnList.append(cv)

    cv = (currentPoint[0] - length, currentPoint[1])
    if cv in visited:
        returnList.append(cv)

    cv = (currentPoint[0], currentPoint[1] + length)
    if cv in visited:
        returnList.append(cv)

    cv = (currentPoint[0], currentPoint[1] - length)
    if cv in visited:
        returnList.append(cv)

    return returnList


def returnUnvisitedNeighbours(availableVertices, currentPoint, visited, length):
    returnList = []

    cv = (currentPoint[0] + length, currentPoint[1])
    if cv in availableVertices and cv not in visited:
        returnList.append(cv)

    cv = (currentPoint[0] - length, currentPoint[1])
    if cv in availableVertices and cv not in visited:
        returnList.append(cv)

    cv = (currentPoint[0], currentPoint[1] + length)
    if cv in availableVertices and cv not in visited:
        returnList.append(cv)

    cv = (currentPoint[0], currentPoint[1] - length)
    if cv in availableVertices and cv not in visited:
        returnList.append(cv)

    return returnList