from List import *

def main():

    numbers = ArrayToList(eval(input("Enter an array of numbers: ")))
    print(reverse(numbers))

def reverse(items):

    return rhelper(None,items)
    
def rhelper(t,s):

    if (s == None):
        return t
    else:
        return rhelper(join(head(s),t),tail(s))

main()

