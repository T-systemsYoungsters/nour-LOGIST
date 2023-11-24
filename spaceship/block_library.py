import pygame
import random

class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
    def __init__(self, filename:str ,width:int ,height:int):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.SCREEN_WIDTH:int = width
        self.SCREEN_HEIGHT:int = height

        self.image = pygame.image.load(filename).convert()

        if filename == "images/stone.png" or filename == "images/big-diamond.png"  or filename == "images/add_heart.png" or filename == "images/new_laser.png":
            self.image.set_colorkey((0,0,0))
        else:
            self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
    
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off the screen. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(self.SCREEN_WIDTH)
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 1
        if self.rect.y > self.SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()