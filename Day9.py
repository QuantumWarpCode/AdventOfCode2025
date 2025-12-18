import math

def main():
    answer = 0
    
    pXs = []
    pYs = []
    
    #file = open("./Day9-Sample.txt")
    file = open("./Day9.txt")
    content = file.read()
    contents = content.split("\n")
    
    for i in contents:
        coords = i.split(",")
        pXs.append(int(coords[0]))
        pYs.append(int(coords[1]))
    
        
    for i in range(0, len(pXs)):
        for j in range(i, len(pXs)):
            print(pXs[i], pXs[j], pYs[i], pYs[j])
            area = (abs(pXs[j] - pXs[i]) + 1) * (abs(pYs[j] - pYs[i]) + 1)
            print(area)
            if area > answer:
                answer = area
    
    print(answer)
    return answer

def test_main():
    assert main() == 4777967538

main()