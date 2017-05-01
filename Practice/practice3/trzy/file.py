from scanner import *
import sys
import os

def main():

    array = scan()
    print(smallest(array))     

def scan():

    s = Scanner(os.path.join(sys.path[0],"data.txt"))
    a = s.readint()
    b = s.readint()
    c = s.readint()
    d = s.readint()
    s.close
    array = [a, b, c, d]
    return array

def smallest(array):

    ismallest = 0
    for i in range(1, len(array), 1):
        if (array[i] < array[ismallest]):
            ismallest = i
    return array[ismallest]



main()


