import math

def main():

    length_miles = int(input('What was the length in miles (mi)? '))
    minutes = int(input('What was the time in minutes (m)? '))
    seconds = int(input('What was the time in seconds (s)? '))
    Conversion_Hours = minutes/60 + seconds/3600
    print ("")
    confirm (length_miles, minutes, seconds)
    print('')
    mph_conversion(length_miles, Conversion_Hours)

def confirm(length_miles, minutes, seconds):
    print('These are the inputted values we will be using:')
    print (length_miles, "miles")
    print (minutes, "minutes")
    print (seconds, "seconds")

def mph_conversion(length_miles, Conversion_Hours):
    mph = length_miles/Conversion_Hours
    print ('The horse ran',mph,' miles per hour.')

main()
