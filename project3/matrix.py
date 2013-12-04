def main():
    
    displayMatrix(generateMatrix(20,30))

def generateMatrix(n,m):

    result = []
    for i in range(0,n):
        temp = []
        for j in range(0,m):
            temp.append(" ")
        result.append(temp)
    return result

def displayMatrix(matrix):
    
    for i in range(0, len(matrix), 1):
        for j in range(0 ,len(matrix[i]), 1):
            print(matrix[i][j], end = "-")
        print("\n")

main()
    

