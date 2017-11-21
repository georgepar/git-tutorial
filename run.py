import sys


def add(x, y):
    return x + y

def mult(x, y):
    return float(x) * float(y)

def division(x, y):
    return mult(x, 1.0 / float(y))

def main():
    # The operation we want to perform will be passed
    # as a string in the positional command line args
    # Example: python run.py '1 + 2'
    args = sys.argv[1].strip().split()
    x, op, y = args[0], args[1], args[2]
    if op == '*':
        print(mult(x, y))

    if op == '+':
        print(add(x, y))

    if op == '/':
        print(division(x, y))


if __name__ == '__main__':
    main()
    
    
