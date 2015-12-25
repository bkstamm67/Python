#Brian Stamm
#Homework 2 - Steel Tubes
#10.7.14

#This program calculates volume and surface area of an object, and then get cost of
#manufacturing it.  It does round values, which are noted in the code.  Calculations were seperated out
#from the program for ease.  Also, I attempted to have as few of variables as possible.

import math

#Instruction Section

print ('Welcome to Acme’s Rubber Wrapped Steel Tube Calculator!')
print ('')
print ('The program will need to know a few basic measurements (in centimeters)')
print ('of the Acme Rubber Wrapped Steel Tubes you would want, and then it will')
print ('help to determine the total amount of materials which need to be ordered,')
print ('cost for the order, and what the total volume of the tubes produced will be.')
print ('')


#Input

height = float(input ('What is the height (cm) desired? '))
radius = float(input ('What is the radius (cm) desired? '))
total_amount = int(input ('How many tubes do you want? '))
print ('')

#Calculations

vol_individual = math.floor(math.pi*(radius**2)*height) #rounded down
vol_total = vol_individual*total_amount #rounded value, because using rounded variable
sa_steel = (math.ceil(2*math.pi*(radius**2))+(2*math.pi*radius*height))*total_amount #rounded up
sa_rubber = (math.ceil(2*math.pi*(radius**2))+((2*math.pi*radius+0.5)*height))*total_amount #rounded up
steel_cost = 0.12*sa_steel #using rounded variable
rubber_cost = 0.04*sa_rubber #using rounded variable
total_cost = steel_cost+rubber_cost #using rounded variables

#Confirmation of Amounts

print ("Here are the amounts the calculator is using -")
print ("Height: ",height)
print ("Radius: ",radius)
print ("Total Tubes: ",total_amount)
print ('')

#Outputs, with brief note

print ('With those measurements, here is some more information about that order:')
print ('')
print ('Individual tube volume: ', format(vol_individual,',.0f'), 'cm^3')
print ('Total volume of tubes produced: ', format(vol_total,',.0f'), 'cm^3')
print ('')
print ('Acme Steel Tube surface area: ', format(sa_steel,',.0f'), 'cm^2')
print ('Acme Rubber Tube surface area: ', format(sa_rubber,',.0f'), 'cm^2')
print ('')
print ('Cost of steel for order:  $', format(steel_cost,',.2f'), sep='')
print ('Cost of rubber for order: $', format(rubber_cost,',.2f'), sep='')
print ('Total cost of material: $', format(total_cost,',.2f'), sep='')
print ('')
print ('Hopefully with this information, you now feel confident in completing your')
print ('order with Acme.  Please contact us at our national hotline at (888) 555-5555.')
print ("Thanks, and we'll wait to hear from you!")

#Test Cases - 1st - h=98,r=22,#=13.  When I ran thru it, got vol_individual=149012.02
#vol_total=1937156.296, sa_steel=215638.92, sa_rubber=215.645.42, steel_cost=25876.67
#rubber_cost=8625.82, with a total=34502.49.  When I ran it, the numbers were close
#especially considering the rounding.

#Test Case 2 - h=20,r=5,#=10, vol_individual=1570.796, vol_total=15707.9,
#sa_steel=7853.98, sa_rubber=7068.58, steel_cost=942.48
#rubber_cost=282.24, with a total=1225.22
