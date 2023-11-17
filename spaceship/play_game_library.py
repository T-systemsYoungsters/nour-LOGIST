import pygame
import random
import math
import player_library
import goodblock_library
import badblock_library
import bullet_library
import data_library
#------------------------------------Global constants --------------------------------- 
BLACK = (0,0,0)
WHITE = (255,255,255)
BUTTON_COLOR = (53,80,90)
BUTTON_SHADOW = (212,255,255)
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800

#--Load images
HEART = pygame.image.load("images/heart.png")
BACKGROUND_IMAGE = pygame.image.load("images/stern.jpg")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE,(SCREEN_WIDTH,SCREEN_HEIGHT))
 

#--------------Class Game-------------------
class Game(): 
    def __init__(self,name):
        #--creat an instance from the Data class work with the JASON file
        self.data_manger = data_library.Data()

        #--player data
        self.player_name = name
        self.player_score = self.data_manger.get_score(self.player_name)

        self.score = 0
        self.player_lives = 5
        #-- when the player loses 
        self.game_over = [False, self.player_name, self.player_score, "Game Over!"]
 

        # Initial values for the background image
        self.background_speed = 2  
        self.background_x = 0
        self.background_y = 0

        # Create sprite lists
        self.good_block_list = pygame.sprite.Group()
        self.bad_block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        # List of each bullet
        self.bullet_list = pygame.sprite.Group()

        #--load sounds
        self.collect_sound = pygame.mixer.Sound("sounds/collect.wav")
        self.crash_sound = pygame.mixer.Sound("sounds/bomb.wav")
        self.shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")

        #--Background Music
        pygame.mixer.music.load('sounds/bgmusic.wav')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()
        
        # Create the good block sprites
        self.create_blocks("good_block",50,SCREEN_HEIGHT)

        # Create the bad block sprites
        self.create_blocks("bad_block",50,SCREEN_HEIGHT)

        # Create the player
        self.player = player_library.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT-100,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.all_sprites_list.add(self.player)

    def create_blocks(self,type,size,y_pos):
        if type == "good_block":  
            # Create the good block sprites
            for block in range(size):
                block = goodblock_library.Goodblock("images/diamond.png",SCREEN_WIDTH,SCREEN_HEIGHT)
                block.rect.x = random.randrange(SCREEN_WIDTH)
                block.rect.y = random.randrange(-300, y_pos)
                self.good_block_list.add(block)
                self.all_sprites_list.add(block)
         
        elif type == "bad_block":
            # Create the bad block sprites
            for block in range(size):
                block = badblock_library.Badblock("images/stone.png",SCREEN_WIDTH,SCREEN_HEIGHT)
                # Set a random center location for the block to orbit
                block.center_x = random.randrange(SCREEN_WIDTH)
                block.center_y = random.randrange(-300,y_pos)
                # Random radius from 10 to 200
                block.radius = random.randrange(10, 200)
                # Random start angle from 0 to 2pi
                block.angle = random.random() * 2 * math.pi
                # radians per frame
                block.speed = 0.008
                # Add the block to the list of objects
                self.bad_block_list.add(block)
                self.all_sprites_list.add(block)

    def process_events(self):
        """ Process all of the events. Return a "True" if we need to close the window. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #--Before ending the game check if the player has reached a new high score
                if self.player_score < self.score:
                    self.data_manger.edit_highscore(self.player_name,self.score)
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

                elif event.key == pygame.K_SPACE:
                    self.shoot_sound.play()
                    # Fire a bullet if the user clicks space key
                    self.bullet = bullet_library.Bullet()
                    # Set the bullet so it is where the player is
                    self.bullet.rect.x = self.player.rect.x
                    self.bullet.rect.y = self.player.rect.y
                    # Add the bullet to the lists
                    self.all_sprites_list.add(self.bullet)
                    self.bullet_list.add(self.bullet)

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
                    self.__init__(self.player_name)
                    
            if event.type == pygame.constants.USEREVENT:
            # This event is triggered when the song stops playing.
                pygame.mixer.music.load('sounds/bgmusic.wav')
                pygame.mixer.music.play()
        return False
 
    def run_logic(self):
        #-----Update the background image location(make it moves)
        self.background_x -= self.background_speed
        if self.background_x < -SCREEN_WIDTH :
            self.background_x=0

        if self.game_over[0] == False:
            # Move all the sprites
            self.all_sprites_list.update()
        
        #-----Calculate mechanics for each bullet
        for bullet in self.bullet_list:
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, self.bad_block_list, True)
    
            # For each block hit, remove the bullet
            for block in block_hit_list:
                self.bullet_list.remove(bullet)
                self.all_sprites_list.remove(bullet)
    
            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                self.bullet_list.remove(bullet)
                self.all_sprites_list.remove(bullet)

            
        # See if the player block has collided with good blocks(Diamonds).
        good_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.good_block_list, True)
            
        # See if the player block has collided with bad blocks(Rocks).
        bad_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.bad_block_list, True)

        # Check the list of collisions.
        for block in good_blocks_hit_list:
            self.score += 1
            self.collect_sound.play()

        for block in bad_blocks_hit_list:
            self.crash_sound.play()
            self.player_lives -= 1
            # Make the player invisible  
            self.player.image.set_alpha(0)

            if self.player_lives <= 0:
                #--Before ending the game check if the player has reached a new high score
                if self.player_score < self.score:
                    self.game_over[2] = self.score
                    self.data_manger.edit_highscore(self.player_name,self.score)
                self.game_over[0] = True
            
        # If player has lives left, gradually increase alpha to make the player reappear
        if self.player_lives > 0 and (self.player.image.get_alpha()) is not None and (self.player.image.get_alpha() < 255):
            alpha_value = min(self.player.image.get_alpha() + 2, 255)
            self.player.image.set_alpha(alpha_value)   

        # Recreate blocks(Rocks and diamonds)
        if len(self.good_block_list) <= 20:
            self.create_blocks("good_block",10,-100)

        if len(self.bad_block_list) <= 25:
            self.create_blocks("bad_block",35,-25)

    def display_frame(self, screen):
        # Set the background image to the screen 
        screen.blit(BACKGROUND_IMAGE, [self.background_x, 0])
        screen.blit(BACKGROUND_IMAGE, [self.background_x + SCREEN_WIDTH, 0])

        #Display player lives
        font = pygame.font.Font(None, 25)
        lives = font.render("Lives :", True, WHITE)
        screen.blit(lives, [2, 0])
        x =70
        for live in range(self.player_lives):
            screen.blit(HEART,[x ,0])
            x += 30

        #Display player Name
        font = pygame.font.Font(None, 25)
        player_score = font.render("Player name :"+self.player_name, True, WHITE)
        screen.blit(player_score, [2, 25])


        #Display the high score
        font = pygame.font.Font(None, 25)
        player_score = font.render("High score :"+str(self.player_score), True, WHITE)
        screen.blit(player_score, [2, 50])

        #Display the score
        font = pygame.font.Font(None, 25)
        score = font.render("Score :"+str(self.score), True, WHITE)
        screen.blit(score, [2, 75])
       
        if self.game_over[0]:
            if self.player_score < self.score:
                self.game_over[3] = "Congratulations, you have reached a new high score "+str(self.score)
                return self.game_over
        else: 
            self.all_sprites_list.draw(screen)
        
        pygame.display.flip()
        return self.game_over