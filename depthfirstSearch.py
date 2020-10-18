import drawing, solvingOperations, pygame

def solvemaze(maze, pixelArr, colour1, colour2, length):
    root = maze[0]
    goal = maze[len(maze) - 1]

    discovered = []
    S = []
    cameFrom = {}

    S.append(root)

    while len(S) > 0:
        pygame.event.get()
        v = S.pop()

        drawing.drawSquare(pixelArr, int(length / 2), v[0], v[1], colour1)
        pygame.display.update()

        if v == goal:
            solvingOperations.backtrack(goal, root, cameFrom, pixelArr, colour2, length)
            break

        if not (v in discovered):

            discovered.append(v)

            for w in solvingOperations.neighbours(maze, v, length):
                if w in discovered: continue
                S.append(w)
                cameFrom[w] = v