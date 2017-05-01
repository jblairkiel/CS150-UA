def main():

    print(tester([1,2,3,4,5]))

def tester(items):
    if (len(items) == 0):
        return 0
    return 1 + tester(items[1:])

main()
