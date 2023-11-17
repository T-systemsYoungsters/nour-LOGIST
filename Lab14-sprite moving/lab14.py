import pygame
import random
import math
import player_library
import goodblock_library
import badblock_library
#------------------------------------Global constants --------------------------------- 
BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

#--------------------------------------- Classes ----------------------------------------  
#--------------Game class----------------- 
class Game(object): 
    def __init__(self):
        """ Constructor. Create all our attributes and initialize the game. """
 
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
            block = goodblock_library.Goodblock("diamond.png",SCREEN_WIDTH,SCREEN_HEIGHT)
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)
            self.good_block_list.add(block)
            self.all_sprites_list.add(block)
        
         # Create the bad block sprites
        for i in range(50):
            block = badblock_library.Badblock("stone.png",SCREEN_WIDTH,SCREEN_HEIGHT)
             # Set a random center location for the block to orbit
            block.center_x = random.randrange(SCREEN_WIDTH)
            block.center_y = random.randrange(SCREEN_HEIGHT)
            # Random radius from 10 to 200
            block.radius = random.randrange(10, 200)
            # Random start angle from 0 to 2pi
            block.angle = random.random() * 2 * math.pi
            # radians per frame
            block.speed = 0.008
            # Add the block to the list of objects
            self.bad_block_list.add(block)
            self.all_sprites_list.add(block)

        # Create the player
        self.player = player_library.Player(50,50,SCREEN_WIDTH,SCREEN_HEIGHT)
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