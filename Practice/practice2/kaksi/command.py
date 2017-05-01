import sys
def main():
    
    pboolean = eval(sys.argv[1])
    pstring = sys.argv[2]
    pnumber = int(sys.argv[3])
    
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
