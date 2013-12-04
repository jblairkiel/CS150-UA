def main():
        
    createArray()

def createArray():

    fname1 = input("Enter the first file: ")
    fname2 = input("Enter the second file: ")
    r1 = read(fname1)
    r2 = read(fname2)
    return r1,r2

def read(fname):

    fp = open(fname,'r')
    lines = fp.readlines()
    fp.close()
    return lines

def merge(records1, records2):
    final = []
    i = 0 
    j = 0 
    while (i < len(records1) and j < len(records2)):
        tokens1 = records1[i].split(",")
        tokens2 = records2[j].split(",")
        if (float(tokens1[4]) < float(tokens2[4])):
            final += [records1[i]]
            i += 1
        else:
            final += [records2[j]]
            j += 1
    return final + records1[i:] + records2[j:]

def write(records):
    fp = open("output",'w')
    for i in range

main()
