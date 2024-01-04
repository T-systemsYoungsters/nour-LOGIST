import pygame
from math import pi
import time

# Define some colors
BLACK = (48, 45, 45)
WHITE = (255, 255, 255)
GRASS = (26, 109, 55)
RED = (207, 35, 35)
BROWN = (104, 52, 21)
GREEN = (80, 136, 58)
YELLOW = (245, 239, 0)

screen_width = 1000
screen_height = 800
size = (screen_width,screen_height)

tree_width =30
tree_height =100
#--------------------------Draw Functions----------------------

def draw_tree(screen,x,y):
    pygame.draw.rect(screen,BROWN,[70+x, 170+y, tree_width,tree_height])
    pygame.draw.polygon(screen,GREEN,[[90+x, 70+y], [x, 170+y], [170+x, 170+y]])
    pygame.draw.polygon(screen,GREEN,[[90+x, 20+y], [20+x, 120+y], [150+x, 120+y]])
    pygame.draw.polygon(screen,GREEN,[[90+x, y], [40+x, 70+y], [130+x, 70+y]])

def draw_bird(screen,x,y):
    pygame.draw.circle(screen,YELLOW,[x+45,y+5],7)
    pygame.draw.circle(screen,BLACK,[x+47,y+5.5],1.5)
    pygame.draw.line(screen,BLACK,[x+51,y+8],[x+53,y+8],3)
    pygame.draw.line(screen,YELLOW,[x+39,y+10],[x+20,y+20],3)
    pygame.draw.arc(screen, YELLOW, [x,y, 45, 25], 3 * pi / 2, 2 * pi,9)
    pygame.draw.line(screen,BLACK,[x+28,y+24],[x+28,y+27],2)




#set up
pygame.init()
 
# Set the width and height of the screen 
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Moving tree and a bird")
 
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10
# -----------------Main Program Loop -----------------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                    x_speed = -3

            elif event.key == pygame.K_RIGHT:
                    x_speed = 3

            elif event.key == pygame.K_UP:
                    y_speed = -3

            elif event.key == pygame.K_DOWN:
                    y_speed = 3
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 y_speed = 0

    # ------------Game logic should go here-------------
    
    # Call draw stick figure function
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed
    
    #limit the tree's movement within the screen bounderies
    if x_coord < 0:
        x_coord = 0 

    elif x_coord +170 > screen_width:
         x_coord = screen_width-170 

    if y_coord  < 0 :     
        y_coord = 0
    elif y_coord+tree_height+170 > screen_height:
         y_coord = screen_height-tree_height-170
    
   
        

    # -----------Screen-clearing code goes here------------
    screen.fill(WHITE)

    #-------------Draw objects-----------
    draw_tree(screen,x_coord,y_coord)
    draw_bird(screen,x,y)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()