import os

def main():
    menu()

def menu():
    print("FileIO Menu:")
    print("1: Reading from a file")
    print("2: Writing to a file")
    print("3: Appending to a file")
    print("4: Delete a file")
    choice = input("Enter a choice: ")

    option(choice)

def option(c):
    if (c== '1'):
        rFile()
    elif (c== '2'):
        wFile()
    elif (c== '3'):
        aFile()
    elif (c== '4'):
        dFile()
    else:
        print("Invalid choice!")
        menu()
def cFile():
    fname1 = input("Enter the source file: ")
    fname2 = input("Enter the destination file: ")
    fpsrc = open(fname1, 'r')
    fpdest = open(fname2, 'w')
    data = fpsrc.read()
    fpdest.write(data)
    fpsrc.close()
    fpdest.close()

def rFile():
    fname = input("Enter a filename: ")
    fp =  open(fname, 'r')
    data = fp.read()
    print(data)
    fp.close()

def wFile():
    fname = input("Enter a filename:")
    fp = open(fname, 'w')
    data = input("Enter some data to write: ")
    data += '\n'
    fp.write(data)
    fp.close()

def aFile():
    fname = input("Enter a filename:")
    fp = open(fname, 'a')

main()
