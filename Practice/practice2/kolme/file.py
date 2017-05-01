from scanner import *
import os
import sys
def main():
    
    items = scan()
    print(items)
    pboolean = items[0]
    pstring =  items[1]
    pnumber = items[2]
    
    function(pboolean,pstring,pnumber)


def scan():   

    s = Scanner(os.path.join(sys.path[0],'info.dat'))
    items = []
    token = s.readtoken()
    while (token != ""):
        items.append(token)
        token = s.readtoken()
    s.close()
    return items

def function(a, b, c):

    if(eval(a) == True):
        print(b)
        print('"',b,'"')
    elif(eval(a) == False):
        print(2*c)
    else:
        print("Error!: Enter correct Boolean")
        


main()  
