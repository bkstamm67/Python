#Brian Stamm
#CSC 110 - Dr. West
#HW 9 - Creating Webpage
#11.25.14

import os
import sys

def main():
    instruction()
    another = 'y'                                           #Control for Looping the program
    while another == 'y' or another =='Y':
        file_name = input("What is the name of file: ")
        infile = open(file_name, 'r')
        temp_file = open('temp.txt', 'w')                   #Temp file, later to be converted to html
        html_body(infile, temp_file)                        #Function translating txt into html, passes both infile and temp_file
        new_name = rename(file_name)                        #Function changing extension to html
        print()
        print("The html file is named: ",new_name)          #Showing 'new' name
        print()
        infile.close()                                      #Closing original file
        temp_file.close()                           
        os.rename('temp.txt',new_name)                      #Closing temp file and renaming
        another = input("Would you like to translate another txt file? (Y for yes): ") #Loop for program
    closure()                                               #Closing statement
    
def instruction():  #Basic instructions
    print("Instructions")
    print()
    print("This program is designed to translate simple text files into")
    print('html files.  Be sure to include the extension at the end of')
    print('the file name when prompted.  Off we go!')
    print()

def html_body(infile, temp_file):
    line = infile.readline()#Starts reading the lines
    
    temp_file.write("<html>\n")                                         #Writes to temp
    temp_file.write("<head><title>"+line.rstrip('\n')+"</title></head>\n")#Then writes line 1 from txt for title header
    temp_file.write("<body>\n")                                             #Continuing formating for html   
    temp_file.write("<h1>"+line.rstrip('\n')+"</h1>\n")                 #Then writes next line, all for heading portion of page
    while line != '':                                           #For body of page
        line = infile.readline()
        betty=line.replace("*","<b>")                           #Replaces * for bolds, couldn't for the life of me figure out how to alternate.  Never could get a count to work
        freddy=betty.replace("_","<i>")                         #See above, same but for italic
        temp_file.write(freddy)                                 #Actually writes to temp file.  Odd names because I'm tired

    temp_file.write("\n</body>")        #Closes out the html
    temp_file.write("\n</html>")
    
def rename(file_name):
    new_name = file_name[:len(file_name)-4]+'.html' #Makes file into actual html
    return new_name

def closure():
    print("Thanks for using this program!")  #Closes program
    sys.exit()

main()
