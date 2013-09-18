import sys

def main():
    print("The program name is: ", sys.argv[0])
    args = sys.argv[1:]
    print("Arguments:", args)

main()
