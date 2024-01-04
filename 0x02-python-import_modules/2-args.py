#!/usr/bin/python3
def print_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{} argument.".format(n))
        return
    else:
        if n == 1:
            print("{} argument:".format(n))
        else:
            print("{} arguments:".format(n))
        for n in range(n + 1):
            print("{}: {}".format(n, argv[n]))

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
