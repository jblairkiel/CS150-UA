from scanner import *
def main():

    s = Scanner("data.tok")
    pboolean =  s.readbool()
    pstring = s.readstring()
    pfloat = s.readfloat()
    pnumber = s.readint()
    s.close
    
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
        print("Error")


main()
