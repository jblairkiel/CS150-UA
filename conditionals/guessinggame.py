import random
def main():

    print("Guessing Game!")
    y = eval(input("Guess a number 1-10: "))
    x = makenumber()
    while(x != y):
        if(y<x):
             print("Guess Higher!")
        elif(y>x):
             print("Guess Lower!")
    if(x == y):
        print("You guessed correctly! : ",y)

def makenumber():

    return random.randrange(10)


    
    
main()
