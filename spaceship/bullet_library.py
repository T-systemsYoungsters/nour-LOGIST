import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("images/laser2.png")
        self.rect = self.image.get_rect()

 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3