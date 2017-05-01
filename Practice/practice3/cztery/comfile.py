from List import *
from scanner import *
import sys
import os

def main():

    for name in sys.argv[1:]:
        print(smallest(scan(name)))

def scan(name):
    s = Scanner(os.path.join(sys.path[0],name))
    a = s.readint()
    b = s.readint()
    c = s.readint()
    d = s.readint()
    s.close()
    array = [a, b, c, d]
    return array

def smallest(array):

    ismallest = array[0]
    for i in range(0, len(array), 1):
        if (array[i] < ismallest):
            ismallest = array[i]
    return ismallest
        

main()
