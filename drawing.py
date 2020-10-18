def printArr(listInput, pixArr, colour):
    for v in listInput:
        drawSquare(pixArr, 10, v[0], v[1], colour)

def drawSquare(pixelArr, length, x, y, colour):
    for i in range(length):
        for j in range(length):
            pixelArr[x + i][y + j] = colour