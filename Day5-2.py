def checkOverlap(s1, e1, s2, e2):
    # range 1 is contained in range 2
    if s1>=s2 and e1<=e2:
        return True
    # range 2 is contained in range 1
    elif s1<=s2 and e1>=e2:
        return True
    # range 2 starts during range 1
    elif s2>=s1 and s2<=e1:
        return True
    # range 1 starts during range 2
    elif s1>=s2 and s1<=e2:
        return True
    else:
        return False


def main():
    answer = 0
    rangeS = []
    rangeE = []
    rangeCount = 0
    
    #file = open("./Day5-Sample.txt")
    file = open("./Day5.txt")
    content = file.read()
    contents = content.split("\n")
    
    mode = True
    for line in contents:
        if mode:
            if line == "":
                mode = False
            else:
                thisRange = line.split("-")
                rangeS.append(int(thisRange[0]))
                rangeE.append(int(thisRange[1]))
                rangeCount += 1
                #print(line + " is a Range")
    
    #print(rangeS)
    #print(rangeE)
    
    foundOverlap = True
    while foundOverlap:
        foundOverlap = False
        newS = []
        newE = []
        newRangeCount = 0
        rangeCounted = []
        for i in range(0, rangeCount):
            rangeCounted.append(0)
        for i in range(0, rangeCount):
            foundOverlapThisRange = False
            for j in range(i + 1, rangeCount):
                if (not foundOverlapThisRange) and checkOverlap(rangeS[i], rangeE[i], rangeS[j], rangeE[j]):
                    print(rangeS[i], rangeE[i], rangeS[j], rangeE[j])
                    print("Found overlapping range", min(rangeS[i], rangeS[j]), max(rangeE[i], rangeE[j]))
                    newS.append(min(rangeS[i], rangeS[j]))
                    newE.append(max(rangeE[i], rangeE[j]))
                    rangeCounted[j] = 1
                    newRangeCount += 1
                    foundOverlap = True
                    foundOverlapThisRange = True
            if (not foundOverlapThisRange) and rangeCounted[i] == 0:
                newS.append(rangeS[i])
                newE.append(rangeE[i])
                newRangeCount += 1
        rangeS = newS
        rangeE = newE
        rangeCount = newRangeCount
        print("Combining ranges again")
        #print(rangeS)
        #print(rangeE)
    
    print(rangeS)
    print(rangeE)
    for i in range(0, rangeCount):
        answer += rangeE[i] - rangeS[i] + 1
    
    print(answer)
    return answer

def test_main():
    assert main() == 352807801032167

main()