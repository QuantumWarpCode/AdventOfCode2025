def main():
    answer = 0
    rangeS = []
    rangeE = []
    IDs = []
    
    #file = open("./Day5-Sample.txt")
    file = open("./Day5.txt")
    content = file.read()
    contents = content.split("\n")
    
    mode = True
    for line in contents:
        if line == "":
            mode = False
        elif mode:
            thisRange = line.split("-")
            rangeS.append(int(thisRange[0]))
            rangeE.append(int(thisRange[1]))
            #print(line + " is a Range")
        else:
            IDs.append(int(line))
            #print(line + " is an ID")
    
    #print(rangeS)
    #print(rangeE)
    #print(IDs)
    
    for test in IDs:
        counted = False
        for i in range (0, len(rangeS)):
            if counted == False:
                if test >= rangeS[i] and test <= rangeE[i]:
                    print(str(test) + " is in range from " + str(rangeS[i]) + "-" + str(rangeE[i]))
                    counted = True
                    answer += 1
    print(answer)

main()