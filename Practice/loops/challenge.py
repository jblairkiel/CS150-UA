def main():
    
    lines = readFile()
    writeFile(lines)

def readFile():
    fname = input("Enter a filename: ")
    fp = open(fname, 'r')
    lines = fp.readlines()
    fp.close()
    return lines

def writeFile(data):
    fp = open('output','a')
    for i in range(0, len(data), 1):
        fp.write(str(i) + ' ' + data[i])
    fp.close() 

main()
