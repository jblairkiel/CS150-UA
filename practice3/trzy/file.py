from scanner import *

def main():

    array = scan()
    print(smallest(array))     

def scan():

    s = Scanner("data.txt")
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
        if (array[i] > array[ismallest]):
            ismallest = array[i]
        else:
            ismallest = 
    return ismallest



main()


