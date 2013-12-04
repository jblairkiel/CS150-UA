import random

def main():

    move = input("Choose Rock, Paper, Scissors: R, P, or S: "))
    comp = compMove()
    write(move, comp)
    
def compMove():

    arr = ['R','P','S']
    choice= random.choice(arr)
    return choice

def write():

    fp = open('moves.dat', 'w')
    fp.write(user + ' ' + comp)
    fp.close()

def read():

    tokens = []
    sc = Scanner('moves.dat')
    tokens += [sc.readtoken()]
    tokens += [sc.readtoken()]
    sc.close()
    return tokens

     
    print("The AI chose: ", compMove())    
main()
