#Author:  Brian Stamm
#Assignment:  1-4
#Date:  12.18.15
#Notes:  None.

def main():
    print()
    print("This will convert a Celsius temp to a Fahrenheit.  ")
    cel = int(input("What is the Celsius temperature:  "))
    
    fahr = (9/5)*cel + 32

    print("Here is the amount in Fahrenheit:  ", format(fahr, ',.1f'), sep ='')
    print()

main()
