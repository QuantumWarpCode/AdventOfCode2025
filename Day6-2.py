def main():
    answer = 0
    
    #file = open("./Day6-Sample.txt")
    file = open("./Day6.txt")
    content = file.read()
    contents = content.split("\n")
    
    length = len(contents[0])
    lines = len(contents)
    #print(length)
    #print(lines)
    
    operation = ""
    currentVal = 0
    for i in range(0, length):
        currentOp = contents[-1][i]
        if currentOp == "+":
            answer += currentVal
            print(answer)
            currentVal = 0
            operation = "+"
        elif currentOp == "*":
            answer += currentVal
            print(answer)
            currentVal = 1
            operation = "*"
        
        number = 0
        for j in range(0, lines - 1):
            currentDigit = contents[j][i]
            if currentDigit != " ":
                number *= 10
                number += int(currentDigit)
        if number != 0:
            if operation == "+":
                currentVal += number
            elif operation == "*":
                currentVal *= number
            print(number, operation, currentVal)
    answer += currentVal
    
    print(answer)

main()