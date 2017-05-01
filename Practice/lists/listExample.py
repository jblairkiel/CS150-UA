from List import *

def main():

    arr = getArray()
    print(arr)

    lst = ArrayToList(arr)
    print(lst)

    srch = int(input("Enter a value to search for: "))
    val = search(srch, lst)
    print("Searching for", val, "result = ", val)
    
    doubleList = map(double, lst)
    print(doubleList)

    largest = getLargest(doubleList)
    print("The largest value is:", largest)

    smallest = getSmallest(doubleList)
    print("The smallest value is:", smallest)


def getSmallest(lst):
    
    node = lst
    min = head(node)
    while (node!= None):
        if (head(node) < min):
            min = head(node)
        node = tail(node)
    return min


def getLargest(lst):
    
    node = lst
    max = head(node)
    while (node!= None):
        if (head(node) > max):
            max = head(node)
        node = tail(node)
    return max


def map(f, lst):

    node = lst
    while (node != None):
        setHead(f(head(node)))
        node = tail(node)
    return lst
    
def double(x):

    return x * 2

def search(val, lst):
    
    node = lst
    while (node != None):
        if (head(node) == val):
            return node
        node = tail(node)
    return None

def getArray():
    
    arr = eval(input("Enter an array: "))
    return arr


main()
