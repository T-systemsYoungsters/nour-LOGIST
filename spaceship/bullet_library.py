import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image:str , angle:int):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.sent_angle:int = angle
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        if self.sent_angle  != -1:
            self.angle:float = math.radians(self.sent_angle)  # Convert degrees to radians
            self.speed:int = 5
 
    def update(self):
        """ Move the bullet. """
        if self.sent_angle != -1:
            self.rect.x:float = self.rect.x + self.speed * math.cos(self.angle)
            self.rect.y:float = self.rect.y - self.speed * math.sin(self.angle)
        else:
            self.rect.y:float = self.rect.y-3


