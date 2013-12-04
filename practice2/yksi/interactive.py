def main():
    
    pboolean =  eval(input("Give me a Boolean: "))
    pstring = input("Give me a String: ")
    pnumber = int(input("Give me a number: "))
    
    function(pboolean,pstring,pnumber)

def function(a, b, c):

    if(a == True):
        print(b)
        print('"',b,'"')
    elif(a == False):
        print(2*c)
    else:
        print("Error!: Enter correct Boolean")
        


main()
