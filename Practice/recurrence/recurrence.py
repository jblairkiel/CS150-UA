def main():
    
    #val = fib(20)
    #print(val)
    val2 = emult(27,32)
    print(val2)

def fib(n):
    
    if (n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

#fact(n)   is 1              if n is 1
#fact(n)   is n *fact(n-1)   otherwise recursive step

def fact(n):
    if (n == 1):
        return 1
    else:
        return n * fact(n-1)

# emult(a,b)            is          up(a,b,1)

#up(a,b,c)              is          up(a,2*b,2*c)               if c is less than a 
#up(a,b,c)              is          down(a,b,c,0)               otherwise

#down(a,b,c,d)          is          d                           if a is less than 1
#down(a,b,c,d)          is          down(a-c,b/2,c/2,d=b)       if c<=a
#down(a,b,c,d)          is          down(a,b/2,c/2,d)           otherwise

def emult(a,b):

    return up(a,b,1)

def up(a,b,c):

    if (c < a):
        return up(a,2*b,2*c)
    else:
        return down(a,b,c,0)

def down(a,b,c,d):
    
    if (a<1):
        return d
    elif (c<=a):
        return down(a-c,b/2,c/2,d=b)
    else:
        return down(a,b/2,c/2,d)

main()
