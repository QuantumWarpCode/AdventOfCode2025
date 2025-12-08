def findGreatest(bank, bMin, bMax):
    gV = -1
    gVPos = -1
    for i in range(bMin, bMax):
        if int(bank[i]) > int(gV):
            gV = bank[i]
            gVPos = i
    if int(gV) < 0:
        print(str(bMin) + " " + str(bMax) + " " + str(gV) + " " + str(gVPos))
    return gV, gVPos

def getBank(bank):
    returnString = ""
    bankLength = len(bank)
    print(bank + " " + str(bankLength))
    lastPos = -1
    digits = 12
    for i in range(1, digits + 1):
        tS, lastPos = findGreatest(bank, lastPos + 1, bankLength - (digits - i))
        returnString += str(tS)
    print(returnString)
    return int(returnString)

def main():
    answer = 0
    
    #file = open("./Day3-Sample.txt")
    file = open("./Day3.txt")
    content = file.read()
    contents = content.split("\n")
    for bank in contents:
        answer += getBank(bank)
    
    print(answer)
    return answer

def test_main():
    assert main() == 167523425665348

main()