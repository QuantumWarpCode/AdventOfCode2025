def checkSerial(i):
    serial = str(i)
    length = len(serial)
    check = False
    for tLength in range(1, length):
        modulo = length / tLength % 1 == 0
        if modulo:
            sections = [serial[i:tLength + i] for i in range(0, length, tLength)]
            if len(set(sections)) == 1:
                #print(str(sections) + " " + str(tLength))
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
    
    #for i in range(9999, 10001):
    #    if checkSerial(i):
    #       answer += i

main()