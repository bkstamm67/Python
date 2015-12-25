#Author:  Brian Stamm
#Assignment:  1-3
#Date:  12.18.15
#Note:  None.

def main():
    tA = 15
    tB = 12
    tC = 9

    print()
    aTotal = int(input("How many 'A' tickets do you need:  "))
    bTotal = int(input("How many 'B' tickets do you need:  "))
    cTotal = int(input("How many 'C' tickets do you need:  "))

    total = (tA * aTotal) + (tB * bTotal) + (tC * cTotal)
    
    print()
    print("Total sales amount:  $", format(float(total), ',.2f'), sep ='')
    print()

main()
