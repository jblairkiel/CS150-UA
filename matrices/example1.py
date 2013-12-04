def main():
`
    arr = [[1,2,3],[4,5,6],[7,8,9]]

    # Iterating over the rows
    for i in range(0,len(arr),1):

    # Iterating over the columns
        for j in range(0,len(arr[i]),1):

            print(arr[i][j], end= ' ')
        print()

    sums = sumOfColumns(arr)
    print("Sums:", sums)
    Diag = sumDiag(arr)
    print(Diag)

def sumOfColumns(arr):
    
    sums = []
    for j in range(0, len(arr), 1):
        s = 0
        for i in range(0, len(arr), 1):
            s += arr[i][j]
        sums += [s]

def sumDiag(arr):
    
    i = 0
    while(i<len(arr)):
        s = 0
        j = 0
        while(j<len(arr[i])):
            if(i ==j):
                s += arr[i][j]
            j+=1
        i+=1



main()
