def getCellString(grid, length, height, x, y):
    cell = grid[(x * (length)) + y]
    return cell

def getCellValue(grid, length, height, x, y):
    if x < 0 or y < 0 or x > length - 1 or y > height - 1:
        return 0
    else:
        cell = grid[(x * length) + y]
        if cell == "." or cell == "X":
            return 0
        elif cell == "@":
            return 1

def checkCell(grid, length, height, x, y):
    if getCellValue(grid, length, height, x, y) == 0:
        return "."
    else:
        nearby = 0
        nearby += getCellValue(grid, length, height, x - 1, y + 1)
        nearby += getCellValue(grid, length, height, x, y + 1)
        nearby += getCellValue(grid, length, height, x + 1, y + 1)
        nearby += getCellValue(grid, length, height, x - 1, y)
        nearby += getCellValue(grid, length, height, x + 1, y)
        nearby += getCellValue(grid, length, height, x - 1, y - 1)
        nearby += getCellValue(grid, length, height, x, y - 1)
        nearby += getCellValue(grid, length, height, x + 1, y - 1)
        if nearby < 4:
            return "X"
        else:
            return "@"

def testCheckCell(grid, length, height, x, y):
    return getCellString(grid, length, height, x, y)

def printGrid(grid, length):
    printString = ""
    for i in range(0, len(grid)):
        printString += grid[i]
        if ((i + 1) / length) % 1 == 0:
            printString += "\n"
    print(printString)

def main():
    #file = open("./Day4-Sample.txt")
    file = open("./Day4.txt")
    content = file.read()
    contents = content.split("\n")
    lastGrid = ""
    newGrid = ""
    
    height = len(contents)
    length = len(contents[0])
    
    for row in contents:
        lastGrid += row
    #print(lastGrid)
    printGrid(lastGrid, length)
    
    answer = 0
    newAnswer = 0
    growing = True
    cycles = 0
    while growing:
        x = 0
        y = 0
        newGrid = ""
        for x in range(0, length):
            for y in range(0, height):
                newVal = checkCell(lastGrid, length, height, x, y)
                newGrid += newVal
        for i in newGrid:
            if i == "X":
                answer += 1
                newAnswer += 1
        print(str(answer) + " " + str(newAnswer))
        
        if newAnswer == 0 or cycles == 3:
            growing = False
        else:
            newAnswer = 0
            lastGrid = newGrid
        #cycles += 1
    
    print("\n")
    #print(newGrid)
    printGrid(newGrid, length)
    
    
    
    print(answer)
    return answer

def test_main():
    assert main() == 8484

main()