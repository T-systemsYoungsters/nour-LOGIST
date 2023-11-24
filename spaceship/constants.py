import pygame

SCREEN_WIDTH:int = 1300
SCREEN_HEIGHT:int = 800
#--Colors
BLACK:list = [0,0,0]
WHITE:list = [255,255,255]
BUTTON_COLOR:list  = [53,80,90]
BUTTON_SHADOW:list  = [212,255,255]

#--Load images
HEART = pygame.image.load("images/heart.png")
GAME_LOGO_IMAAGE = pygame.image.load("images/spaceship.png")
GAME_LOGO_IMAAGE = pygame.transform.scale(GAME_LOGO_IMAAGE,(500,250))
BACKGROUND_IMAGE = pygame.image.load("images/stern.jpg")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE,(SCREEN_WIDTH,SCREEN_HEIGHT))