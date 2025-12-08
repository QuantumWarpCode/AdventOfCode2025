def rleft(i):
    zeros = 0
    o = i - 1
    if o == -1:
        o = 99
    if o == 0:
        #print("Zero")
        zeros += 1
    return o, zeros
    
def rright(i):
    zeros = 0
    o = i + 1
    if o == 100:
        o = 0
    if o == 0:
        #print("Zero")
        zeros += 1
    return o,zeros

def rotate(i, line):
    zeros = 0
    newzeros = 0
    o = i
    if line[0] == "L":
        i = 0
        while i < int(line[1:]):
            o, newzeros = rleft(o)
            zeros += newzeros
            i += 1
    elif line[0] == "R":
        i = 0
        while i < int(line[1:]):
            o, newzeros = rright(o)
            zeros += newzeros
            i += 1
    else:
        print("Error, not a valid command.")
    
    return o, zeros

def main():
    zeros = 0
    newzeros = 0
    r = 50
    print(r)
    print("")
    
    file = open("./Day1.txt")
    content = file.read()
    contents = content.split("\n")
    for f in contents:
        r, newzeros = rotate(r, f)
        zeros += newzeros
        print(f + " " + str(r))
        #print("")
    print(zeros)
    return zeros

def test_main():
    assert main() == 6770

main()