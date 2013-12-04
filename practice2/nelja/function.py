def main():
    
    num1 = input("Give me a number: ")
    num2 = input("Another: ")
    num3 = input("Another: ")

    max3(num1,num2,num3)
    
def max3(a,b,c):
    
    if((a>b) & (a>c)):
        maxnum = a
    elif(b>c):
        maxnum = b
    else:
        maxnum = c
    
    print("The max is", maxnum)
    
main()
