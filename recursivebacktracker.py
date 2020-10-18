import random, drawing, pygame
def returnmaze(width, height, pixelArr, colour, length):
    maze = []

    availableV = availableVertices(width, height, length)

    visited = []

    stack = []

    entry = (availableV[0][0], availableV[0][1] - int(length / 2))
    maze.append(entry)
    drawing.drawSquare(pixelArr, int(length / 2), entry[0], entry[1], colour)

    current = availableV[0]
    maze.append(current)
    visited.append(current)

    drawing.drawSquare(pixelArr, int(length / 2), current[0], current[1], colour)

    updateNum = 0

    while True:
        adjacentV = returnUnvisitedNeighbours(availableV, current, visited, length)

        if len(adjacentV) > 0:
            temp = adjacentV[random.randint(0, len(adjacentV) - 1)]

            wall = (int((temp[0] + current[0]) / 2), int((temp[1] + current[1]) / 2))
            visited.append(temp)
            stack.append(temp)

            maze.append(wall)
            maze.append(temp)

            drawing.drawSquare(pixelArr, int(length / 2), wall[0], wall[1], colour)
            drawing.drawSquare(pixelArr, int(length / 2), temp[0], temp[1], colour)

            current = temp

        elif len(stack) > 0:
            current = stack.pop()
        else:
            break
        if updateNum % 5 == 0:
            pygame.display.update()
        updateNum += 1


    end = (availableV[len(availableV) - 1][0], availableV[len(availableV) - 1][1] + int(length / 2))
    drawing.drawSquare(pixelArr, int(length / 2), end[0], end[1], colour)
    maze.append(end)
    return maze


def availableVertices(width, height, length):
    returnArr = []
    for x in range(20, width - 16, length):
        for y in range(16, height - 16, length):
            # drawSquare(pixArr, 10, x, y, colour)
            # pygame.time.wait(1)
            # pygame.display.update()
            returnArr.append((x, y))
            # print("added point: " + str(x) + ", " + str(y))
    # pygame.display.update()
    return returnArr

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