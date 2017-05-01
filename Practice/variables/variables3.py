def main():
    a = int(input("Give me an integer:"))
    b = float(input("Give me a float:"))

    resultA = a/b
    print(resultA)

    c = str(b)
    resultC = c*a
    print(resultC)

    a = a + 1
    print("New value of a:",a)

    b += 1
    print("New value of b:",b)

    a = a - 1

    b*= 100

main()
