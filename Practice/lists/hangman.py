import os
from List import *

def main():

    word = input("Enter a word or phrase: ")
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    underscores = map(word, underscore)
    usedLetters = []
    unusedLetters = letters
    Score = 6

    while(underscores != word):
        os.system('clear') 
        guess(letters)
        search(guess,letters)
        draw(underscores)
        print("The used letters are: ", usedLetters)

    
def map(val, f):

    ret = ' '
    for i in range(0, len(val), 1):
        if (val[i] != ' '):
            ret += f(val[i])
        else:
            ret += ' '
        return ret

def underscore(c):
    return '_'

def draw(a):
# just prints the current guessed word to the screen
    print(a) 

def guess(letters):

    p1 = input("Guess a letter: ")
    search(p1, letters) 

def search(val , lst):

    node = lst
    while (node != None):
        if(head(node) == val):
            node = tail 
            guessRight(val)
            return node
        elif (node == " "):
            guessWrong(val)
    return None

def guessWrong(val):

    append.val(usedLetters)
    Score -1

def guessRight(val):

    append.lst(unusedLetters)
    append.val(usedLetters)

main()
