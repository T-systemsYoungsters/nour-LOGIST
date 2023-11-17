import pygame
import time
from math import pi

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (245, 239, 0)
#--------------------------Draw Functions----------------------
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
screen = pygame.display.set_mode([700,394])

pygame.display.set_caption("Bitmapped Graphics and user control")
 
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)

# loads images
background_image = pygame.image.load("background.png").convert()


#load a sound
bird_sound = pygame.mixer.Sound("pip.flac")

# -----------------Main Program Loop -----------------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #play the sound
            #my_sound.play()
    # ------------Game logic should go here-------------
    
    pos = pygame.mouse.get_pos()
    x_bird = pos[0]
    y_bird = pos[1]

    
    bird_location = screen.get_at((x_bird,y_bird))
    tree_top =(130,104,183,255)
    lamp_top =(120,95,172,255)

    # make the bird chirp if it is on the top of the tree or on the top of the lamp
    if bird_location == tree_top or bird_location == lamp_top :
        bird_sound.play()
   

    # -----------Screen-clearing code goes here------------
    #fill the screen with an image 
    screen.blit(background_image,[0,0])
   
   

    #----------------------Draw objects--------------------
    #Call a function to drw a bird on the screen
    draw_bird(screen,x_bird,y_bird)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()