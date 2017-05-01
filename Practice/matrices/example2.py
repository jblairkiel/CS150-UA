import sys

def main():
    
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    mode = sys.argv[3]
    # Mode = 'recursive' or 'iterative'
    mode = sys.argv[3]
    mat = createMatrix(rows,cols,mode)
    print(mat)

def createMatrix(r,c,m):
    
    if (m == 'recursive'):
        return recursiveMatrix(r,c)
    elif (m == 'iterative'):
        return iterativeMatrix(r,c)
    else:
        print("ERROR!")
        return

def iterativeMatrix(r,c):

    mat = []
    for i in range(0,r,1):
        mat += [iterativeRow(c)]
    return mat

def iterativeRow(c):
    
    row = []
    for i in range(0,c,1):
        row += [0]
    return row

def recursiveMatrix(r,c):
    
    if (r == 0):
        return mat
    else:
        row = recursiveRow(c,[])
        return  recursiveMatrix(rows-1,cols,mat+[row])

def recursiveRow(c,arr):

    if(c ==0):
        return arr
    else:
        return recursiveRow(c-1,arr+[0])
    
    



main()
