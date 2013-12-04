from time import time
import sys
sys.setrecursionlimit(10000)

def main():
    
    t1 = time()
    factIter = iterativeFact(5000)
    t2 = time()
    d = t2-t1
    print(factIter)
    print("Time duration: ",d)
    t1 = time()
    factRec = recursiveFact(5000)
    t2 = time()
    d = t2-t1
    print(factRec)
    print("Time duration: ",d)

def iterativeFact(n):
    
    res = 1
    for i in range(2,n,1):
        res *= i
    return res

def recursiveFact(n):
    
    if (n == 1):
        return n
    else: 
        return n * recursiveFact(n-1) 
main()
