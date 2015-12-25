#Author:  Brian Stamm
#Assignment:  1-2
#Date:  12.18.15
#Note:  This is me doing it.

import random

def main():
    print()
    upper = int(input("Upper bound integer number:  "))
    lower = int(input("Lower bound integer number:  "))
    print()
    for num in range(5):
        print(random.randint(lower,upper))

main()
