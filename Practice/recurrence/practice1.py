def main():
    print(sum(1,5))
def sum(a,b):
    if (a == b):
        return 0 
    else:
        return a + sum(a + 1,b)
main()
