import pygame
import math 

pygame.init
red = (255, 0 ,0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0 , 0)
PI= math.pi

size = [700,500]
screen =pygame.display.set_mode(size)
pygame.display.set_caption("Wellcome to my game")

done = False
#to control how fast the game run
clock = pygame.time.Clock()

while not done :
    # user did somthing
    for event in pygame.event.get():
        #if the user clicked close
        if event.type == pygame.QUIT:
            done = True

    screen.fill(white)

#Draw 5 lines
    #for x in range(0,100,20):
    #   pygame.draw.line(screen, green, [x, 0], [x, 100], 5)

#Draw a rectangle
    #pygame.draw.rect(screen,black, [150, 150, 250 ,100],5)
    #pygame.draw.ellipse(screen,black, [150, 150, 250 ,100],5)
    
#Draw a arc
    #pygame.draw.arc(screen,green, [150, 150, 250 ,100],PI/2 ,PI ,2)
    #pygame.draw.arc(screen,black, [150, 150, 250 ,100], 0, PI/2 ,2)
    #pygame.draw.arc(screen,red,   [150, 150, 250 ,100], 3*PI/2 , 2*PI ,2)
    #pygame.draw.arc(screen,blue,  [150, 150, 250 ,100],PI, 3*PI/2, 2)

#Draw a arc  
    pygame.draw.arc(screen,green, [0, 0, 200 ,300],PI, 3*PI/2 ,2)
    pygame.draw.arc(screen,blue,  [0, 0, 200 ,300], 3*PI/2,2*PI, 2)
    pygame.draw.arc(screen,black, [200, 0, 200 ,300], PI/2, PI ,2)
    pygame.draw.arc(screen,red,   [200, 0, 200 ,300], 0 , PI/2 ,2)
    pygame.draw.arc(screen,blue,  [400, 0, 200 ,300],PI, 3*PI/2 ,2)
    pygame.draw.arc(screen,green,  [400, 0, 200 ,300], 3*PI/2,2*PI, 2)
    pygame.display.flip()
    
    clock.tick(20)
pygame.quit()