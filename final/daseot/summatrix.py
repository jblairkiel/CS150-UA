import sys
def main():
    
    matrix = eval(sys.argv[1])
    compute(matrix)
    pi(matrix)

def compute(matrix):
    
    count = sum(matrix[0]) 
    for i in range( 1, len(matrix), 1):
        count += matrix[i][len(matrix[i]) - 1]
    print("The sum of the first row and last column is",count)

def sum(items):
    
    total = 0
    for i in range(0, len(items),1):
        total += items[i]
    return total
    
def pi(matrix):

    count = 0
    for i in range(0, len(matrix), 1):
        for j in range(0, len(matrix[i]),1):
            if ( (matrix[i][0] * matrix[i][1]) <= 1):
                count += 1
            pi = (count / len(matrix)) * 4
            print(pi)
main()
