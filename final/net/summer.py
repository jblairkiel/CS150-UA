from List import *
def main():

    items = eval(input("Give me a list: "))
    print("The sum of the list is: ",sum(items))

def sum(items):

    return helper(0,items)

def helper(result,items):

    if(items == None):
        return result
    else:
        return helper(result + head(items),tail(items))

main()
    
