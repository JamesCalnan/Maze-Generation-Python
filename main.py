import pygame, recursivebacktracker, Astar, breadthfirstSearch, depthfirstSearch, prims

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

width = 800
height = 800

length = 26

gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(black)

pixArr = pygame.PixelArray(gameDisplay)


while True:

    gameDisplay.fill(black)
    maze = prims.returnmaze(width, height, pixArr, white, length)

    breadthfirstSearch.solvemaze(maze, pixArr, red, green, length)

    pygame.time.wait(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:

            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            #else:


