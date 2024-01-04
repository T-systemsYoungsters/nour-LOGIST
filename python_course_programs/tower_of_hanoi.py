import pygame
import random


# Initialize pygame
pygame.init()

font = pygame.font.Font(None,50)
number_of_discs=int(input("Please enter the number of the decks : "))
deck_width=200
deck_heigh=50

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Set the height and width of the screen
size = [1000, 800]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tower of Hanoi")



while not done:
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
    #---------------------------------------------------------First Step (Events handeln)---------------------------------
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    #---------------------------------------------------------Secound Step (Game Logic)-----------------------------------      
    def draw_discs(num_of_decks):
        n=0
        y=600
        x=200
        for i in range(number_of_discs) :
            R=random.randint(0,255)
            G=random.randint(0,255)
            B=random.randint(0,255)
            color = (R,G,B) 
            y = y - deck_heigh
            
            pygame.draw.rect(screen, color, (x,y, deck_width-n, deck_heigh))
            n = n + 20
            x = x + 20
     
    #---------------------------------------------------------tird Step (Clear the screen)--------------------------------  
    # Clear the screen and set the screen background
    screen.fill((255,255,255))
    #---------------------------------------------------------Fourth Step (draw objects)----------------------------------

    
    pygame.draw.line(screen, (0,0,0),[100, 600], [900, 600], 5)

    pygame.draw.line(screen, (0,0,0),[300, 200], [300, 600], 5)
    a = font.render("A", True,[0,0,0])
    screen.blit(a,[300,650])

    pygame.draw.line(screen, (0,0,0),[500, 200], [500, 600], 5)
    b = font.render("B", True,[0,0,0])
    screen.blit(b,[500,650])

    pygame.draw.line(screen, (0,0,0),[700, 200], [700, 600], 5)
    c = font.render("C", True,[0,0,0])
    screen.blit(c,[700,650])

    draw_discs(number_of_discs)
    
    #--------------------------------------------------------fifth Step (Flip the screen)--------------------------------
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
#---------------------------------------------------------sixth Step (End the game and clear all)-------------------------
pygame.quit()



