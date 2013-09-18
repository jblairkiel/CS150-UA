def main ():
    menu()   


def menu ():
    print("Stacks and Queues!\n")
    myArray = eval(input("Enter an array:"))
    print("\n0: Stack")
    print("1: Queue")

    choice = input("Enter in your choice:")

    if (choice == '0'):
        stack(myArray, choice)
    elif (choice == '1'):
        queue(myArray, choice)
    else:
        print("Error!")
        menu()


def stack(arr, c):
    print("\nInitial Stack:", arr)
    print("Length of Stack:", len(arr))
    push(arr)
    print("\nStacck after pushing:",arr)
    print("New length of stack:", len(arr))
    push(arr)
    print("\nInitial Stack:", arr)
    print("Length of Stack:", len(arr))
    pop(arr, c)
    pop(arr, c)
    pop(arr, c)
    print("\nStack after pop: ", arr)
    print("Length of Stack: ", len(arr))


rChoice()

def queue(arr,c):
    print("\nInitial Queue:",arr)
    print("\nLength of Queue:", len(arr))
    push(arr)
    print("\nInitial Queue:",arr)
    print("\nLength of Queue:", len(arr))
    push(arr)
    print("\nInitial Queue:",arr)
    print("\nLength of Queue:", len(arr))
    pop(arr, c)
    pop(arr, c)
    pop(arr, c)
    print("\nQueue after pop:", arr)
    print("Length of Queue: ", len(arr))

rChoice()
 
def push(arr):
    item = eval(input("Item to push: "))
    arr.append(item)
    
def pop(arr,c):
    if (c == '0'):
        arr.pop()
    else:
        del arr[0]

def rChoice():
    rC = input("\n1 for menu, else terminate:")
    if (rC == "1"):
        menu()
    else:
        print("Exiting program.\n")

main()
