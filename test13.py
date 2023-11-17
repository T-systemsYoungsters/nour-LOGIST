import pygame
import random

# Define some colors and constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

#--------------------------------------Classes Section--------------------------------------
#---------------Blocks-----------------
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block,  (to draw on it)and fill it with a color, this could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        #by default it will take the top left cornen (x=0 , y=0) and width and height of the rectangle are thedimensions of the image 
        self.rect = self.image.get_rect()

    def reset_pos(self): 
        # to make the block start reset above the screen and then slide on the screen 
        # -20 because the block height is 15
        self.rect.y = random.randrange(-SCREEN_HEIGHT,-20)
        # in order to not repeat the same pattern , -20 is the width of the block
        self.rect.x = random.randrange(SCREEN_WIDTH-20)

    #make the blocks moves
    def update(self):
        self.rect.y += 1 
        #make the blocks reset to the top of the screen when they fall off 
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


#---------------player-----------------
class Player(Block):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def update(self):
        # Get the current mouse position. This returns the position as a list of two numbers.
        pos = pygame.mouse.get_pos()
        
        # Fetch the x and y out of the list,just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]


#--------------------------------------Game initialization------------------------------------
pygame.init()
 
# Set the width and height of the screen [width, height]

screen = pygame.display.set_mode(SIZE)
 
pygame.display.set_caption("Sprites")
 
# This is a list of 'sprites.' Each block in the program is added to this list. The list is managed by a class called 'Group.'
#it represent for example the players in my game
block_list = pygame.sprite.Group()

# This is a list of every sprite, all blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
#the number of collided blocks by the player
score = 0


#----------------------------------Create Objects--------------------------------------------
#-------------create the blocks----------------------
for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(SCREEN_WIDTH)
    block.rect.y = random.randrange(SCREEN_HEIGHT)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

#-------------Create a RED player block----------------------
#if i am loading an image i have to remove the width(20) and the height(15)
player = Player(RED, 20, 15)
all_sprites_list.add(player)
 

# --------------------------------------Main Program Loop ------------------------------------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # ------------------------------Game logic should go here---------------------------------
    
    #--------make all the blocks move /make the player move too----------
    all_sprites_list.update()


    
    # See if the player block has collided with anything.
    #true means that when the player hit a block  remove that block from block_list and saves it in blocks_hit_list
    #false means not removing it (and the game will keep going even if the player collect 50 blocks)
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
        block.reset_pos()

    # --- -----------------------Screen-clearing code goes here-------------------------------
    screen.fill(WHITE)
 
    # ---------------------------- Drawing code should go here--------------------------------

    # Draw all the spites
    all_sprites_list.draw(screen)
    

    # ----------------Go ahead and update the screen with what we've drawn.-------------------
    pygame.display.flip()
 
    # ------------------------------Limit to 60 frames per second-----------------------------
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()