def main():

    string = input("Give me a string of parenthesis")
    checkParens(string)

def checkParens(items):

    print("Balanced?",helper(items))

def helper(items):

    if(len(items) == 1):
        return False
    elif(len(items) == 2):   
        if (items[:-1] == "(" and items[1:] == ")"):
            return True
        else:
            return False
    else:
        if (items[:-1] == "(" and items[1:] == ")"):
            return helper(items[1:-1])
        else:
            return False

main()
