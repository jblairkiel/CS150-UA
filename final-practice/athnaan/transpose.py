from scanner import *
import sys

def main():

    m = sys.argv[1]
    rows = eval(sys.argv[2])
    cols = eval(sys.argv[3])

    print("The original matrix is:", originalMatrix(m,rows,cols))
    print("The transposed matrix is:", transposeMatrix(m,rows,cols))
    
def originalMatrix(m,rows,cols):

    s = Scanner(m)
    array = []
    for i in range(0,rows,1):
        for j in range(0,cols,1):
            m[i][j] = s.readint()
            print(m[j][i], end='')
        print()
    return

def transposeMatrix(m,rows,cols):
    
    for j in range(0,cols,1):
        for i in range(0,rows,1):
            print(m[j][i], end='')
        print()
    return

main()

    
