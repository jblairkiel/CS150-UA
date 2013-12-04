from scanner import *
def main():
    
    pboolean = items[0]
    pstring =  items[1]
    pnumber = items[2]
    
    function(pboolean,pstring,pnumber)


def scan(info):   

    s = Scanner(info.dat)
    items = []
    token = s.readtoken()
    while (token != " "):
        items.append(token)
        token = s.readtoken()
    s.close()
    return items

def function(a, b, c):

    if(a == True):
        print(b)
        print('"',b,'"')
    elif(a == False):
        print(2*c)
    else:
        print("Error!: Enter correct Boolean")
        


main()  
