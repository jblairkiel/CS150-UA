from scanner import *

def main():
    fname = input("Enter a filename: ")
    sc = Scanner(fname)

    print("0 - Tokens")
    print("1 - Integers")
    print("2 - Floats")
    c - input("Enter a choice: ")

    if (c == '0'):
        tokens = readTokens(sc)
    elif (c == '1'):
        tokens = readIntegers(sc)
    elif (c =='2'):
        tokens = readFloats(sc)
    else:
        print("Error")
        main()

    tokens = readTokens(sc)

    

def readTokens(sc)
    arr = []
    arr += [sc.readtoken()]
    arr += [sc.readtoken()]
    arr += [sc.readtoken()]
    arr += [sc.readtoken()]
    return arr

def readIntegers(sc):
   arr = []
   arr += [sc.readint()]
   arr += [sc.readint()]
   arr += [sc.readint()]
   arr += [sc.readint()]
  return arr 

def readFloats(sc):
   arr = []
   arr += [sc.readfloat()]
   arr += [sc.readfloat()]
   arr += [sc.readfloat()]
   arr += [sc.readfloat()]
  return arr 
