#Brian Stamm
#CSC 110 - Dr. West
#11.21.14
#Lab 9 - Advanced Strings

import os

def main(): 
    instructions()
    file_name = input("What is the name of the file we are using? ")
    file = open(file_name, 'r')
    line = file.readline()

    upper_count = 0
    total_count = 0
    lower_count = 0
    digit_count = 0
    space_count = 0

    while line != '':
        for ch in line:
            if ch.isupper() == True:
                upper_count +=1
                total_count +=1
            elif ch.islower() == True:
                lower_count +=1
                total_count+=1
            elif ch.isdigit() == True:
                digit_count+=1
                total_count+=1
            elif ch.isspace() == True:
                space_count+=1
                total_count+=1
        line=file.readline()

    upper_percent = format(((upper_count/total_count)*100),'.1f')
    lower_percent = format(((lower_count/total_count)*100),'.1f')
    digit_percent = format(((digit_count/total_count)*100),'.1f')
    space_percent = format(((space_count/total_count)*100),'.1f')
    
    print ("Upper case: ",upper_count)
    print("Upper percent: %s%%" %(upper_percent))
    print()
    print ("Lower case: ",lower_count)
    print("Lower percent: %s%%"%(lower_percent))
    print()
    print("Digits: ",digit_count)
    print("Digit percent: %s%%"%(digit_percent))
    print()
    print ("White Space: ",space_count)
    print("White Space percent: %s%%"%(space_percent))
    

    file.close()

def instructions():
    print("This program will give a total count of characters in a .txt file")
    print("Be sure to include the extension (ie - .txt) at the end of the file name.")
    print()

main()
        
