import pygame
import random
import math
import player_library
import goodblock_library
import badblock_library
import bullet_library
import data_library
import constants
from datetime import datetime

#--------------Class Game-------------------
class Game(): 
    def __init__(self,name:str):
        self.start_time = datetime.now()
        #--to generate two spical diamond (each 1min)
        self.current_time:int = 0
        self.interval:int =60000 # 1 min

        #--to generate two heart (each 1.5min)
        self.current_time_heart:int = 0
        self.interval_heart:int =90000 # 1.5 min

        #--to generate an icon to get a new laser (each 2min)
        self.current_time_laser:int = 0
        self.interval_laser:int =120000 # 2 min

        #-- new laser expiration time
        self.current_time_new_laser:int = 0
        self.interval_new_laser:int =15000 # 15sec
        self.new_laser_flag:bool = False

        #--creat an instance from the Data class work with the JASON file
        self.data_manger = data_library.Data()

        #--player data
        self.player_name:str = name
        self.player_score:int = self.data_manger.get_score(self.player_name)

        #--Set the intial values of the score and player lives
        self.score:int = 0
        self.player_lives:int = 5

        #--when the player loses 
        self.game_over:list = [False, self.player_name, self.player_score, "Game Over!"]
 
        #--Initial values for the background image
        self.background_speed:int = 2  
        self.background_x:int = 0
        self.background_y:int = 0

        #--Create sprite lists
        self.good_block_list = pygame.sprite.Group()
        self.bad_block_list = pygame.sprite.Group()
        self.spical_diamonds_list = pygame.sprite.Group()
        self.heart_list = pygame.sprite.Group()
        self.new_laser = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        #--List of each bullet
        self.bullet_list = pygame.sprite.Group()

        #--Load sounds
        self.collect_sound = pygame.mixer.Sound("sounds/collect.wav")
        self.crash_sound = pygame.mixer.Sound("sounds/bomb.wav")
        self.shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")

        #--Background Music
        pygame.mixer.music.load('sounds/bgmusic.wav')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()
        
        # Create the good block sprites
        self.create_blocks("good_block",50,constants.SCREEN_HEIGHT)

        # Create the bad block sprites
        self.create_blocks("bad_block",100,constants.SCREEN_HEIGHT)

        # Create the player
        self.player = player_library.Player(constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT-100,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
        self.all_sprites_list.add(self.player)

    def create_blocks(self, type:str, size:int, y_pos:int):
        if type == "good_block":  
            # Create the good block sprites
            for block in range(size):
                block = goodblock_library.Goodblock("images/diamond.png",constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
                block.rect.x = random.randrange(constants.SCREEN_WIDTH)
                block.rect.y = random.randrange(-300, y_pos)
                self.good_block_list.add(block)
                self.all_sprites_list.add(block)
         
        elif type == "bad_block":
            # Create the bad block sprites
            for block in range(size):
                block = badblock_library.Badblock("images/stone.png", constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
                # Set a random center location for the block to orbit
                block.center_x = random.randrange(constants.SCREEN_WIDTH)
                block.center_y = random.randrange(-150,y_pos)
                # Random radius from 10 to 200
                block.radius = random.randrange(10, 800)
                # Random start angle from 0 to 2pi
                block.angle = random.random() * 2 * math.pi
                # radians per frame
                block.speed = 0.0006
                # Add the block to the list of objects
                self.bad_block_list.add(block)
                self.all_sprites_list.add(block)

        elif type == "special_diamond":
            for block in range(size):
                block = goodblock_library.Goodblock("images/big-diamond.png",constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
                block.rect.x = random.randrange(constants.SCREEN_WIDTH)
                block.rect.y = random.randrange(-300, y_pos)
                self.spical_diamonds_list.add(block)
                self.all_sprites_list.add(block)

        elif type == "add_heart":
            for block in range(size):
                block = goodblock_library.Goodblock("images/add_heart.png",constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
                block.rect.x = random.randrange(constants.SCREEN_WIDTH)
                block.rect.y = random.randrange(-300, y_pos)
                self.heart_list.add(block)
                self.all_sprites_list.add(block)

        elif type == "new_laser":
            block = goodblock_library.Goodblock("images/new_laser.png",constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
            block.rect.x = random.randrange(constants.SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, y_pos)
            self.new_laser.add(block)
            self.all_sprites_list.add(block)

    def process_events(self):
        """ Process all of the events. Return a "True" if we need to close the window. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #--Before ending the game check if the player has reached a new high score
                if self.player_score < self.score:
                    self.data_manger.edit_highscore(self.player_name,self.score)
                return True
            
            # Set the player speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 3)

                # Fire a bullet if the user clicks space key
                elif event.key == pygame.K_SPACE:
                    self.shoot_sound.play()
                    #--Check which weapon the player has
                    if not self.new_laser_flag:
                        #------------Regular weapon that shoots in one dirction-------------
                        self.bullet = bullet_library.Bullet("images/laser.png",-1)
                        self.bullet.rect.x = self.player.rect.x
                        self.bullet.rect.y = self.player.rect.y
                        # Add the bullet to the lists
                        self.all_sprites_list.add(self.bullet)
                        self.bullet_list.add(self.bullet)
                    else:
                        #------------The new weapon that shoots in all directions-----------
                        # Define angles for bullets in different directions
                        angles = [0, 45, 90, 135, 180, 225, 270, 315]
                        # Create bullets with different angles and add them to the lists
                        for angle in angles:
                            bullet = bullet_library.Bullet("images/laserN.png",angle)
                            bullet.rect.center = self.player.rect.center  # Set the bullet at the player's center
                            self.all_sprites_list.add(bullet)
                            self.bullet_list.add(bullet)

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

            # This event is triggered when the song stops playing.
            if event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('sounds/bgmusic.wav')
                pygame.mixer.music.play()

        return False
 
    def run_logic(self):
        #-----Update the background image location(make it moves)
        self.background_x -= self.background_speed
        if self.background_x < -constants.SCREEN_WIDTH :
            self.background_x = 0

        if self.game_over[0] == False:
            # Move all the sprites
            self.all_sprites_list.update()

       
        # Get the current time
        current_time = datetime.now()
        elapsed_time = (current_time - self.start_time).total_seconds()*1000
        #elapsed_time= pygame.time.get_ticks()

        #------------Generate two spical diamonds each 1min-----------
        # Check if 1 min have passed 
        if elapsed_time - self.current_time >= self.interval:
            self.create_blocks("special_diamond",2,-100)
            self.current_time = elapsed_time

        #------------Generate a heart each 1.5 min-----------  
        # Check if 1.5 min have passed 
        if elapsed_time - self.current_time_heart >= self.interval_heart:
            self.create_blocks("add_heart",1,-100)
            self.current_time_heart = elapsed_time

        #------------Generate a new laser  each 2 min-----------  
        # Check if 2min have passed 
        if elapsed_time - self.current_time_laser >= self.interval_laser:
            self.create_blocks("new_laser",1,-100)
            self.current_time_laser = elapsed_time
                           
        #------------After 15Sec return to the regular laser weapon(by setting the new_laser_flag to false)----------- 
        # Check if 15sec have passed  
        if elapsed_time - self.current_time_new_laser >= self.interval_new_laser:
            self.new_laser_flag = False
            self.current_time_new_laser = elapsed_time
            
        # Check if the bullet has hit a stone
        for bullet in self.bullet_list: 
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

        # See if the player block has collided with spical red Diamonds.
        spical_Diamonds_hit_list = pygame.sprite.spritecollide(self.player, self.spical_diamonds_list, True)

        # See if the player block has collided with a heart.
        heart_hit_list = pygame.sprite.spritecollide(self.player, self.heart_list, True)

        # See if the player block has collided with a new laser weapon.
        laser_hit = pygame.sprite.spritecollide(self.player, self.new_laser, True)

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
                self.game_over[0] = True
            
        # If player has lives left, gradually increase alpha to make the player reappear
        if self.player_lives > 0 and (self.player.image.get_alpha()) is not None and (self.player.image.get_alpha() < 255):
            alpha_value = min(self.player.image.get_alpha() + 1, 255)
            self.player.image.set_alpha(alpha_value)   

        # Recreate blocks(Rocks and diamonds)
        if len(self.good_block_list) <= 20:
            self.create_blocks("good_block",15,-100)

        if len(self.bad_block_list) <= 70:
            self.create_blocks("bad_block",100,-100)

        # If the player has taken the big diamond, increase his score by ten 
        for block in spical_Diamonds_hit_list:
            self.collect_sound.play()
            self.score += 10
        # If the players takes a heart and his number of lives is less than five, add one to his lives
        for block in heart_hit_list:
            self.collect_sound.play()
            if self.player_lives < 5:
                self.player_lives += 1
        # If the player takes the new laser weapon, replace his old laser weapon with the new one 
        # (by setting the new_laser_flag to true)
        for block in laser_hit:
            self.collect_sound.play()
            self.new_laser_flag = True

    def display_frame(self, screen):
        # Set the background image to the screen 
        screen.blit(constants.BACKGROUND_IMAGE, [self.background_x, 0])
        screen.blit(constants.BACKGROUND_IMAGE, [self.background_x + constants.SCREEN_WIDTH, 0])

        # Display player lives
        font = pygame.font.Font(None, 25)
        lives = font.render("Lives :", True,constants.WHITE)
        screen.blit(lives, [2, 0])
        x =70
        for live in range(self.player_lives):
            screen.blit(constants.HEART,[x ,0])
            x += 30

        # Display player Name
        font = pygame.font.Font(None, 25)
        player_score = font.render("Player name :"+self.player_name, True, constants.WHITE)
        screen.blit(player_score, [2, 25])


        # Display the high score
        font = pygame.font.Font(None, 25)
        player_score = font.render("High score :"+str(self.player_score), True, constants.WHITE)
        screen.blit(player_score, [2, 50])

        # Display the score
        font = pygame.font.Font(None, 25)
        score = font.render("Score :"+str(self.score), True, constants.WHITE)
        screen.blit(score, [2, 75])
       
        # Check if the game is over or not
        if self.game_over[0]:
            if self.player_score < self.score:
                self.game_over[2] = self.score
                self.data_manger.edit_highscore(self.player_name,self.score)
                self.game_over[3] = "Congratulations, you have reached a new high score "+str(self.score)
                return self.game_over
        else: 
            self.all_sprites_list.draw(screen)
        
        pygame.display.flip()
        return self.game_over