def checkSerial(i):
    serial = str(i)
    length = len(serial)
    check = False
    modulo = length / 2 % 1 == 0
    if modulo:
        if serial[:int(length / 2)] == serial[int(length / 2):]:
            check = True
    
    return check

def main():
    answer = 0
    
    #file = open("./Day2-Sample.txt")
    file = open("./Day2.txt")
    content = file.read()
    contents = content.split(",")
    for nrange in contents:
        rangeL = int(nrange.split("-")[0])
        rangeR = int(nrange.split("-")[1])
        print(str(rangeL) + " - " + str(rangeR))
        for i in range(rangeL, rangeR + 1):
            if checkSerial(i):
                print(i)
                answer += i
    
    print("\n" + str(answer))
    return answer

def test_main():
    assert main() == 53420042388

main()