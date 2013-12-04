def main():

    array = eval(input("Give me an array of numbers: "))
    print(smallest(array))

def smallest(array):

    ismallest = array[0]
    for i in range(1, len(array), 1):
        if (array[i] < ismallest):
            ismallest = array[i]
            print(ismallest)
    return ismallest


main()
