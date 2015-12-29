#Brian Stamm
#CSC 110
#HW 10 - Cellular Automata
#12.4.14

CELLS=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
#GLOBAL CONSTANT (tuple), can change to change the # of iterations

def main():
    instructions()
    function()
    closure()

def instructions():  #Basic instructions
    print("Welcome to Brian's Cellular Automata 'Game!'")
    print("This will be simulating a simple one-dimensional")
    print("cellular automation.  \"+\"'s symbolizes alive cells,")
    print("while the \"-\"'s are dead cells.  We start with 65")
    print("alive cells.  Cells changed based on their neighbors:")
    print("all the same - alive, any different, death.")
    print("Past the seen boundaries are dead cells.")
    print()
    print("So, now you get to choose how many iterations this")
    print("simulation runs through.  The first line is all alive cells,")
    print("and then the program will run through your iterations.")
    print("Be sure to put a whole number. Try a range of numbers!")
    print("After it goes through once, the program will ask if")
    print("you want to try again.  Enjoy!")
    print()

def function(): #Contains 'while' loop which keeps running the simulation
    again = 'y'
    while again == 'y' or again == 'Y':
        futher_instr() #Function which runs the automata
        print()
        again = input("Do you want to go again (Y/y is yes, anything else, no): ")
        print()

def closure():
    print("Thanks for trying Brian's Cellular Automata 'Game!'")
    print("The end.")

def futher_instr():  #Function running simulation
    cells=list(CELLS)#GLOBAL CONSTANT!
    i=0 #Counter for iterations
    try:
        iteration=int(input("How many steps: ")) #Counts how many times person want to run automata
        print()
        display(cells) #function changes 0's & 1's to +/-'s
        while i<iteration:
            x=0 #Counter cells
            new_cells=[] #empty cell list, emptied each time it starts
            while x<len(cells): #Starts going through cells list
                if x==0 and cells[x]==1 and cells[x+1]==cells[x]: #For the first cell
                    new_cells.append(0)
                    x+=1
                elif x==0: #Still for first cell
                    new_cells.append(1)
                    x+=1
                elif x>0 and x<len(cells)-1: #Anything between 1 and end
                    if cells[x-1]==cells[x] and cells[x]==cells[x+1]:
                        new_cells.append(0)
                        x+=1
                    else:
                        new_cells.append(1)
                        x+=1
                elif x==len(cells)-1 and cells[x]==1 and cells[x-1]==cells[x]:#Last cell
                    new_cells.append(0)
                    x+=1
                else: #Also last cell
                    new_cells.append(1)
                    x+=1
            i+=1 #For iteration count
            cells=new_cells #Changes cells to equal new cells, so program can run through another 'step'
            display(new_cells) #Function to change 0/1 to +/-
    except ValueError as err:  #In case iteration is not an integer
        print()
        print("I'm sorry, I didn't understand that.  Let's try")
        print("again.  Remeber, I only understand whole numbers.")

def display(group):#Changes cells into +/-
    for i in group:
        if i==0:
            print('+', end='')
        elif i==1:
            print('-', end='')
    print()
            
main()
