def main():

    data = readFile()

def writeFile():
    fp = open('output', 'w')
    for i in range(0, len(data), 1):
        fp.write('data[' + stri(i) + ']= ' + data[i])
    fp.close()

def readFile():
    fname = input("Enter a filename: ")
    fp = open(fname,'r')
    lines = fp.readlines()
    fp.close()
    return lines

def map(f, arr):
    
    result = []
    for i in range(0, len(arr), 1):
        enc = f(arr[j])
        result += [enc]
    return result

def encrypt(s):
    ret = ''
    for j in range(0, len(s), 1):
        if(s[j].isanum
        ret += rotate(s[j])
    return ret

def rotate(c):
    return chr(ord(c) + 5)
main()
