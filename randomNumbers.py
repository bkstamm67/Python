import random

def main():
    characters = 'abcdefghijklmnopqrstuvwxyz'
    string = ''
    for count in range(10):
        number = random.randint(0, 25)
        print("Here's the letter: ", characters[number])
        string += characters[number]

    print("Done with for loop.")
    print("Now, here's string: ", string)
main()

