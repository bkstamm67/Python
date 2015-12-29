#Brian Stamm
#CSC 110 - 11/11/14
#HW 6:  Binary Number Game

import random       #Done for random numbers
import sys          #Done to exit the program at the end
WINNING = 10        #Score needed to win/end game, GLOBAL CONSTANT!!!!!!

def main():
    computer_score = 0     #Starting score for computer
    player_score = 0       #Starting score for player 
    instruction(WINNING)   #Instructions of game
    while computer_score < WINNING and player_score < WINNING:
        print("Here's the score:")#Statement of scores
        print("Computer - ",computer_score)
        print("You - ",player_score)
        print('')
        game = base_value() #Randomization of Integer or Binary version of game
        if game == 0: #Starts the binary version of game
            score = binary_game()
            if score == 1: #If player gets correct, adds point to player
                player_score+=1
            else: #If player wrong, adds point to computer
                computer_score+=1
        else: #Starts the integer version of the game
            score = integer_game()
            if score == 1: #If player right, adds point to player
                player_score+=1
            else: #If wrong, adds point to computer
                computer_score+=1
    closure(computer_score, player_score, WINNING) #End of the game, when someone gets to WINNING total
              
def instruction(WINNING): #Instructions for the game, location of GLOBAL WINNING
    print("Welcome to the Binary Number Game!")
    print("In in this game, it pits you against the computer!")
    print('')
    print("The computer will show you one of two types of numbers:")
    print("Either a binary number, with a bunch of 0's and 1's,")
    print("or an integer number.  The value of the number will be")
    print("between 1 and 100.  Now, this value is randomly picked,") 
    print("and what you must do to get a point is to convert that")
    print("number into the other form!")
    print("So, if you get a binary, what's that as an integer, OR")
    print("if you get a integer, what's that in the binary form?")
    print("Make sense?  Good!")
    print('')
    print("If you do this successfully, then you get a point....")
    print("If not, the computer gets a point.  First to get to",WINNING,"is the winner!") #Location of GLOBAL WINNING
    print("Best of luck!")
    print('')

def base_value(): #Randomization between integer game and binary game, random value 0 or 1
    number = random.randint(0,1)
    return number

def integer_game(): #Integer game
    number=random.randint(1,100)
    print("Here's a random integer -",number)
    player_guess = input('What is that in binary: ')
    converted_guess = int(player_guess,2) #Converts input to a binary number
    if converted_guess == number: #if correct answer
        print("Congrats, you get a point!")
        print('')
        score = 1 #scoring a point for player
        return score
    else:
        print("Sorry, the computer gets a point :( ")
        print('Here\'s the correct answer: ',"{0:b}".format(number)) #Shows the correct answer
        print('')
        score = 0 #No point for player, instead for computer
        return score

def binary_game(): #Binary game
    number=random.randint(1,100)
    print('Here\'s a random binary number -',"{0:b}".format(number)) #Converts random number to binary
    player_guess = int(input('What is that as an integer: '))
    if player_guess == number:
        print("Congrats, you get a point!")
        print('')
        score = 1 #Scores a point
        return score
    else:
        print("Sorry, the computer gets a point :(")
        print("Here's the correct answer: ",number) #Shows correct answer
        print('')
        score = 0 #No point for player, instead for computer
        return score
    
def closure(computer_score,player_score,WINNING): #Ends program, location of GLOBAL CONSTANT!
    if player_score == WINNING: #location of GLOBAL CONSTANT!
        print("Congrats!") #If player got winning score, a congrats!
        print("Seems like you know your binary and integers!")
        sys.exit()
        
    else:
        print("Too bad, guess you need a little practice!") #If not, a gentle push toward practice
        sys.exit()
    
main()
