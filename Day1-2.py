global zeros = 0

def rleft(i):
    o = i - 1
    if o == -1:
        o = 99
    if o == 0:
        #print("Zero")
        zeros += 1
    return o
    
def rright(i):
    o = i + 1
    if o == 100:
        o = 0
    if o == 0:
        #print("Zero")
        zeros += 1
    return o

def rotate(i, line):
    o = i
    if line[0] == "L":
        i = 0
        while i < int(line[1:]):
            o = rleft(o)
            i += 1
    elif line[0] == "R":
        i = 0
        while i < int(line[1:]):
            o = rright(o)
            i += 1
    else:
        print("Error, not a valid command.")
    
    return o

def main():
    r = 50
    print(r)
    print("")
    
    file = open("./Day1.txt")
    content = file.read()
    contents = content.split("\n")
    for f in contents:
        r = rotate(r, f)
        print(f + " " + str(r))
        #print("")
    print(zeros)

main()