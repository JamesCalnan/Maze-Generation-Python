import drawing, solvingOperations, pygame

def solvemaze(maze, pixelArr, colour1, colour2, length):
    Q = []
    discovered = []
    cameFrom = {}

    root = maze[0]
    goal = maze[len(maze) - 1]

    discovered.append(root)
    Q.append(root)

    while len(Q) > 0:
        pygame.event.get()
        v = Q.pop(0)

        drawing.drawSquare(pixelArr, int(length / 2), v[0], v[1], colour1)
        pygame.display.update()

        if v == goal:
            solvingOperations.backtrack(goal, root, cameFrom, pixelArr, colour2, length)
            break

        for w in solvingOperations.neighbours(maze, v, length):
            if w in discovered:
                continue
            discovered.append(w)
            cameFrom[w] = v
            Q.append(w)