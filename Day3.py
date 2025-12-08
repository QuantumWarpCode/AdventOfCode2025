def getBank(bank):
    gV = -1
    gVPos = -1
    sgV = -1
    sgVPos = -1
    bankLength = len(bank)
    print(bank + " " + str(bankLength))
    for i in range(0, bankLength - 1):
        #print(bank[i])
        if int(bank[i]) > int(gV):
            gV = bank[i]
            gVPos = i
        #print(bank[bankLength - i:])
    for i in range(gVPos + 1, bankLength):
        if int(bank[i]) > int(sgV):
            sgV = bank[i]
            sgVPos = i
    print(gV + sgV)
    return int(gV+sgV)

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
    assert main() == 16842

main()