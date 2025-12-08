def main():
    answer = 0
    
    #file = open("./Day6-Sample.txt")
    file = open("./Day6.txt")
    content = file.read()
    contents = content.split("\n")
    
    Nums1 = []
    Nums2 = []
    Nums3 = []
    Nums4 = []
    Ops = []
    
    temp = contents[0].split(" ")
    for i in temp:
        if i != "":
            Nums1.append(i)
    temp = contents[1].split(" ")
    for i in temp:
        if i != "":
            Nums2.append(i)
    temp = contents[2].split(" ")
    for i in temp:
        if i != "":
            Nums3.append(i)
    temp = contents[3].split(" ")
    for i in temp:
        if i != "":
            Nums4.append(i)
    temp = contents[4].split(" ")
    for i in temp:
        if i != "":
            Ops.append(i)
    
    #print(Nums1)
    #print(Nums2)
    #print(Nums3)
    #print(Ops)
    
    for i in range(0, len(Nums1)):
        tAnswer = 0
        if Ops[i] == "+":
            tAnswer = int(Nums1[i]) + int(Nums2[i]) + int(Nums3[i]) + int(Nums4[i])
        elif Ops[i] == "*":
            tAnswer = int(Nums1[i]) * int(Nums2[i]) * int(Nums3[i]) * int(Nums4[i])
        print(int(Nums1[i]), int(Nums2[i]), int(Nums3[i]), int(Nums4[i]), Ops[i], tAnswer)
        answer += tAnswer
    
    print(answer)
    return answer

def test_main():
    assert main() == 4805473544166

main()