from List import*
import sys

def main():

    data = ArrayToList(sys.argv[1:])
    numbers = ListMap(int,data)
    print(smallest(numbers))

def smallest(numbers):
    
    index = 0
    spot = numbers
    smallest = head(spot)
    ismallest = 0
    while (spot != None):
        if (head(spot) < smallest):
            ismallest = index
            smallest = head(spot)
        index += 1
        spot = tail(spot)
    return smallest

main()
