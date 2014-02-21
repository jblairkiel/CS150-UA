import sys
from scanner import *

def main():

    f = sys.argv[1]
    evaluate(scan(f))
    
def scan(name):

    s = Scanner(name)
    num = []
    token = s.readfloat()
    while (token != ""):
            num.append(token)
            token = s.readfloat()
    s.close
    return num

def evaluate(name):

    largest = name[0]
    for i in range(0, len(name), 1):
        if( name[i] > largest):
            largest = name[i]
    print("The highest number is ", largest)

main()
