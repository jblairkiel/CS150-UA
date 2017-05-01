def main():
    

def f(a):
    if(a == None):
        return 1
    elif(isEven(head(a))):
        return head(a) + f(tail(a))
    else:
        return f(tail(a))

main():
