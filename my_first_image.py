import pygame
from math import pi
import time

# Define some colors
SKY = (28, 63, 94)
BLUE= (69, 147, 146)
GRAY =(139, 139, 139)
GRAY2 =(161, 161, 161)
BLACK2 = (0, 0, 0)
BLACK = (48, 45, 45)
WHITE = (255, 255, 255)
GRASS = (26, 109, 55)
RED = (207, 35, 35)
BROWN = (104, 52, 21)
GREEN = (80, 136, 58)
YELLOW = (245, 239, 0)
PURPLE = (133, 6, 202)
BEIGE = (239, 219, 165)
TAXI  = (255,195,51)
TAXI_SIGN = (109,209,136)

RED_LIGHT = (255,5,51)
GREEN_LIGHT = (153,255,51)
ORANGE_LIGHT = (255,153,51)
GRAY_LIGHT = (224,224,224)

light_state=0
start_time = pygame.time.get_ticks()


# x postition for the plane
x_plane = 200
x_plane_change=5

# y postition for the hand
y_hand = 495
y_hand_change = 0.5

# x and y position for the Taxi
x_taxi =800
y_taxi =600
x_taxi_change = 2


pygame.init()
 
# Set the width and height of the screen [width, height]
screen_width = 1000
screen_height = 800
size = (screen_width,screen_height)
screen = pygame.display.set_mode(size)

font = pygame.font.Font(None,18)
text = font.render("TAXI", True,BLACK)


pygame.display.set_caption("My First Image :)")
 
# Loop until the user clicks the close button.
done = False
stars_num = 30
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -----------------Main Program Loop -----------------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # ------------Game logic should go here-------------
    
    #----for the plane ----
    x_plane += x_plane_change
    if x_plane > 1000 : 
         x_plane = -1000

    #----for the hand ----
    y_hand += y_hand_change
    if y_hand > 515 : 
         y_hand = 495

    #----for the taxi----
    x_taxi -= x_taxi_change
    if x_taxi <= 0 : 
       x_taxi = 900

    #-------Traffic lights-------
    current_time = pygame.time.get_ticks()
    time = current_time - start_time

    light_state = (time // 3000)%4
    
    # -----------Screen-clearing code goes here------------
    screen.fill(SKY)

    #--------------------Draw the stars--------------------
    x_star = 20
    y_star = 40
    y_offset = 0
    x_offset = 0 

    while x_offset < 1000:
        pygame.draw.polygon(screen,WHITE,[[x_star+x_offset, y_star+y_offset], [x_star+5+x_offset, y_star+5+y_offset ], 
                            [x_star+x_offset, y_star+10+y_offset], [x_star-5+x_offset, y_star+5+y_offset]],0)
        y_offset =(-1)* y_offset + 100
        x_offset =x_offset + 100

    #--------------------Draw the moon--------------------
    pygame.draw.circle(screen, GRAY, [100, 100], 60)

    #--------------------Draw an plane---------------------
    pygame.draw.ellipse(screen,WHITE,[x_plane,100,100,30])
    plane_window_offset = 0 

    while plane_window_offset < 60:
        pygame.draw.circle(screen, GRAY2, [x_plane+35+plane_window_offset, 115],5)
        plane_window_offset += 20

    pygame.draw.polygon(screen,BLUE,[[x_plane+60,100],[x_plane+20,80],[x_plane+20,102]] )
    pygame.draw.polygon(screen,BLUE,[[x_plane+60,130],[x_plane+20,150],[x_plane+20,127]] )


    #--------------------Draw gras-----------------------
    pygame.draw.rect(screen,GRASS,[0,400,1000,450],0)

    #--------------------Draw trees----------------------
    x_tree_offset = 0 
    while x_tree_offset <= 460:
        pygame.draw.rect(screen,BROWN,[100+x_tree_offset, 350, 30,100])
        pygame.draw.polygon(screen,GREEN,[[120+x_tree_offset, 250], [30+x_tree_offset, 350], [200+x_tree_offset, 350]])
        pygame.draw.polygon(screen,GREEN,[[120+x_tree_offset, 200], [50+x_tree_offset, 300], [180+x_tree_offset, 300]])
        pygame.draw.polygon(screen,GREEN,[[120+x_tree_offset, 180], [70+x_tree_offset, 250], [160+x_tree_offset, 250]])
        x_tree_offset += 230

    #--------------------Draw a House---------------------
    pygame.draw.rect(screen,BLACK,[700, 350, 200,200])
    pygame.draw.polygon(screen,BLACK,[[900,350],[950,300],[950,500], [900,550]])
    pygame.draw.polygon(screen,RED,[[805,225], [700,350], [900, 350]])
    pygame.draw.polygon(screen,RED,[[805,225], [900, 350], [950,300]])

    #the left window of the house
    pygame.draw.rect(screen,WHITE,[730, 400, 40,40])
    pygame.draw.line(screen, BLACK, [750, 400], [750, 440], 5)
    pygame.draw.line(screen, BLACK, [730, 420], [770, 420], 5)

    #the right window of the house
    pygame.draw.rect(screen,WHITE,[830, 400, 40,40])
    pygame.draw.line(screen, BLACK, [850, 400], [850, 440], 5)
    pygame.draw.line(screen, BLACK, [830, 420], [870, 420], 5)

    #the door of the house
    pygame.draw.rect(screen,WHITE,[775, 480, 50,70])
    pygame.draw.circle(screen, BLACK, [780, 515], 3)
    pygame.draw.circle(screen, YELLOW, [800, 480], 25, 0, draw_top_right=True)
    pygame.draw.circle(screen, YELLOW, [800, 480], 25, 0, draw_top_left=True)

    #----------------the road------------------------
    pygame.draw.rect(screen,GRAY2,[0, 600, 1000,100])
    pygame.draw.polygon(screen,GRAY2,[[775,550],[825,550],[805,600], [750,600]])
    x_road_offset = 0 
    while x_road_offset <= 1000:
        pygame.draw.rect(screen,WHITE,[0+x_road_offset, 640, 25,10])
        x_road_offset += 80
    
    #------------------Draw a traffic light----------
    pygame.draw.rect(screen,BLACK,[50,450,30,65])
    pygame.draw.rect(screen,BLACK,[62,450,6,150])

    pygame.draw.circle(screen, GRAY_LIGHT, [65,463], 8)
    pygame.draw.circle(screen, GRAY_LIGHT, [65,483], 8)
    pygame.draw.circle(screen, GRAY_LIGHT, [65,503], 8)

    if light_state == 0 :
        pygame.draw.circle(screen, GREEN_LIGHT, [65,503], 8)
    elif light_state == 1:
        pygame.draw.circle(screen, RED_LIGHT, [65,463], 8)
    elif light_state == 2:
        pygame.draw.circle(screen, ORANGE_LIGHT, [65,483], 8)
    elif light_state == 3:
        pygame.draw.circle(screen, GREEN_LIGHT, [65,503], 8)
    #------------------Draw Taxi---------------------
    pygame.draw.polygon(screen,TAXI,[[x_taxi,y_taxi], [x_taxi+200,y_taxi], [x_taxi+200,y_taxi+50], [x_taxi,y_taxi+50]])
    pygame.draw.polygon(screen,WHITE,[[x_taxi+50,y_taxi], [x_taxi+50,y_taxi-30], [x_taxi+150,y_taxi-30],[x_taxi+150,y_taxi]])

    #Door handle
    pygame.draw.rect(screen,BLACK,[x_taxi+85, y_taxi+10, 8,5])
    pygame.draw.rect(screen,BLACK,[x_taxi+140, y_taxi+10, 8,5])
    
    # taxi boeders
    pygame.draw.polygon(screen,BLACK,[[x_taxi,y_taxi], [x_taxi+200,y_taxi], [x_taxi+200,y_taxi+50], [x_taxi,y_taxi+50]],4)
    pygame.draw.polygon(screen,BLACK,[[x_taxi+50,y_taxi], [x_taxi+50,y_taxi-30], [x_taxi+150,y_taxi-30],[x_taxi+150,y_taxi]],4)
    
    pygame.draw.line(screen,BLACK,[x_taxi+100,y_taxi-30],[x_taxi+100,y_taxi+50],4)
    pygame.draw.line(screen,BLACK,[x_taxi+50,y_taxi],[x_taxi+150,y_taxi],4)

    #the car wheels
    pygame.draw.circle(screen, BLACK, [x_taxi+50, y_taxi+55], 20)
    pygame.draw.circle(screen,GRAY, [x_taxi+50, y_taxi+55], 10)
    pygame.draw.circle(screen, BLACK, [x_taxi+150,y_taxi+55], 20)
    pygame.draw.circle(screen, GRAY, [x_taxi+150,y_taxi+55], 10)

    #car light
    pygame.draw.rect(screen,TAXI,[x_taxi-10, y_taxi+8, 10,10])
    pygame.draw.rect(screen,BLACK,[x_taxi-10, y_taxi+8, 10,10],2)

    #car sign
    pygame.draw.rect(screen,TAXI_SIGN,[x_taxi+75, y_taxi-45, 50,15])
    pygame.draw.rect(screen,BLACK,[x_taxi+75, y_taxi-45, 50,15],2)
    screen.blit(text,[x_taxi+85,y_taxi-43])
    #-----------------------Draw a man-------------------------
    #Hair
    pygame.draw.rect(screen,BROWN,[400, 467, 25,20])
    #Head
    pygame.draw.polygon(screen,BEIGE,[[400,470], [425,470], [425,493], [410,493], [410,500], [400,500]])
    #eye
    pygame.draw.circle(screen, BLACK2, [420,480], 3)
    
    #Body
    pygame.draw.polygon(screen,BLUE,[[400,500], [425,500], [425,510], 
                                     [440,y_hand], [440,y_hand+5], 
                                     [425,515], [425,520],[400,520]])

    pygame.draw.polygon(screen,BLACK2,[[400,520], [425,520], [425,540], [435,540], [435,545], 
                                      [405,545], [405,550], [425,550], [425,555], [400,555]])
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()