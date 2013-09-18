def main():
    
    a = input("Enter your first name:")
    b = input("Enter your last name:")

    print("Your name is",a,b)

    temp = a
    a = b
    b = temp
    
    print("Your name reversed",a,b)
main()
