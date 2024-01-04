#!/usr/bin/python3
def infinite_add(argv):
    n = len(argv) - 1
    if n == 0:
        result = 0
        print("{}".format(result))
    else:
        result = 0
        for n in range(1, n + 1):
            result += int(argv[n])
        print("{}".format(result))


if __name__ == "__main__":
    import sys
    infinite_add(sys.argv)
