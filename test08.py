import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#position of rectangel
rect_x = 0
rect_y = 50

#vector / direction speed of rectangel
rect_change_x = 5
rect_change_y = 3

#creating random positions for the snowballs and saves them in to a list 
star_list =[]
for i  in range(50):
    x = random.randrange(0,700)
    y = random.randrange(0,500)
    star_list.append([x,y])


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
    rect_x += rect_change_x
    rect_y += rect_change_y
    
    if rect_x > 649 or rect_x < 0: 
        rect_change_x *= -1
   
    if rect_y > 449 or rect_y < 0:
        rect_change_y *= -1

    # --- Screen-clearing code goes here
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen,RED,[rect_x,rect_y,50,50])

    #-----Drawing snowballs
    for item in star_list:
        #--move the snow balls
        item[1] +=1
        pygame.draw.circle(screen,WHITE,item,2)

        #--refalling snowballs from the top of the screen
        if item[1] > 500:
            item[1]=random.randrange(500)
            item[0] = random.randrange(700)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()