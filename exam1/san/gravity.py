def main():

    time = int(input("amount of time falling?"))
    vt = time*-9.81
    print("velocity at time", time," :", vt)
    position = .5* -9.81* time* time
    print("position at time", time," :", position)
    position2 = .5* -9.81* time* time -50
    return

main()
