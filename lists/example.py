from List import *

def main():

    lst = EnumerateList(0,20,2)
    print(lst)
    lstRec = EnumerateList(0,20,2)
    print(lstRec)

def EnumerateList(low, high, step):

    lst = NodeCreate(low, None)
    node = lst
    count = low + step
    while ( count < high):
        nextNode = NodeCreate(count, None)
        NodeSetNext(node, nextNode)
        count += step
        node = nextNode
    return lst

def EnumerateListRec(low, high, step):

    if (low >= high):
        return None
    else:
        return NodeCreate(low,EnumerateListRec(low+step, high, step))




main()
