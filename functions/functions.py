def main():
    x = float(input("Enter the first value:"))
    y = float(input("Enter the second value:"))
    op = input("Enter an operation (+, -, *, %, /): ")

    if (op == '+'):
        print("The answer is %.2" %  addition(x,y))
    elif (op == '-'):
        print("The answer is", subtraction(x,y))
    elif (op == '*'):
        print("The answer is", multiplication(x,y))
    elif (op == '%'):
        print("The answer is", modulus(x,y))
    elif (op == '/'):
        print("The answer is", division(x,y))
    else:
        print("Error!")

def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b)
    return a * b
def modulus(a,b)
    return a%b
def division(a,b)
    return a/b
main()
