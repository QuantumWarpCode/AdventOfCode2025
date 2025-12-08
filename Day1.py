def rotate(i, line):
    o = i
    if line[0] == "L":
        o -= int(line[1:])
    elif line[0] == "R":
        o += int(line[1:])
    else:
        print("Error, not a valid command.")
    
    while o >= 100:
        o -= 100
    while o < 0:
        o += 100
    return o

def main():
    r = 50
    print(r)
    zeros = 0
    
    file = open("./Day1.txt")
    content = file.read()
    contents = content.split("\n")
    for f in contents:
        r = rotate(r, f)
        print(f + " " + str(r))
        if r == 0:
            zeros += 1
    print(zeros)
    return zeros

def test_main():
    assert main() == 1195

main()