import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        
        super().__init__()
        # Set height, width
        self.SCREEN_WIDTH=width
        self.SCREEN_HEIGHT=height

        #load the image
        self.image = pygame.image.load("images/alien.png").convert()
        self.image.set_colorkey((0,0,0))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        
        #load a sound
        self.hit_screen_borders_sound = pygame.mixer.Sound("sounds/bump.wav")

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


        elif self.rect.x + 64  > self.SCREEN_WIDTH:
            self.hit_screen_borders_sound.play()
            self.rect.x = self.SCREEN_WIDTH - 64

        else:
           self.rect.x += self.x_speed_player

        if self.rect.y  < 0 :   
            self.hit_screen_borders_sound.play()  
            self.rect.y  = 0

        elif self.rect.y +64  > self.SCREEN_HEIGHT :
            
            self.hit_screen_borders_sound.play()
            self.rect.y  = self.SCREEN_HEIGHT- 64

        else:
            self.rect.y += self.y_speed_player  