def main():

    arr1 = [0,0,0]
    print("Initial state of array: ",arr1)

    i1 = eval(input("What is the first number? "))
    i2 = eval(input("What is the second number? "))
    i3 = eval(input("What is the third number? "))
    
    arr2 = [i1,i2,i3]
    print("State of array after input = ", arr2)
    
    if (i1>i2 and i1>i3):
        print("The largest number is", i1," and at location 1") 
        maxIndex = i1
        print("State of array after swap: " [i1,i2,i3])
    elif (i2>i3):
        print("The largest number is", i2," and at location 1") 
        maxIndex = i2
        i2 = i1
        i1 = maxIndex
        print("State of array after swap: ", [i1,i2,i3])
    else:
        print("The largest number is", i3," and at location 1")
        maxIndex = i3
        i3 = i1
        i1 = maxIndex
        print("State of array after swap: ", [i1,i2,i3])

    
main()
