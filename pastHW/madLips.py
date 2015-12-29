#Brian Stamm
#CSC 110
#HW 1 - Mad Lips
#9.29.14 v2

#Original story
#The other day, I was walking with my dog, and then the most amazing thing happened!
#We were in the middle of Discovery Park, and then a leprechaun jumped out of the bushes!
#“Hello, my name is Patrick!  And I will grant you 1 wish(es)!”  
#“Well, Patrick, I was really wanting…" I started to say.
#When, Patrick stopped me, saying, “No, I was talking to your dog!”
#At that point, my dog gave an excited bark, and Patrick disappeared!
#When we got home, our house was filled with bones! 

#Instructions, so users know what to expect.

print ("Hello!  Welcome to Brian’s Mad Lips Program!")
print ("In case you have never played Mad Libs, you will be asked to pick a variety of different words.")
print ("Those words will be inserted into a story.  Hopefully, with funny outcomes!")
print ("Time to get started!")
print ('')

#Inputs.

past_part = input('Please pick a present participle (verb with -ing): ')
pet = input('Please pick an animal: ')
adj_one = input('Please pick an adjective: ')
proper_place = input('Please pick a Proper Place: ')
noun_one = input('Please pick a noun: ')
name = input('Please pick a name: ')
number = input('Favorite number: ')
adj_two = input('Time for another adjective: ')
onomatopoeia = input('What about an onomatopoeia: ')
past_verb = input('Almost there!  Now a verb in the past tense: ')
noun_two = input('Finally, a plural noun: ')
print ('') #Used for spacing, same for the outputs.  To help visually with the program

#Outputs

print ('Thanks for all the great words!  Now, story time!')#Transition
print ('')
print ('The other day, I was %s with my %s,'%(past_part, pet))
print ('and then the most',adj_one,'thing happened!')
print ('We were in the middle of %s, and then a %s jumped out of the bushes!'%(proper_place,noun_one))
print ('')
print ('“Hello, my name is %s!  And I will grant you %s wishes!”' %(name,number))  
print ('')
print ('“Well, %s, I was really wanting…” I started to say.'%(name))
print ('')
print ('When %s stopped me, saying, “No, I was talking to your %s!”'%(name,pet))
print ('')
print ('At that point, my %s gave an %s %s, and %s disappeared!'%(pet,adj_two,onomatopoeia,name))
print ('When we got home, our house was %s with %s'%(past_verb, noun_two)) 
print('')
print ('')
print ("Well, I hope that you enjoyed the story!   Thanks for trying Brian's Mad Lips Program!")
