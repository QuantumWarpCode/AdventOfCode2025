def getBeam(beam, index):
    if index > -1 and index < len(beam):
        return beam[index]
    else:
        return "."

def beam(lastBeam, newLine, splits):
    returnLine = ""
    newSplits = []
    for i in splits:
        newSplits.append(i)
    for i in range(0, len(newLine)):
        char = getBeam(newLine, i)
        if char == "S":
            newSplits[i] = 1
            returnLine += "S"
        elif char == "^":
            returnLine += "^"
            newSplits[i] = 0
            if i + 1 < len(newSplits):
                newSplits[i + 1] += splits[i]
            if i - 1 > -1:
                newSplits[i - 1] += splits[i]
        elif char == ".":
            if getBeam(lastBeam, i) == "|" or getBeam(lastBeam, i) == "S":
                returnLine += "|"
            elif getBeam(lastBeam, i + 1) == "|" and getBeam(newLine, i + 1) == "^":
                returnLine += "|"
            elif getBeam(lastBeam, i - 1) == "|" and getBeam(newLine, i - 1) == "^":
                returnLine += "|"
            else:
                returnLine += "."
    print(returnLine)
    print(splits)
    return returnLine, newSplits

def main():
    answer = 0
    
    #file = open("./Day7-Sample.txt")
    file = open("./Day7.txt")
    content = file.read()
    contents = content.split("\n")
    
    lastBeam = ""
    splits = []
    for i in range(0, len(contents[0])):
        lastBeam += "."
        splits.append(0)
    
    for newLine in contents:
        #print(len(lastBeam), len(newLine))
        lastBeam, splits = beam(lastBeam, newLine, splits)
    
    for i in splits:
        answer += i
    
    print(answer)
    return answer

def test_main():
    assert main() == 53916299384254

main()