import sys
def main():

    pboolean =  eval(sys.argv[1])
    pstring = sys.argv[2]
    pfloat = float(sys.argv[3])
    pnumber = int(sys.argv[4])
    
    function(pboolean,pstring,pfloat,pnumber)

def function(a, b, c, d):

    if(a == True):
        b_upper = b.upper()
        print(a)
        print(b)
        print(c)
        print(d)
        print(b_upper)
       # print('"',b,'"')
    elif(a == False):
        print(a)
        print(b)
        print(c)
        print(d)
        f = c + d
        print(2*f)
    else:
        print("Error!: Enter correct Boolean")
        


main()
