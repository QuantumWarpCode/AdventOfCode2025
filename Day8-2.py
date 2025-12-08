import math

def getDist(x1, y1, z1, x2, y2, z2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))

def hasMultipleCircuits(circuits):
    firstCircuit = circuits[0]
    for i in range(1, len(circuits)):
        if circuits[i] != firstCircuit:
            return True
    return False

def main():
    answer = 0
    
    xVs = []
    yVs = []
    zVs = []
    circuits = []
    
    dists = []
    distP1 = []
    distP2 = []
    
    #file = open("./Day8-Sample.txt")
    file = open("./Day8.txt")
    content = file.read()
    contents = content.split("\n")
    
    ccount = 0
    for i in contents:
        coords = i.split(",")
        xVs.append(int(coords[0]))
        yVs.append(int(coords[1]))
        zVs.append(int(coords[2]))
        circuits.append(ccount)
        ccount += 1
    
    for i in range(0, len(xVs)):
        for j in range(i + 1, len(xVs)):
            distP1.append(i)
            distP2.append(j)
            dists.append(getDist(xVs[i], yVs[i], zVs[i], xVs[j], yVs[j], zVs[j]))
    
    maxDist = 0
    maxDistP = -1
    for i in range(0, len(dists)):
        if dists[i] > maxDist:
            maxDist = dists[i]
            maxDistP = i
    
    #for count in range(0, 10):
    #for count in range(0, 1000):
    minDistP1 = -1
    minDistP2 = -1
    while hasMultipleCircuits(circuits):
        minDist = maxDist
        minDistP = maxDistP
        for i in range(0, len(dists)):
            if dists[i] != 0 and dists[i] < minDist:
                minDist = dists[i]
                minDistP = i
        minDistP1 = distP1[minDistP]
        minDistP2 = distP2[minDistP]
        print(minDist, minDistP)
        print(xVs[minDistP1], yVs[minDistP1], zVs[minDistP1])
        print(xVs[minDistP2], yVs[minDistP2], zVs[minDistP2])
        if circuits[minDistP1] != circuits[minDistP2]:
            replaceCircuit = circuits[minDistP2]
            for i in range(0, len(circuits)):
                if circuits[i] == replaceCircuit:
                    circuits[i] = circuits[minDistP1]
        dists[minDistP] = 0
        print(circuits)
    
    answer = xVs[minDistP1] * xVs[minDistP2]
    
    print(answer)
    return answer

def test_main():
    assert main() == 7017750530

main()