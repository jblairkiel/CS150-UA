from random import *
from time import sleep
def main():
    print("Think of a number between 1 and 10.")
    sleep(3)
    num = guess()
    print("Is",num,"your number?")
    sleep(3)
    num = guess()
    print("Is",num,"your number?")
def guess():
    guessNum = randint(1,10)
    return guessNum
main()
