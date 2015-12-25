#Brian Stamm
#CSC - 110, Dr. West
#Howework 8 - Encryption/Decryption
#11.18.14

import sys
import os

INSTRUCTION_CHOICE = 1  #GLOBAL CHOICES
DECRYPT_CHOICE = 2
ENCRYPT_CHOICE = 3
QUIT_CHOICE = 4

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!?,\'\";:-'  #GLOBAL LIST - contains all letters/numbers/symbols encrypted

def main():
    my_key = 'HIJKLMNOPQRSTUVWXYZ0123456789.!?,\'\";:-abcdefghijklmnopqrstuvwxyzABCDEFG' #KEY for LETTERS
    choice = 0
    pre_instruction(my_key) #Instructing on menu selection, also contains check to make sure my_key and LETTERS line up accurately

    while choice != QUIT_CHOICE:  #MENU Loop
        display_menu()

        choice = int(input("Enter the number of your choice: "))

        if choice == INSTRUCTION_CHOICE:
            print()
            instruction()
        elif choice == DECRYPT_CHOICE:
            print()
            decrypt(my_key)
        elif choice == ENCRYPT_CHOICE:
            print()
            encrypt(my_key)
        elif choice == QUIT_CHOICE:
            closure()
            sys.exit()
        else:
            print("Sorry, I didn't understant that.  Please try again.")
            print()
            
def pre_instruction(key):
    print("Welcome to Little Orphan Annie's Encrpytion Program, brought to you by Ovaltine.")
    print("Be sure to pick one of the numbers from the menu:")
    keyList = list(key)   #Following checks to ensure both LETTERS and my_list have all same characters within it.  if not, shuts down.
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print("There's an error with the program's key.  Please contact Olvatine.")
        sys.exit()
    else:
        print()

def instruction():  #Detailed instructions
    print("This program is designed to either encrypt a simple text file,")
    print("or it will decrypt a file it has encrypted.  It uses a special key designed")
    print("only for this program, so it cannot decipher a code it does not have the key for.")
    print()
    print("A menu will display various options.  Currently, you are in the \"Detailed")
    print("Instructions\" Section.  In the \"Decrypt file\", it will walk you through")
    print("how to decrypt a selected file.  The \"Encrypt file\" will help with encrypting.")
    print()
    print("After either encrypting or decrypting the file, this program creates a new")
    print("file in the same folder as the initial program.  To help distinguish from")
    print("the original, the new file will either have a 'E' at the end of the file")
    print("named for \"Encrypted,\", or 'D' for \"Decrypted.\"")
    print()
    print("Be sure when you are asked to write the file name, be sure to to put the")
    print("extention at the end as well.  For example, if your file is named \"Program\",")
    print("you will need to remember to write out \"Program.txt\"") 
    print()
    print("That's all for now!  Back to the menu -")
    print()

def display_menu(): #Displays menu
    print("Display menu:")
    print()
    print("1) Detailed Instructions")
    print("2) Decrypt file")
    print("3) Encrypt file")
    print("4) Quit")
    print('')

def decrypt(my_key): #Decyption
    file_name = input("What is the name of the file we are decrypting, with extension? ")
    infile = open(file_name, 'r')
    temp_file = open('temp.txt', 'w') #Creates temp file
    new_name = rename_d(file_name)  #Function to create new name for decrypted file, with D at end
    line = infile.readline()
    while line != '':
        temp_file.write(line.translate({ord(x):y for (x,y) in zip(my_key,LETTERS)})) #LOOP that deciphers (same in Encryption, but my_key and LETTERS flipped
        line=infile.readline() 
    infile.close()
    temp_file.close()
    os.rename('temp.txt', new_name) #Renames the temp file as something permnament

def encrypt(my_key): #Encryption, same as previous, except
    file_name = input("What is the name of the file we are encrpyting, with extension? ")
    infile = open(file_name, 'r')
    temp_file = open('temp.txt', 'w')
    new_name = rename_e(file_name) #HERE, different function used for naming the file
    line = infile.readline()
    while line != '':
        temp_file.write(line.translate({ord(x):y for (x,y) in zip(LETTERS,my_key)}))  #And here, loop is basically same, except LETTERS and my_key are flipped
        line=infile.readline()
    infile.close()
    temp_file.close()
    os.rename('temp.txt', new_name)

def rename_d(file): #Creates new file name for DECRYPTION
    new_name = file[0:(len(file)-4)]+'D.txt'
    print("Your decrypted file is named: ",new_name)
    print("And back to the main menu.")
    print()
    return new_name

def rename_e(file): #Creates new file name for ENCRYPTION
    new_name = file[0:(len(file)-4)]+'E.txt'
    print("Your encrypted file is named: ",new_name)
    print("And bakc to the main menu.")
    print()
    return new_name
    
def closure():  #Farewell
    print()
    print("Thanks for using Little Orphan Annie's Encrpytion Program!")
    print("And don't forget, More Ovaltine, Please!")
    sys.exit()

main()
    
