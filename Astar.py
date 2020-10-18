import math, pygame, solvingOperations, drawing

def extractMin(openSet, fScore):
    sortedDict = sorted(fScore.items(), key=lambda  t:t[1])

    for i in range(len(sortedDict)):
        if sortedDict[i][0] in openSet:
            return sortedDict[i][0]

def h(current, goal, heuristic):
    return float((math.fabs(current[0] - goal[0]) + math.fabs(current[1] - goal[1])) * heuristic)


def solvemaze(maze, pixelArr, colour1, colour2, length):
    heuristic = 1.6

    openSet = []

    cameFrom = {}

    gScore = {}
    fScore = {}

    max = 999999

    for v in maze:
        gScore[v] = max
        fScore[v] = max

    root = maze[0]
    goal = maze[len(maze) - 1]

    gScore[root] = 0
    fScore[root] = h(root, goal, heuristic)

    openSet.append(root)

    while len(openSet) > 0:
        pygame.event.get()
        current = extractMin(openSet, fScore)

        drawing.drawSquare(pixelArr, int(length / 2), current[0], current[1], colour1)
        pygame.display.update()

        if current == goal:
            solvingOperations.backtrack(goal, root, cameFrom, pixelArr, colour2, length)
            break

        openSet.remove(current)

        for neighbour in solvingOperations.neighbours(maze, current, length):
            tentative_gScore = gScore[current] + 10

            if tentative_gScore <= gScore[neighbour]:
                cameFrom[neighbour] = current
                gScore[neighbour] = tentative_gScore
                fScore[neighbour] = gScore[neighbour] + h(neighbour, goal, heuristic)

                if not neighbour in openSet:
                    openSet.append(neighbour)