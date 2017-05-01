from scanner import *
import os
import scanner

def main():
    
    array = scan()
    print("The second longest string is, ", secondLongest(array))

def scan():
    
    s = Scanner(os.path.join(sys.path[0],"strings.txt"))
    array = []
    string = s.readstring()
    while(string != ""):
        array.append(string)
        string = s.readstring()
    s.close()
    return array

def secondLongest(data):
    
    longest = data[0]
    second = 0
    for i in range(0, len(data), 1):
        if (len(longest) < len(data[i])):
            second = longest
            longest = data[i]
    return second

main()
