def main():

    time = eval(input("Enter the period of the pendulum(seconds)"))
    length = eval(input("Enter the wavelength of the pendulum(meters)"))
    compute(time,length)

def compute(time,length):

    f = 1 / time

    print("The frequency of the pendulum is ", f,"hertz")

    v = f * length
    
    print("The velocity of the pendulum is ", v, "m/s")

main()
