import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#--------------------------------------Classes Section--------------------------------------
#--------RECTANGLE-----------
class Rectangle():
    def __init__(self):
        self.x = random.randrange(0,701)
        self.y = random.randrange(0,501)
        self.change_x =  random.randrange(-3,4)
        self.change_y =  random.randrange(-3,4)
        self.width = random.randrange(20,71)
        self.height =  random.randrange(20,71)
        self.color = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.width,self.height])

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

#----------ELLIPS-------------
class Ellips(Rectangle):
    def __init__(self):
        super().__init__()
        
    def draw(self,screen):
        pygame.draw.ellipse(screen,self.color,[self.x,self.y,self.width,self.height])


#--------------------------------------Game initialization------------------------------------
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My shapes")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# An empty list for my shapes
my_list =[]

#----------------------------------Create Objects--------------------------------------------
for i in range(1000):
    my_rectangle = Rectangle()
    my_list.append(my_rectangle)

for j in range(1000):
    my_ellips = Ellips()
    my_list.append(my_ellips)


# --------------------------------------Main Program Loop ------------------------------------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # ------------------------------Game logic should go here---------------------------------
   
    for item in my_list:
        item.move()

    # --- -----------------------Screen-clearing code goes here-------------------------------
    screen.fill(BLACK)
 
    # ---------------------------- Drawing code should go here--------------------------------
    for item in my_list:
        item.draw(screen)
      
    

    # ----------------Go ahead and update the screen with what we've drawn.-------------------
    pygame.display.flip()
 
    # ------------------------------Limit to 60 frames per second-----------------------------
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()