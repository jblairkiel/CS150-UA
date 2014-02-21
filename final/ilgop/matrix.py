def main():

    mat = eval(input("Give me a matrix of positive integers: "))
    compute(mat)

def compute(items):
    
    largest = sum(items[0])
    for i in range(0, len(items),1):
        for j in range(0, len(items[i]),1):
            if (largest <= sum(items[i])):
                largest = sum(items[i])
    print("The row with the largest sum has sum", largest)
    return largest
        
def sum(items):

    total = 0
    for i in range(0, len(items),1):
        total += items[i]
    return total

main()
