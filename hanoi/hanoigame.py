def main():

    hanoi(3,"Left","Right","Middle")

def hanoi(n,fr,to,spare):

    if(n == 1):
        display(fr, to)
    else:
        hanoi(n-1,fr,spare,to)
        hanoi(1,fr,to,spare)
        hanoi(n-1,spare,to,fr)

def display(fr,to):
    print("  -            ")
    print(" ---           ")
    print("-----          ")
    
    print("Move ring from %s peg to %s peg." % (fr,to))

main()
    

