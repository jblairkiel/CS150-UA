from List import *
from scanner import *
import sys

def main():

    name = sys.argv[1:]
    smallest(scan(name))

def scan(name):

    s = Scanner(name)
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
