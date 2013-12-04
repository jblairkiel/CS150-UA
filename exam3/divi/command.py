import sys
from List import *

def main():
    
    strings = ArrayToList(sys.argv[1:])
    print("The second longest string is, ",secondLongest(strings))

def secondLongest(data):

    longest = head(data)
    second = 0
    while (data != None):
        if (len(head(data)) > len(longest)):
            second = longest
            longest = head(data)
        data = tail(data)
    return second

main()
