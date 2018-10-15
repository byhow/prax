#
# Complete the 'roverMove' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER matrixSize
#  2. STRING_ARRAY cmds
#

def roverMove(matrixSize, cmds):
    # Write your code here
    l = []
    
    for i in range(matrixSize):
        j = []
        for k in range(matrixSize):
            j.append(i * matrixSize + k)
        l.append(j)

    x = 0
    y = 0
    for i in cmds:
        if (i == "RIGHT") and (y + 1 < matrixSize):
            y += 1
        elif (i == "DOWN") and (x + 1 < matrixSize):
            x += 1
        elif (i == "LEFT") and (y - 1 > -1):
            y -= 1
        elif (i == "UP") and (x - 1 > -1):
            x -= 1
    return l[x][y]   

        
        


