def getBeam(beam, index):
    if index > -1 and index < len(beam):
        return beam[index]
    else:
        return "."

def beam(lastBeam, newLine):
    returnLine = ""
    validSplits = 0
    for i in range(0, len(newLine)):
        char = getBeam(newLine, i)
        if char == "S":
            returnLine += "S"
        elif char == "^":
            returnLine += "^"
            if getBeam(lastBeam, i) == "|":
                validSplits += 1
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
    return returnLine, validSplits

def main():
    answer = 0
    
    #file = open("./Day7-Sample.txt")
    file = open("./Day7.txt")
    content = file.read()
    contents = content.split("\n")
    
    lastBeam = ""
    for i in range(0, len(contents[0])):
        lastBeam += "."
    
    for newLine in contents:
        #print(len(lastBeam), len(newLine))
        lastBeam, splits = beam(lastBeam, newLine)
        answer += splits
    
    print(answer)

main()