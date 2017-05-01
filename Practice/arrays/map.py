def main():


    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(mat)
    mat2 = map(sum,mat)
    print(mat2)

def sum(arr):

    val = 0
    for i in range(0, len(arr),1):
        val += arr[i]
    return val

def map(f,mat):
    m = []
    for i in range(0,len(mat),1):
        m += [f(mat[i])]
    return m

main()

