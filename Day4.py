def getCellString(grid, length, height, x, y):
    if grid[y][x] == ".":
        return "."
    elif grid[y][x] == "@":
        return "@"

def getCellValue(grid, length, height, x, y):
    if x < 0 or y < 0 or x > length - 1 or y > height - 1:
        return 0
    elif grid[y][x] == ".":
        return 0
    elif grid[y][x] == "@":
        return 1

def checkCell(grid, length, height, x, y):
    if getCellString(grid, length, height, x, y) == ".":
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

def main():
    answer = 0
    
    #file = open("./Day4-Sample.txt")
    file = open("./Day4.txt")
    content = file.read()
    contents = content.split("\n")
    newGrid = ""
    
    height = len(contents)
    length = len(contents[0])
    
    x = 0
    y = 0
    for row in contents:
        for column in row:
            newVal = checkCell(contents, length, height, x, y)
            newGrid += newVal
            x += 1
        x = 0
        y += 1
        newGrid += "\n"
    
    for row in contents:
        print(row)
    print("\n")
    print(newGrid)
    
    for i in newGrid:
        if i == "X":
            answer += 1
    
    print(answer)
    return answer

def test_main():
    assert main() == 1467

main()