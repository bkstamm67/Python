#Brian Stamm
#CSC 110 - Dr. West
#10.21.14
#Homework 4 - Drawing

#This program is NOT interactive, and it draws the same picture every time.  Running this program, you must
#have the Gui tool (Gui3.py) to run this properly, and it must be saved in the same file as this.

from Gui import *  # - as mentioned, Gui3.py is also needed for this program 

CANVAS_WIDTH = 1500 #Dimensions - These are constants
CANVAS_HEIGHT = 950

def main():
    canvas.config(bg = 'green')
    canvas.circle([500, 350],75, fill = 'yellow', outline = 'black', width = 2.5) #Sun in the upper corner
    draw_ponds(375,-265,125)#This creates 2 ponds
    draw_complete_house()  #This draws the whole house/factory
    draw_smoke_rising(-327.5, 140, 35) #This draws the rising smoke from the house/factory, more below.
    draw_tree_cluster(650, 0, 100) #This has cluster of 3 trees, more information below
    draw_tree_cluster(450,0,80)
    draw_tree_cluster(585, -265, 225)
    draw_tree_cluster(-40, -30, 65)
    draw_tree_cluster(60, -120 , 120)
    draw_simple_tree(-80, -150, 140) #This draws one tree, more below
    draw_simple_tree(-100, -180, 160)

def draw_ponds(x,y,radius):  #This draws 2 ponds.  1st pond is based on inputted coordinates. 
    canvas.circle([x,y],radius, fill = 'dark blue', outline='dark blue') #1st Pond
    canvas.circle([x-300,y],radius*.5,fill='dark blue', outline='dark blue')#2nd Pond, which is 300 pixels to the left of 1st, 1/2 the size.

def draw_smoke_rising (x, y, radius):  #This contains the 3 smoke circles.  
    smoke(x, y, radius) #Smoke is anchored to this smoke circle - furtherest to bottom right
    smoke(x*1.4, y*1.60, radius*1.5)
    smoke(x*2, y*2, radius*2)

def smoke(x,y,radius): #This creates the circle for the smoke
    canvas.circle([x, y], radius, fill = 'black')

def draw_complete_house():#Each item you have to put in their own coordinates
    canvas.rectangle([[-700, -250],[-300,0]], outline='black', fill = 'brown') # This is the building.
    canvas.rectangle([[-355, 0],[-300,95]], outline= 'black', fill = 'gray')# This creates the chimney
    canvas.rectangle([[-525,-250],[-475,-175]], outline= 'black', fill = 'white') #This creates the door
    canvas.circle([-490,-212.5],5, fill = 'yellow') #Door knob
    draw_simple_windows(-615,-175,45)#Creates a window with coordinates, bottom left window.  Refer below for more information
    draw_simple_windows(-375,-175,45)#bottom right window
    draw_simple_windows(-615,-75,45)#top left window
    draw_simple_windows(-375,-75,45)#top right window

def draw_simple_windows(x,y,size):#Creates the window+pane, using coordinates 
    canvas.rectangle([[x-size*.5,y-size*.5],[x+size*.5,y+size*.5]], outline='black', fill='yellow')#Block window
    canvas.line([[x,y-size*.5],[x,y+size*.5]], width=2)#Window pane, updown
    canvas.line([[x-size*.5,y],[x+size*.5,y]], width=2)#Window pane, leftright
                     

def draw_tree_cluster(x, y, size):#Draws a cluster of 3 trees
    draw_simple_tree(x - size * 0.15, y + size * 0.5, size * 0.5)
    draw_simple_tree(x - size * 0.3, y + size * 0.3, size * 0.6)
    draw_simple_tree(x, y, size * 0.8)

def draw_simple_tree(base_x, base_y, height):#Draws a single tree
#First Trunk
    trunk_x1 = base_x - height * 0.05
    trunk_x2 = base_x + height * 0.05
    trunk_y1 = base_y
    trunk_y2 = base_y + height * 0.5
    canvas.rectangle([[trunk_x1, trunk_y1], [trunk_x2, trunk_y2]], \
                     fill='brown', width = 0)
    # draw crown
    # the polygon has 3 points, peak, lower left (LL), and lower right (LR)
    LL_x = base_x - height * 0.2
    LR_x = base_x + height * 0.2
    L_y = base_y + height * 0.3
    canvas.polygon([[base_x, base_y + height], [LL_x, L_y], [LR_x, L_y]], \
                   fill='darkgreen', width=0)

###################################################################DoNOT change

g = Gui()
g.title("Brian's Homework Wk 4: Python's Impression of Picasso's Brick Factory at Tortosa")

# canvas is the drawing area
canvas = g.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
main()
g.mainloop()
