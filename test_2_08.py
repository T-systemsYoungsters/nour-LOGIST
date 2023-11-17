import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#position of rectangel
x = 100
y = 100

#vector / direction speed of rectangel
change_x = 5
change_y = 3


pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    x += change_x
   
    
    if x > 649 or x < 0: 
        change_x *= -1
   
    if y > 449 or y < 0:
        change_y *= -1

    # --- Screen-clearing code goes here
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    pygame.draw.circle(screen,WHITE,(x,y-20),20)
    pygame.draw.rect(screen,WHITE,[x-2,y,4,60])
    pygame.draw.rect(screen,WHITE,[x-2,y+60,4,60])
    pygame.draw.rect(screen,WHITE,[x-40,y,40*2,4])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()