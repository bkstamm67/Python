#Brian Stamm
#CSC 110 - Dr. West
#10.29.14
#Homework 5 - Sandy's Sub Shop

import sys

SALES_TAX = 0.095  #Percentage as a decimal, GLOBAL!

def main():
    intro()                                                         #Introduction function, explain basics to users, HAS SPECIALS LISTED (marked)
    instructions()                                                  #Explicit instructions on ordering - could be combined to Intro, but done to help if ever changing specials or names of subs
    sub_type = get_sub_type()                                       #Returns the size of sub ordered
    sub_num = get_sub_num()                                         #Returns amount of subs ordered
    confirmation(sub_type, sub_num)                                 #Confirming amounts inputted by user    
    calculations = get_sales(sub_type,sub_num)                      #Calculation of sale
    print("The amount for your Sandy's Subs is $",format(calculations,',.2f'),sep='')
    show_sales_tax = get_sales_tax(calculations, SALES_TAX)         #Calc sales tax
    print('And total sales tax is $',format(show_sales_tax,',.2f'),sep='')
    total_amount = total_cost(show_sales_tax, calculations)          #Calc Total cost(sale+sales tax)
    print('And your total is $',format(total_amount,',.2f'),sep='')
    print('')
    closure()                                                       #Little goodbye for users

def intro():
    print("Welcome to Sandy's Sub Shop's Swift Orderer!")
    print("This program will walk you through your order at Sandy's.")
    print("Currently, here are the prices and specials at Sandy's:")
    print('')
    print("Small Sub\t - $5.99 each") #Small sub, no special
    print("Regular Sub\t - $9.99 each, and a second is $5.99!")#Regular sub, special
    print("Jumbo Sub\t - $20.99 each.  If you get 3 or more, you get 10% off!")#Jumbo sub, special
    print('')
    print("Please input your order following the directions below.")
    print('')

def instructions():#Contains small, regular, jumbo for sizes
    print("For Sandy's Small Sub, please enter S.")
    print("For the Regular, R.")
    print("And for the Jumbo, J.")
    print("Also, we'll ask you how many you want too.  Be sure to enter a number.")
    print("We can't do half orders.....Yet.  Anyway, let's get started!")
    print('')

def get_sub_type():
    sub = input("Enter what size of Sandy's Sub you would like: ")
    if sub=='j' or sub=='J': #For Jumbo
        return 'J' #all caps to keep consistent, same for all sizes
    elif sub=='r' or sub=='R': #for Regular
        return 'R'
    elif sub=='s' or sub=='S': #for Small
        return 'S'
    else: #For any other input.  ENDS PROGRAM!
        print("Sorry, we did not understand what size you wanted.")
        print("If you want to try to order again, please start from the beginning.")
        print('')
        sys.exit()
    
def get_sub_num():
    total = int(input("And how many of those would you like: "))
    if total>0: #To insure total positive number
        return total
    elif total==0: #What happens when you stay up too late programming, you think of weird possible inputs/outputs.  Easter egg?
        print("Well, it seems like you're just not interested in having some of Sandy's")
        print("Subs today!  Shucks!  Come on back when you're hungry.  We'll be waiting!")
        sys.exit()
    else: #For any other input.  ENDS PROGRAM!
        print("Sorry, we did not understand how many subs you wanted.")
        print("If you want to try to order again, please start from the beginning.")
        print('')
        sys.exit()

def confirmation(number_1,number_2): #User has to press ENTER to proceed/confirm order
    print('')
    print("To confirm, we have that you are ordering",number_2,"subs,")
    print("And they are all",number_1,"types of Sandy Subs.")
    print("If that is correct, press enter for your total.")
    input("")

def get_sales(sub,number):
    if sub =='S':                   #Cost of SMALL sub
        return 5.99*number
    elif sub =='R':                                         #Cost of REGULAR sub
        if number%2==1:                                     #if odd amount
            return((number-1)/2)*(9.99+5.99)+9.99 
        elif number%2==0:                                   #if even
            return (number/2)*(9.99+5.99)
        else:
            return 9.99                                      #if 1
    elif sub =='J':                         #Cost of JUMBO sub
        if number<3:                        #regular Jumbo
            return number*(20.99)
        else:                               #Jumbo Speical
            return (number*(20.99)*.9)
    else: #Again, what happens if you stay up too late.  Can't think of way this would be called.  Easter egg for programs?
        print("Huh?  Didn't really expect this one.")
        sys.exit()

def get_sales_tax(number, tax):     #Sales Tax
    total = number*(tax)
    return total

def total_cost(tax, cost):          #Sales Tax + Cost
    total = tax + cost
    return total
    
def closure():  #End Statement
    print("Sandy welcomes your business! As we say at Sandy's, Sandy's subs are")
    print("served sizable and are satisfyingly savory!  Open every day but Sundays.")
    print('')

main()


#Test Run 1:  7 Jumbo subs.  by hand - 7*20.99=146.93 -(ans*10%) = 132.237 *1.095= 144.799515.  Program: $144.80.  Bam.
#Test Run 2:  67 Regular subs.  by hand - 33*(9.99+5.99)+9.99=537.33*1.095=588.3763... Program: 588.38.  Bam**2
