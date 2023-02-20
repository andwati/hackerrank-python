#!/bin/python3

import sys


if __name__ == "__main__":
    n = int(input("Enter the number: ").strip())
    if not (n > 1 and n <= 100):
        print("The number is not between 0 and 100.Please try again")
        sys.exit()

    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")

    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
