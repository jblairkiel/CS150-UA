def main():

    data = eval(input("Give me an array of strings: "))

    print("The second longest string is,",secondLongest(data))

def secondLongest(data):
    
    longest = data[0]
    second = 0
    for i in range(0, len(data), 1):
        if (len(longest) < len(data[i])):
            second = longest 
            longest = data[i]
    return second

main()

           
