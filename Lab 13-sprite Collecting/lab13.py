import pygame
import random
 
#------------------------------------Global constants ---------------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (122, 209, 226)
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

 
# Current position
x_coord = 10
y_coord = 10
#--------------------------------------- Classes ---------------------------------------- 
#--------------Block class-----------------
class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
 
    def __init__(self,filename):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        if filename == "stone.png" :
            self.image.set_colorkey(BLACK)
        else:
            self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
    
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 1
 
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()
 
#--------------player class-----------------
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        # Set height, width
        self.image = pygame.image.load("alien.png").convert()
        self.image.set_colorkey(BLACK)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        #load a sound
        self.hit_screen_borders_sound = pygame.mixer.Sound("bump.wav")

        # Speed in pixels per frame
        self.x_speed_player = 0
        self.y_speed_player = 0 
    
    def changespeed(self,x,y):
        self.x_speed_player += x
        self.y_speed_player += y

    #limit the tree's movement within the screen bounderies 
    def update(self):

        #limit the player movement within the screen bounderies
        if self.rect.x < 0:
            self.hit_screen_borders_sound.play()
            self.rect.x = 0 


        elif self.rect.x + 64  > SCREEN_WIDTH:
            self.hit_screen_borders_sound.play()
            self.rect.x = SCREEN_WIDTH - 64

        else:
           self.rect.x += self.x_speed_player

        if self.rect.y  < 0 :   
            self.hit_screen_borders_sound.play()  
            self.rect.y  = 0

        elif self.rect.y +64  > SCREEN_HEIGHT :
            
            self.hit_screen_borders_sound.play()
            self.rect.y  = SCREEN_HEIGHT- 64

        else:
            self.rect.y += self.y_speed_player  
       
 
#--------------Game class----------------- 
class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """
 
    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """
 
        self.score = 0
        self.game_over = False
 
        # Create sprite lists
        self.good_block_list = pygame.sprite.Group()
        self.bad_block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        #load sounds
        self.collect_sound = pygame.mixer.Sound("collect.wav")
        self.crash_sound = pygame.mixer.Sound("bomb.wav")
        

        # Create the good block sprites
        for i in range(50):
            block = Block("diamond.png")
 
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)
 
            self.good_block_list.add(block)
            self.all_sprites_list.add(block)

         # Create the bad block sprites
        for i in range(50):
            block = Block("stone.png")
 
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)
 
            self.bad_block_list.add(block)
            self.all_sprites_list.add(block)

        # Create the player
        self.player = Player(50,50)
        self.all_sprites_list.add(self.player)
 
    def process_events(self):
        """ Process all of the events. Return a "True" if we need to close the window. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            
            # Set the speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 3)
    
            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -3)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False
 
    def run_logic(self,screen):
        """This method is run each time through the frame. It updates positions and checks for collisions."""
       
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()
 
            # See if the player block has collided with good blocks.
            good_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.good_block_list, True)
            
            # See if the player block has collided with good blocks.
            bad_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.bad_block_list, False)

            # Check the list of collisions.
            for block in good_blocks_hit_list:
                self.score += 1
                self.collect_sound.play()

            for block in bad_blocks_hit_list:
                self.game_over = True
                self.crash_sound.play()
 
            if len(self.good_block_list) == 0:
                self.game_over = True
 
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(WHITE)

        #Display the score
        font = pygame.font.Font(None, 25)
        text = font.render("Score :"+str(self.score), True, BLACK)
        screen.blit(text, [0, 0])
             
        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
       
        if not self.game_over:
            self.all_sprites_list.draw(screen)
 
        pygame.display.flip()
 
# -----------------------------------Main Function-----------------------------------
def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)
 
    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = Game()
 
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Update object positions, check for collisions
        game.run_logic(screen)
 
        # Draw the current frame
        game.display_frame(screen)

        # Pause for the next frame
        clock.tick(60)
 
    # Close window and exit
    pygame.quit()
 
#----------------------Call the main function, start up the game------------------
if __name__ == "__main__":
    main()