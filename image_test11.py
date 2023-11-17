import pygame
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#--------------------------Draw Functions----------------------


#set up
pygame.init()
 
# Set the width and height of the screen 
screen = pygame.display.set_mode([900,700])

pygame.display.set_caption("Adding an image")
 
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)

# loads images
background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("player.png").convert()
#to hide the background of the image (Transparent Background)
player_image.set_colorkey(BLACK)


#load a sound
my_sound = pygame.mixer.Sound("laser5.ogg")

# -----------------Main Program Loop -----------------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            #play the sound
            my_sound.play()
    # ------------Game logic should go here-------------
    
    player_position = pygame.mouse.get_pos()
    x_pos = player_position[0]
    y_pos = player_position[1]
    
   

    # -----------Screen-clearing code goes here------------
    #fill the screen with an image 
    screen.blit(background_image,[0,0])
    screen.blit(player_image,[x_pos,y_pos])

    #-------------Draw objects-----------


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()