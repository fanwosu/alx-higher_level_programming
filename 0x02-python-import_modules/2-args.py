#!/usr/bin/python3
import sys
def print_arguments():
    num_arguments = len(argv) - 1
    print(f"Number of argument(s): {num_arguments}", end="")
    if num_arguments == 0:
        print(".")
    else:
        print(":")
        for i in range(num_arguments):
            print(f"{i + 1}: {argv[i + 1]}")

if __name__ == "__main__":
    print_arguments()
