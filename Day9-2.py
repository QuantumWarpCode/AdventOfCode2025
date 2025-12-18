import math

def searchRow(row, x):
    leftB = False
    rightB = False
    for i in range(0, len(row)):
        if i < x and row[i] == "#":
            leftB = True
        elif i > x and row[i] == "#":
            rightB = True
    if leftB and rightB:
        return True
    else:
        return False

def searchRowB(row, x):
    leftB = False
    rightB = False
    for i in range(0, len(row)):
        if i < x and (row[i] == "#" or row[i] == "X"):
            leftB = True
        elif i > x and (row[i] == "#" or row[i] == "X"):
            rightB = True
    if leftB and rightB:
        return True
    else:
        return False

def searchColumn(grid, x, y):
    topB = False
    bottomB = False
    for i in range(0, len(grid)):
        if i < y and grid[i][x] == "#":
            topB = True
        elif i > y and grid[i][x] == "#":
            bottomB = True
    if topB and bottomB:
        return True
    else:
        return False

def searchColumnB(grid, x, y):
    topB = False
    bottomB = False
    for i in range(0, len(grid)):
        if i < y and (grid[i][x] == "#" or grid[i][x] == "X"):
            topB = True
        elif i > y and (grid[i][x] == "#" or grid[i][x] == "X"):
            bottomB = True
    if topB and bottomB:
        return True
    else:
        return False

def checkArea(grid, x1, x2, y1, y2):
    DEBUG = False
    #if x1 == 11 and x2 == 2 and y1 == 1 and y2 == 5:
    #    print("DEBUG ME!")
    #    DEBUG = True
    
    
    if x1 == x2 and y1 == y2:
        return False
    
    if x1 > x2:
        x1, x2 = x2, x1
    
    if y1 > y2:
        y1, y2 = y2, y1
    
    if DEBUG:
        print(range(x1, x2))
        print(range(y1, y2))
    
    printTest = ""
    for j in range(y1, y2 + 1):
        for i in range(x1, x2 + 1):
            printTest += grid[j][i]
            if grid[j][i] == ".":
                if DEBUG:
                    print(printTest)
                return False
        printTest += "\n"
    if DEBUG:
        print(printTest)
    return True

def main():
    answer = 0
    
    pXs = []
    pYs = []
    
    #file = open("./Day9-Sample.txt")
    file = open("./Day9.txt")
    content = file.read()
    contents = content.split("\n")
    
    print("Getting points...")
    maxX = 0
    maxY = 0
    for i in contents:
        coords = i.split(",")
        pXs.append(int(coords[0]))
        pYs.append(int(coords[1]))
        if int(coords[0]) > maxX:
            maxX = int(coords[0])
        if int(coords[1]) > maxY:
            maxY = int(coords[1])
    
    print("Making grid...")
    grid = []
    for i in range(0, maxY + 2):
        row = []
        for j in range(0, maxX + 2):
            row.append(".")
        grid.append(row)
    
    # Add Red tiles
    print("Adding red tiles...")
    for i in range(0, len(pXs)):
        #print([pYs[i]],[pXs[i]])
        grid[pYs[i]][pXs[i]] = "#"
    
    # Add Green tiles in lines
    print("Adding green tiles...")
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == ".":
                if searchRow(grid[i], j):
                    grid[i][j] = "X"
                elif searchColumn(grid, j, i):
                    grid[i][j] = "X"
    
    # Fill Green tiles
    print("Filling green tiles...")
    newGrid = grid
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == ".":
                if searchRowB(grid[i], j) and searchColumnB(grid, j, i):
                    newGrid[i][j] = "X"
    
    #for row in grid:
    #    rowText = ""
    #    for letter in row:
    #        rowText += letter
    #    print(rowText)
        
    # Find max area
    for i in range(0, len(pXs)):
        for j in range(i + 1, len(pXs)):
            check = checkArea(grid, pXs[i], pXs[j], pYs[i], pYs[j])
            #print(check)
            if check:
                #print("Tested good.", pXs[i], pXs[j], pYs[i], pYs[j])
                area = (abs(pXs[j] - pXs[i]) + 1) * (abs(pYs[j] - pYs[i]) + 1)
                print(area)
                if area > answer:
                    answer = area
    
    print(answer)
    return answer

def test_main():
    assert main() == "false"

main()