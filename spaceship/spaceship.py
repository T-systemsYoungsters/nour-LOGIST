import pygame
import pygame.locals
import data_library
import play_game_library
import sys
#------------------------------------Global constants --------------------------------- 
BLACK = (0,0,0)
WHITE = (255,255,255)
BUTTON_COLOR = (53,80,90)
BUTTON_SHADOW = (212,255,255)
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800

#--Load images
GAME_LOGO_IMAAGE = pygame.image.load("images/spaceship.png")
GAME_LOGO_IMAAGE = pygame.transform.scale(GAME_LOGO_IMAAGE,(500,250)) 
HEART = pygame.image.load("images/heart.png")
BACKGROUND_IMAGE = pygame.image.load("images/stern.jpg")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE,(SCREEN_WIDTH,SCREEN_HEIGHT))

class Menu():
    def __init__(self):
        pygame.init()
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Spaceship")
        self.done = False

        self.clock = pygame.time.Clock()

        # New player name
        self.player_name=""

        # Player Name that already exists
        self.loaded_player_name=""

        # To display the players
        self.current_player = 0

        #--creat an instance from the Data class work with the JASON file
        self.data_manger = data_library.Data()

        # Initial values for the background image
        self.background_speed = 2  
        self.background_x = 0
        self.background_y = 0

        #--Background Music
        pygame.mixer.music.load('sounds/bgmusic.wav')
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()
        
    def draw_button(self, screen, x, y, text,button_type=None):
        # Create a Rect object for the button
        button_rect = pygame.Rect(x, y, 200, 100)
        # Draw shadow 
        shadow_rect = button_rect.copy()
        shadow_rect.inflate_ip(10, 10)  # Increase the size of the shadow
        pygame.draw.rect(screen, BUTTON_SHADOW, shadow_rect,0,10)

        # Draw the button
        rect=pygame.draw.rect(screen, BUTTON_COLOR, button_rect,0,10)

        # Create text surface and get its Rect
        font = pygame.font.Font(None, 35)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=button_rect.center)

        # Blit the text onto the screen
        screen.blit(text_surface, text_rect.topleft)   
        if button_type == "player_name_button": 
            self.loaded_player_name = text
        
        #elif button_type == "delet_player_button":
        #    return text
        return rect  

    def input_box(self, screen, x, y):
        #--Label
        font = pygame.font.Font(None, 36)
        label_surface = font.render("Enter the player name", True, WHITE)
        label_rect = label_surface.get_rect(topleft=(x-30, y-40))
        screen.blit(label_surface, label_rect)

        #--Input Box
        input_rect = pygame.Rect(x, y , 200, 100)
        input_rect_shadow = input_rect.copy()
        # Draw shadow 
        input_rect_shadow.inflate_ip(10, 10)  # Increase the size of the shadow
        pygame.draw.rect(screen, BUTTON_SHADOW, input_rect_shadow,0,10)


        font = pygame.font.Font(None, 36)
        input_surface = font.render(self.player_name, True, WHITE)
        # Adjust the width of the input box based on the text width
        input_rect.w = max(200, input_surface.get_width() + 10)
        # Adjust the width of the shadow box
        input_rect_shadow.w= input_rect.w + 10
        
        pygame.draw.rect(screen, BUTTON_SHADOW, input_rect_shadow, 0,10)
        pygame.draw.rect(screen, BUTTON_COLOR, input_rect, 0,10)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
        

        return input_rect
    
    #---------------------------Main Menu----------------------------
    def main_menu(self):
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                # Check if the mouse click is within the bounds of the specific button
                    if self.quit_game_button.collidepoint(event.pos):
                        return True
                    
                    elif self.start_game_button.collidepoint(event.pos) :
                        return self.start_menu()
                    
                if event.type == pygame.constants.USEREVENT:
                # This event is triggered when the song stops playing.
                    pygame.mixer.music.load('sounds/bgmusic.wav')
                    pygame.mixer.music.play()

            # --- Game logic should go here
            #-----Update the background image location(make it moves)
            self.background_x -= self.background_speed
            if self.background_x < -SCREEN_WIDTH :
                self.background_x=0

            # --- Screen-clearing 
            # Set the background image to the screen 
            self.screen.blit(BACKGROUND_IMAGE, [self.background_x, 0])
            self.screen.blit(BACKGROUND_IMAGE, [self.background_x + SCREEN_WIDTH, 0])
            self.screen.blit(GAME_LOGO_IMAAGE,[(SCREEN_WIDTH/2)-250,50])
        
            # --- Drawing code should go here
            #draw the start game button
            self.start_game_button=self.draw_button(self.screen,(SCREEN_WIDTH/2)-110,300,"Start Game")
            #draw the Quit game button
            self.quit_game_button=self.draw_button(self.screen,(SCREEN_WIDTH/2)-110,450,"Quit Game")

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            self.clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()
        sys.exit()
    
    #---------------------------Start Menu----------------------------
    def start_menu(self):
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                # Check if the mouse click is within the bounds of the specific button
                    if self.new_player_button.collidepoint(event.pos) :
                        return self.create_player_menu()
                    
                    elif self.Load_player_button.collidepoint(event.pos) :
                        return self.load_players_menu()
                    
                    elif self.back_button.collidepoint(event.pos) :
                        return self.main_menu()
                    
                if event.type == pygame.constants.USEREVENT:
                # This event is triggered when the song stops playing.
                    pygame.mixer.music.load('sounds/bgmusic.wav')
                    pygame.mixer.music.play()

            # --- Game logic should go here
            #-----Update the background image location(make it moves)
            self.background_x -= self.background_speed
            if self.background_x < -SCREEN_WIDTH :
                self.background_x=0

            # --- Screen-clearing 
            # Set the background image to the screen 
            self.screen.blit(BACKGROUND_IMAGE, [self.background_x, 0])
            self.screen.blit(BACKGROUND_IMAGE, [self.background_x + SCREEN_WIDTH, 0])
            self.screen.blit(GAME_LOGO_IMAAGE,[(SCREEN_WIDTH/2)-250,50])
        
            # --- Drawing code should go here
            #draw the new player  button
            self.new_player_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)-110,300,"New Player")
            #draw the load player button
            self.Load_player_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)-110,450,"Load Player")
            #draw the back player button
            self.back_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)-110,600,"Back")

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            self.clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()
        sys.exit()
    
    #-----------------------Create player Menu-------------------------
    def create_player_menu(self):
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                # Check if the mouse click is within the bounds of the specific button
                    if self.done_button.collidepoint(event.pos) and self.player_name!="":
                        #save the new player in JASON file
                        self.data_manger.add_player(self.player_name)
                        return self.play_game(self.player_name)
                    
                    elif self.back_button.collidepoint(event.pos) :
                        return self.start_menu()
                    
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        # Perform actions when Enter key is pressed
                        print("Player name entered:", self.player_name)
                    else:
                        self.player_name += event.unicode

                if event.type == pygame.constants.USEREVENT:
                # This event is triggered when the song stops playing.
                    pygame.mixer.music.load('sounds/bgmusic.wav')
                    pygame.mixer.music.play()

            # --- Game logic should go here
            #-----Update the background image location(make it moves)
            self.background_x -= self.background_speed
            if self.background_x < -SCREEN_WIDTH :
                self.background_x=0

            # --- Screen-clearing 
            # Set the background image to the screen 
            self.screen.blit(BACKGROUND_IMAGE, [self.background_x, 0])
            self.screen.blit(BACKGROUND_IMAGE, [self.background_x + SCREEN_WIDTH, 0])
            self.screen.blit(GAME_LOGO_IMAAGE,[(SCREEN_WIDTH/2)-250,50])
        
            # --- Drawing code should go here
            #draw the input box
            self.input_field = self.input_box(self.screen,(SCREEN_WIDTH/2)-110,300)
            #draw the done button
            self.done_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)-110,450,"Done")
            #draw the back player button
            self.back_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)-110,600,"Back")

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            self.clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()
        sys.exit()
    
    #-------------------------Load players Menu------------------------
    def load_players_menu(self):
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                # Check if the mouse click is within the bounds of the specific button
                    if self.player_name_button.collidepoint(event.pos) :
                        self.play_game(self.loaded_player_name)
                        
                    elif self.delete_player_button.collidepoint(event.pos) :
                        self.data_manger.delete_player(self.loaded_player_name)

                    elif self.back_button.collidepoint(event.pos) :
                        return self.start_menu()
                    
                    elif self.next_player_button.collidepoint(event.pos) :
                        self.current_player += 1
                        
                    elif self.previous_player_button.collidepoint(event.pos) :
                        self.current_player -= 1
                        
                    
                if event.type == pygame.constants.USEREVENT:
                # This event is triggered when the song stops playing.
                    pygame.mixer.music.load('sounds/bgmusic.wav')
                    pygame.mixer.music.play()

            # --- Game logic should go here
            #-----Update the background image location(make it moves)
            self.background_x -= self.background_speed
            if self.background_x < -SCREEN_WIDTH :
                self.background_x=0

            # --- Screen-clearing 
            # Set the background image to the screen 
            self.screen.blit(BACKGROUND_IMAGE, [self.background_x, 0])
            self.screen.blit(BACKGROUND_IMAGE, [self.background_x + SCREEN_WIDTH, 0])
            self.screen.blit(GAME_LOGO_IMAAGE,[(SCREEN_WIDTH/2)-250,50])
        
            # --- Drawing code should go here
            #Get the player from the JSON file
            players_data = self.data_manger.get_players()

            if self.current_player < 0 :
                self.current_player = 0
            elif self.current_player >= len(players_data):
                 self.current_player = len(players_data)-1
            else: 
                #draw the name player button
                self.player_name_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)-340,300,players_data[self.current_player][0],"player_name_button")
                #draw player highscore button
                self.highscore_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)-100,300,"Highscore : "+str(players_data[self.current_player][1]))
                #draw the delete player button
                self.delete_player_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)+140,300,"Delete Player")
            
            #draw the next player button
            self.next_player_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)-100,420,"Next player")
            #draw the previous player button
            self.previous_player_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)-100,540,"Previous player")
            #draw the back player button
            self.back_button = self.draw_button(self.screen,(SCREEN_WIDTH/2)-100,660,"Back")

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            self.clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()
        sys.exit()
   
    #---------------------------Game Over Menu-------------------------
    def menu(self,name,score,sentence):

        self.playerName = name
        self.playerScore = score
        self.sentence = sentence
       
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                # Check if the mouse click is within the bounds of the specific button
                    if self.quit_game_button.collidepoint(event.pos):
                        return True

                    elif self.main_menu_button.collidepoint(event.pos) :
                        return self.main_menu()
                     
                    elif self.try_again_button.collidepoint(event.pos) :
                        return self.play_game(self.playerName)
                    
                if event.type == pygame.constants.USEREVENT:
                # This event is triggered when the song stops playing.
                    pygame.mixer.music.load('sounds/bgmusic.wav')
                    pygame.mixer.music.play()

            # --- Game logic should go here
            #-----Update the background image location(make it moves)
            self.background_x -= self.background_speed
            if self.background_x < -SCREEN_WIDTH :
                self.background_x=0

            # --- Screen-clearing 
            # Set the background image to the screen 
            self.screen.blit(BACKGROUND_IMAGE, [self.background_x, 0])
            self.screen.blit(BACKGROUND_IMAGE, [self.background_x + SCREEN_WIDTH, 0])


            font = pygame.font.SysFont("serif", 45)
            text = font.render(self.sentence, True, WHITE)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2)-200 - (text.get_height() // 2)
            self.screen.blit(text, [center_x, center_y])

            # --- Drawing code should go here
            #draw the start game button
            self.try_again_button=self.draw_button(self.screen,(SCREEN_WIDTH/2)-110,300,"Tray again")
            #draw the main menu  button
            self.main_menu_button=self.draw_button(self.screen,(SCREEN_WIDTH/2)-110,450,"Main menu")
            #draw the Quit game button
            self.quit_game_button=self.draw_button(self.screen,(SCREEN_WIDTH/2)-110,600,"Quit Game")

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            self.clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()
        sys.exit()
   
    #---------------------------play Game ------------------------------
    def play_game(self,name):
        pygame.mouse.set_visible(False)
        # Create an instance of the Game class
        game = play_game_library.Game(name)

        self.game_over=[]
        self.game_over_flag=False
        # Main game loop
        while not self.done and not self.game_over_flag:
            # Process events (keystrokes, mouse clicks, etc)
            self.done = game.process_events()
    
            # Update object positions, check for collisions
            game.run_logic()
                
            # Draw the current frame
            self.game_over = game.display_frame(self.screen)

            if self.game_over[0]==True:
                pygame.mouse.set_visible(True)
                self.menu(self.game_over[1], self.game_over[2],self.game_over[3])
                self.game_over_flag=True
            # Pause for the next frame
            self.clock.tick(60)
        # Close window and exit
        pygame.quit()
        sys.exit()

# -----------------------------------Main Function-----------------------------------
def main():
    menu = Menu()
    menu.main_menu()
#----------------------Call the main function, start up the game------------------
if __name__ == "__main__":
    main()   

    