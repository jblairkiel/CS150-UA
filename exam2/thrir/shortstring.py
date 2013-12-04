import sys
def main():

    p1 = input("Give me a string: ")
    p2 = input("Another: ")
    p3 = input("Another: ")
    
    shortest(p1,p2,p3)

def shortest(a,b,c):

    if((len(a)<len(b)) and (len(a) < len(c))):

        print("The shortest string is: ", a)

    elif(len(b)<len(c)):

        print("The shortest string is: ", b)

    else:
        print("The shortest string is: ", c)
        


main()
